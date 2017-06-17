# Pandas python library

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

http://pandas.pydata.org/

### create a new DataFrame

```python
import pandas as pd

my_data_frame = pd.DataFrame(columns=['column1', 'column2', 'column3'])
# Add entry to DataFrame
my_data_frame.append({'column1': 'value1','column2': 'value2','column3': 'value3'})
```

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
1. DataFrame: table with columns and rows (A column in a data frame is a series)
2. Series:  you can hold a series separately without having a DataFrame.

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
# or same as an attribute of DataFrame, then
# you need to use bracket notation only
ufo['Colors Reported']

# you can concatenate 2 series with a simple + sign
ufo.City + ufo.State
# output:
#  0 IthacaNY
#  1 DevliND
#  ..... etc where IthacaNY is from Ithaca + NY

# to create a new column altogther you need to use the bracket notation. Dot notation won't work
ufo.Location = ufo.City + ', ' + ufo.State # this line won't work
ufo['Location'] = ufo.City + ', ' + ufo.State # this will work

```

### Few Attributes and methods of DataFrames

```python
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head() #has parenthesis return first 5 results

movies.describe()# again has parenthesis
# as long as there is at least one numeric column, it will show you descriptive statistics of all numeric columns

movies.shape # no parentheses, this method returns a tuple saying the rows, columns our dataframe has

movies.dtypes # no parenthesis as it is an attribute, shows the data types of each columns
```

### how to rename a column in a pandas Dataframe?

continuing with the above DataFrame
```python
ufo.columns # this is an attribute of the DataFrame, to see the columns

ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported', inplace=True})

## Second method
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols # this way you can update all column names at once

ufo.head() # see that the names would have changed

# now say you want to replace all the spaces with underscore '_'
ufo.columns = ufo.columns.str.replace(' ', '_')
ufo.columns # will output all the headers with _ instead of spaces

```

### how to remove columns from a pandas dataframe?

```python
import pandas as pd

ufo = read_csv('http://bit.ly/uforeports')

ufo.head() #see the first 5 records

ufo.shape # see shape, rows and columns

ufo.drop('Colors Reported', axis=1, inplace=True) #  axis 0 is the row axis, and axis 1 is column axis
# what it basically does is in the column(1) axis, drop mentioned column and we want this operation to occur inplace.

# to drop multiple column we need to pass the first argument as an array of column names
ufo.drop(['State', 'City'], axis=1, inplace=True)
# removes the above 2 columns
ufo.head() # check the data frame after the changes

#to delete the rows just use axis 0 instead of the 1 and also for first argument pass the labels
ufo.drop([0,1], axis=0, inplace=True) # this will delete the first 2 rows of the data frame.
```

# How to sort a pandas dataframe or series?

you can sort the values using the .sort_values() method

```python
# say movies is a dataframe with columns like 'title', 'rating' etc and you want to sort only the series say title

movies.title.sort_values()
# or
movies['title'].sort_values()

#to sort our entire dataframe based on a column
movies.sort_values('title')

# to sort based on multiple values

movies.sort_values(['title', 'duration'])

```

# how to filter rows of a pandas DataFrame by column values?

```python
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head()

# type of True/False will return bool. they are of boolean type

type(True)

booleans = []

for length in movies.duration:
  if length >= 200:
    boolean.append(True)
  else:
    boolean.append(False)

# this list of booleans tells us which movies is longer than 200 in duration
# now converting the python list into a series

is_long_movie = pd.Series(booleans)

# now if we pass the above true/false value to the DataFrame it uses it to filter out.
# we do this with the simple bracket notations

movies[is_long_movie] # this returns movies DataFrame with only those movies with duration greater than 200 mins

# Approach 2
is_long = movies.duration >= 200 # this returns entire series, eliminating the need for the for loop
is_long.head() ## show the first 5 values of the series as booleans
movies[is_long]

# the above could be done in a single line
movies[movies.duration >= 200]

```

# How do I apply multiple filter criteria to a pandas DataFrame?

```python
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')


```

## convert a JSON string to python various

``` python
##
import json

json_out = json.loads('{"cuz" : [[1,2,3,4],[1,2,3,4],[1,2,3,4]]}')
print(json_out["cuz"])

```


# Resources
1. read table: http://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.read_table.html
2. https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y Kevin Markham series on pandas.
3. https://github.com/justmarkham/pandas-videos
