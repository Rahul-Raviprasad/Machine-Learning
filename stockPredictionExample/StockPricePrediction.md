
## Steps
1. Install dependencies
2. Collect datasets
3. Run scripts
4. graph the results

## Step1 : Install the dependencies
Installing scikit-learn
http://scikit-learn.org/stable/install.html
```
pip3 install csv
pip3 install numpy
pip3 install scikit-learn
pip3 install matplotlib
```


## Step 2 : you can collect price data from google finance and other sites

## Step 3 : Script

```python
import csv
import numpy as np
from sklearn.svm import SVR
import matplot.pyplot as plt

# plt.switch_backend('tk')

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
      csvFileReader = csv.reader(csvfile)
      next(csvFileReader) # we are calling the next method to skip the first row in our data since it is only column name
      for row in csvFileReader:
        dates.append(int(row[0].split('-')[0])) # to get the day say 27-03-2017 then this would give us 27
        prices.append(float(row[1]))
    return

def predict_prices(dates, prices, x):
  dates = np.reshape(dates, (len(dates)), 1) # 1 is the order of the elements

  #kernel here tells the type of SVM, C is scientific notation for 1000
  # there is on gaurantee a particular model would do better than the other so trying on both.
  svr_lin = SVR(kernal='linear', C=1e3)
  svr_lin.fit(dates, prices)

  svr_poly = SVR(kernal='poly', C=1e3, degree=2)
  svr_poly.fit(dates, prices)

  svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1) # radio bases function : eucladian distance between two inputs
  svr_rbf.fit(dates, prices)

  plt.scatter(dates, prices, color='black', label='Data')
  plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
  plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
  plt.plot(dates, svr_ploy.predict(dates), color='blue', label='Polynomial model')

  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.title('Support vector Regression')
  plt.legend()
  plt.show()

  return svr_rbf.predict(x)[0],svr_lin.predict(x)[0], svr_poly.predict(x)][0]

get_data('aapl.csv')

predicted_price = predict_price(dates, prices, 29)

print(predicted_price)


```
