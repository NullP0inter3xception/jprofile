import pandas as pd
from jprofile import JProfile

data = {
    'id': [1, 2, 3, 4, 5, None, 7, 8, 8, 10],
    'value': [10.5, 20.3, None, 40.1, 50.2, 60.7, 35.8, 42.0, 10.5, 30.6],
    'age': [25, 34, 28, 45, 52, 19, 31, 25, 39, None],
    'is_valid': [True, False, True, None, False, True, True, True, False, False],
    'name': ['Alice', 'Bob', 'Charlie', '', None, 'Eve', 'Dave', 'Alice', 'Frank', 'Grace'],
    'date': pd.to_datetime(['2023-01-01', '2023-02-01', None, '2023-04-01', '2023-05-01', 
                          '2023-06-01', '2023-01-15', '2023-02-28', '2023-04-01', '2023-07-12'])
}

df = pd.DataFrame(data)

profiler = JProfile(df)
profiler.display_profile()

results = profiler.get_profile()
print("\nResults for 'name' column as dictionary:")
print(results['name'])
