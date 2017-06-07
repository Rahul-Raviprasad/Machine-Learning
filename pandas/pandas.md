# Pandas python library

pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

http://pandas.pydata.org/

### How to read tabular(data in table) data file into pandas?

```python
import pandas as pd

items = pd.read_table('file_name.tsv')
# or from url
orders = pd.read_table('http://bit.ly/chiporders')

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols) # here the separator used by the file was | pipe, also we are passing the header info as names.

# We can see the first 5 rows with
orders.head() # we can pass the number of rows we want to see into head()
```

bonus
for read_table
skiprows=None
skipfooter=None
this can be used if someone

we may not get perfectly ordered data

underlying data file was formatted perfectly to work with the "read_table" method default parameters
read_table assumes
1. your file is tab separated
2. the first row was a header row

### How do I select a pandas Series from a DataFrame?
There are 2 basic object types in pandas
1. Dataframe: table with columns and rows (A column in a data frame is a series)
2. Series:  you can hold a series separately without having a dataframe.

```python
import pandas as pd

ufo = pd.read_table('http://bit.ly/uforeports', sep=',') # the file we are reading is a csv comma separated file.
# the above line could be easily written as
ufo = pd.read_csv('http://bit.ly/uforeports')

type(ufo)
# output: pandas.core.frame.DataFrame

ufo['City'] # gives the column of the cities all records

type(ufo['City']) # note:  the column name we are passing here is case sensitive
# output: pandas.core.series.Series

# you can also use the dot notation. help: after dot some IDE will help with a tab or something
ufo.City

# if you need to access a series which has space in between say like "Colors Reported"
#or same as an attribute of dataframe, then
# you need to use bracket notation only
ufo['Colors Reported']

# you can concatenate 2 series with a simple + sign
ufo.City + ufo.State
# output:
#  0 IthacaNY
#  1 DevliND
#  ..... etc where IthacaNY is from Ithaca + NY

# to create a new column altoghether you need to use the bracket notation. Dot notation won't work
ufo.Location = ufo.City + ', ' ufo.State # this line won't work
ufo['Location'] = ufo.City + ', ' + ufo.State # this will work

```

### Why do some pandas commands end with parentheses, and other commands don't?

```python
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head() #has paranthesis return first 5 results

movies.describe()# again has paranthesis
# as long as there is at least one numeric column, it will show you descriptive statistics of all numeric columns

movies.shape # no parentheses

movies.dtypes # no paranthesis as it is an attribute, shows the data types of each columns
```

# Resources
1. read table: http://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.read_table.html
