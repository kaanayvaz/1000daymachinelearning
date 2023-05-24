import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
    with open(filename, "r") as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_prices(dates,prices):
    dates = np.reshape(dates, (len(dates), 1))
    svr_len = SVR(kernel= "linear", C=1e3)
    #svr_poly = SVR(kernel= "poly", C=1e3, degree=2)
    svr_rbf = SVR(kernel= "rbf", C=1e3, gamma=0.1)
    svr_len.fit(dates, prices)
    #svr_poly.fit(dates, prices) #it did not work I did not understand why
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color = "black", label = "Data")
    plt.plot(dates, svr_rbf.predict(dates), color = "red", label = "RBF model")
    plt.plot(dates, svr_len.predict(dates), color = "green", label = "Linear model")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Support Vector Regression")

    plt.legend()
    plt.show()

get_data("AAPL.CSV")

predict_prices(dates,prices)






