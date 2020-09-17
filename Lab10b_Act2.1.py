# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 10b - 2
# Date:         11/04/2019

#Found Panda Online. Import libraries to help
import matplotlib.pyplot as plt
import pandas as pd

#read the csv file in
w = pd.read_csv("WeatherDataWindows(1).csv",delimiter = ",")

#create a date column from the textual column
w["Date1"] = pd.to_datetime(w["Date"],infer_datetime_format = True)

#create an axis for the plot
ax = plt.gca()

#plot two lines on the same graph
w.plot(kind = "line",x = "Date", y = "Pressure Avg", color = "green",ax=ax)
w.plot(kind = "line",x = "Date", y = "Temp Avg", ax=ax)
plt.show()

# plothistogram from the percipitation value
w[["Precipitation (in.)"]].plot(kind="hist",rwidth = 0.6,bins = 12)
plt.ylabel("Number of Days", fontsize = 12)
plt.show()

#Create a scatterplot indicating the relationship between average temperature and average dew
w.plot(kind = "scatter",x = "Temp Avg",y = "Dew Point Avg",color = "purple")
plt.xlabel("Average Dew Point", fontsize = 12)
plt.ylabel("Average Temperature", fontsize = 12)
plt.show()

#Create a bar chart, with one bar per month, showing the average temperature along with error bars indicating the high and low temperatures from that month
w_grouped = w.groupby(w["Date1"].dt.strftime("%B"))["Temp High","Temp Avg","Temp Low"].sum()
w_grouped.plot(kind = "bar")
plt.show()

