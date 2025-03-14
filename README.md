# JProfile

A simple and powerful Python library for profiling pandas DataFrames. JProfile automatically generates descriptive statistics for various data types, allowing you to quickly gain insights into the structure and quality of your data.

## Features

- **Automatic data type detection**: Automatic recognition of numeric, boolean, string, and datetime columns
- **Descriptive statistics**: Detailed statistics for each data type
- **Null value analysis**: Insights into missing data for each column
- **Duplicate detection**: Identification of unique values and duplicates
- **Simple interface**: Intuitive API that is easy to use

## Installation

```bash
# Install directly from GitHub
pip install git+https://github.com/NullP0inter3xception/jprofile.git
```

## Usage

```python
import pandas as pd
from jprofile import JProfile

# Create a sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5, None, 7, 8, 8, 10],
    'value': [10.5, 20.3, None, 40.1, 50.2, 60.7, 35.8, 42.0, 10.5, 30.6],
    'age': [25, 34, 28, 45, 52, 19, 31, 25, 39, None],
    'is_valid': [True, False, True, None, False, True, True, True, False, False],
    'name': ['Alice', 'Bob', 'Charlie', '', None, 'Eve', 'Dave', 'Alice', 'Frank', 'Grace'],
    'email': ['alice@example.com', 'bob@test.com', None, 'david@mail.net', 'emily@domain.org', '', 'dave@example.com', 'alice2@mail.com', 'frank@test.net', None],
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', None],
    'date': pd.to_datetime(['2023-01-01', '2023-02-01', None, '2023-04-01', '2023-05-01', '2023-06-01', '2023-01-15', '2023-02-28', '2023-04-01', '2023-07-12'])
}

df = pd.DataFrame(data)

# Profile the DataFrame
profiler = JProfile(df)

# Display the results
profiler.display_profile()

# Or get the results as a dictionary for further processing
results = profiler.get_profile()
```

## Example output

### Integer Column
```
==================================================
Column: age (Type: numeric)
==================================================
  count: 9
  null_count: 1
  null_percentage: 10.0
  unique_count: 7
  duplicate_count: 2
  min: 19
  max: 52
  mean: 33.222222222222221
  median: 31
  std: 10.867787645391981
  variance: 118.1111111111111
  q1: 25
  q3: 39
  iqr: 14
  sum: 299
  range: 33
```

### Float Column
```
==================================================
Column: value (Type: numeric)
==================================================
  count: 9
  null_count: 1
  null_percentage: 10.0
  unique_count: 8
  duplicate_count: 1
  min: 10.5
  max: 60.7
  mean: 33.411111111111111
  median: 35.8
  std: 16.717196004584767
  variance: 279.46358024691356
  q1: 15.5
  q3: 42.0
  iqr: 26.5
  sum: 300.7
  range: 50.2
```

### String Column
```
==================================================
Column: name (Type: string)
==================================================
  count: 9
  null_count: 1
  null_percentage: 10.0
  empty_count: 1
  unique_count: 7
  duplicate_count: 2
  min_length: 0
  max_length: 7
  mean_length: 4.111111111111111
  top_frequencies: {'Alice': 2, 'Bob': 1, 'Charlie': 1, 'Eve': 1, 'Dave': 1}
```

## Supported data types

JProfile analyzes the following data types with specific statistics for each:

### Numeric
- Count, null count, null percentage
- Unique values, duplicates
- Min, max, mean, median
- Standard deviation, variance
- Quartiles (Q1, Q3, IQR)
- Sum, range

### Boolean
- Count, null count, null percentage
- Unique values, duplicates
- True/False counts and percentages

### String
- Count, null count, null percentage
- Unique values, duplicates
- Empty strings
- Min/max/average length
- Top-5 frequencies

### Datetime
- Count, null count, null percentage
- Unique values, duplicates
- Min, max, range (duration)

## Requirements

- Python 3.6+
- pandas
- numpy

## License

[MIT](LICENSE)