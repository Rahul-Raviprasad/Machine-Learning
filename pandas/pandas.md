# Pandas python library

pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

http://pandas.pydata.org/

How to read tabular(data in table) data file into pandas?

```python
import pandas as pd

items = pd.read_table('file_name.tsv')
# or from url
orders = pd.read_table('http://bit.ly/chiporders')

# We can see the first 5 rows with
orders.head() # we can pass the number of rows we want to see into head()
```
we may not get perfectly ordered data

underlying data file was formatted perfectly to work with the "read_table" method default parameters
read_table assumes
1. your file is tab separated
2. the first row was a header row

# Resources
1. read table: http://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.read_table.html
