import pandas as pd
import numpy as np
from typing import Dict, Any, List, Tuple
import datetime


class JProfile:
    """
    A simple data profiling library for pandas DataFrames.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize JProfile with a pandas DataFrame.
        
        Args:
            df: The pandas DataFrame to analyze
        """
        self.df = df
        self.results = {}
        self._analyze()
    
    def _analyze(self):
        """
        Analyze the DataFrame and store results.
        """
        # Analyze each column
        for column in self.df.columns:
            col_data = self.df[column]
            col_type = self._determine_type(col_data)
            
            if col_type == 'numeric':
                self.results[column] = self._analyze_numeric(col_data)
            elif col_type == 'boolean':
                self.results[column] = self._analyze_boolean(col_data)
            elif col_type == 'string':
                self.results[column] = self._analyze_string(col_data)
            elif col_type == 'datetime':
                self.results[column] = self._analyze_datetime(col_data)
    
    def _determine_type(self, series: pd.Series) -> str:
        """
        Determine the type of data in a pandas Series.
        
        Args:
            series: The pandas Series to analyze
            
        Returns:
            str: The data type ('numeric', 'boolean', 'string', or 'datetime')
        """
        # Handle empty series
        if series.empty or series.isna().all():
            return 'string'
            
        if pd.api.types.is_numeric_dtype(series):
            # Check if it's effectively boolean (only 0/1 values)
            unique_vals = set(series.dropna().unique())
            if unique_vals.issubset({0, 1, True, False}):
                return 'boolean'
            return 'numeric'
        elif pd.api.types.is_bool_dtype(series):
            return 'boolean'
        elif pd.api.types.is_datetime64_dtype(series):
            return 'datetime'
        else:
            # Everything else is treated as string
            return 'string'
    
    def _analyze_numeric(self, series: pd.Series) -> Dict[str, Any]:
        """
        Analyze a numeric column.
        
        Args:
            series: The pandas Series to analyze
            
        Returns:
            Dict[str, Any]: Descriptive statistics for the numeric column
        """
        total_count = len(series)
        null_count = series.isna().sum()
        non_null = series.dropna()
        
        # Calculate unique values and duplicates
        unique_count = non_null.nunique()
        duplicate_count = len(non_null) - unique_count
        
        results = {
            'type': 'numeric',
            'count': len(non_null),
            'null_count': null_count,
            'null_percentage': (null_count / total_count * 100) if total_count > 0 else 0,
            'unique_count': unique_count,
            'duplicate_count': duplicate_count,
            'min': non_null.min() if not non_null.empty else None,
            'max': non_null.max() if not non_null.empty else None,
            'mean': non_null.mean() if not non_null.empty else None,
            'median': non_null.median() if not non_null.empty else None,
            'std': non_null.std() if not non_null.empty else None,
            'variance': non_null.var() if not non_null.empty else None,
            'q1': non_null.quantile(0.25) if not non_null.empty else None,
            'q3': non_null.quantile(0.75) if not non_null.empty else None,
            'iqr': non_null.quantile(0.75) - non_null.quantile(0.25) if not non_null.empty else None,
            'sum': non_null.sum() if not non_null.empty else None,
            'range': non_null.max() - non_null.min() if not non_null.empty and len(non_null) > 1 else None
        }
        
        return results
    
    def _analyze_boolean(self, series: pd.Series) -> Dict[str, Any]:
        """
        Analyze a boolean column.
        
        Args:
            series: The pandas Series to analyze
            
        Returns:
            Dict[str, Any]: Descriptive statistics for the boolean column
        """
        total_count = len(series)
        null_count = series.isna().sum()
        non_null = series.dropna()
        
        # Convert to boolean if it's numeric (0/1)
        if pd.api.types.is_numeric_dtype(series):
            non_null = non_null.astype(bool)
        
        true_count = non_null.sum()
        false_count = len(non_null) - true_count
        
        # Calculate unique values and duplicates
        unique_count = non_null.nunique()
        duplicate_count = len(non_null) - unique_count
        
        results = {
            'type': 'boolean',
            'count': len(non_null),
            'null_count': null_count,
            'null_percentage': (null_count / total_count * 100) if total_count > 0 else 0,
            'unique_count': unique_count,
            'duplicate_count': duplicate_count,
            'true_count': true_count,
            'false_count': false_count,
            'true_percentage': (true_count / len(non_null) * 100) if len(non_null) > 0 else 0,
            'false_percentage': (false_count / len(non_null) * 100) if len(non_null) > 0 else 0
        }
        
        return results
    
    def _analyze_string(self, series: pd.Series) -> Dict[str, Any]:
        """
        Analyze a string column.
        
        Args:
            series: The pandas Series to analyze
            
        Returns:
            Dict[str, Any]: Descriptive statistics for the string column
        """
        total_count = len(series)
        null_count = series.isna().sum()
        non_null = series.dropna()
        
        # Convert all values to strings to ensure compatibility
        non_null = non_null.astype(str)
        
        # Count empty strings
        empty_count = (non_null == '').sum()
        
        # Calculate string lengths
        if not non_null.empty:
            # Safe calculation of string lengths
            try:
                lengths = non_null.str.len()
                min_length = lengths.min()
                max_length = lengths.max()
                mean_length = lengths.mean()
            except:
                # Fallback in case of error
                min_length = max_length = mean_length = None
        else:
            min_length = max_length = mean_length = None
        
        # Find unique values and duplicates
        unique_count = non_null.nunique()
        duplicate_count = len(non_null) - unique_count
        
        # Get top 5 most frequent values
        top_values = non_null.value_counts().head(5).to_dict() if not non_null.empty else {}
        
        results = {
            'type': 'string',
            'count': len(non_null),
            'null_count': null_count,
            'null_percentage': (null_count / total_count * 100) if total_count > 0 else 0,
            'empty_count': empty_count,
            'unique_count': unique_count,
            'duplicate_count': duplicate_count,
            'min_length': min_length,
            'max_length': max_length,
            'mean_length': mean_length,
            'top_frequencies': top_values
        }
        
        return results
    
    def _analyze_datetime(self, series: pd.Series) -> Dict[str, Any]:
        """
        Analyze a datetime column.
        
        Args:
            series: The pandas Series to analyze
            
        Returns:
            Dict[str, Any]: Descriptive statistics for the datetime column
        """
        total_count = len(series)
        null_count = series.isna().sum()
        non_null = series.dropna()
        
        # Calculate unique values and duplicates
        unique_count = non_null.nunique()
        duplicate_count = len(non_null) - unique_count
        
        results = {
            'type': 'datetime',
            'count': len(non_null),
            'null_count': null_count,
            'null_percentage': (null_count / total_count * 100) if total_count > 0 else 0,
            'unique_count': unique_count,
            'duplicate_count': duplicate_count,
            'min': non_null.min() if not non_null.empty else None,
            'max': non_null.max() if not non_null.empty else None,
            'range': (non_null.max() - non_null.min()) if not non_null.empty and len(non_null) > 1 else None
        }
        
        # Add mean and median for timedeltas only
        if not non_null.empty:
            if isinstance(non_null.iloc[0], pd.Timedelta):
                results['mean'] = non_null.mean()
                results['median'] = non_null.median()
        
        return results
    
    def get_profile(self) -> Dict[str, Dict[str, Any]]:
        """
        Get the full profiling results.
        
        Returns:
            Dict[str, Dict[str, Any]]: Profiling results for each column
        """
        return self.results
    
    def display_profile(self):
        """
        Display the profile results in a readable format.
        """
        for column, stats in self.results.items():
            print(f"\n{'=' * 50}")
            print(f"Column: {column} (Type: {stats['type']})")
            print(f"{'=' * 50}")
            
            for key, value in stats.items():
                if key == 'type':
                    continue
                    
                # Format datetime objects for display
                if isinstance(value, (pd.Timestamp, datetime.datetime, pd.Timedelta)):
                    print(f"  {key}: {value}")
                elif isinstance(value, dict):
                    print(f"  {key}:")
                    for sub_key, sub_value in value.items():
                        print(f"    {sub_key}: {sub_value}")
                elif isinstance(value, list) and len(value) > 5:
                    print(f"  {key}: {value[:5]} ... (truncated)")
                else:
                    print(f"  {key}: {value}")