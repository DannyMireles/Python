# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 9b - 3
# Date:         10/25/2019

#importing statistics
import pandas as pd
import statistics

weather_report=pd.read_csv('WeatherDataWindows(1).csv')
#create the max and min temp variables
max_temp = max(weather_report["Temp High"])
min_temp = min(weather_report["Temp Low"])
#output the maximum and minimum temperature seen over the 3 year period
print("The maximum and minimum temperatures seen over these three years are",max_temp,"and",min_temp)
print()
#calculating the average dailty precipitation
#make a variable for the total days and for the total percipitation
days_tot = weather_report.shape[0]
sum_precipitation = sum(weather_report["Precipitation (in.)"]
#make a value for the average precipitation
av_prec = sum_precipitation/days_tot
print("The average percipitation during this time period was",average_prec)
print()
#calculating the average high temp in July
days_july15 = 0
sum_high_temp = 0
month = 0
year = 0
if(month==7 and year==2015):
    sum_high_temp += weather_report['Temp High'][i]
    days_july15 += 1
av_high_july15 = sum_high_temp/days_july15
print("The average high temperature in July 2015 was",av_high_july15)
print()
#calculating the days where humidity was higher than 90
days_humidity_greater_than_90 = 0
for i in weather_report['Humidity Avg']:
if i>90:
    days_humidity_greater_than_90 += 1
print("The percentage of days where humidity was greater than 90 was",100*(days_humidity_greater_than_90/days_tot))
print()
#calculating the mean and standard deviation of precipitation levels
print("The mean and standard deviation of precipitation levels were",statistics.mean(weather_report["Precipitation (in.)"]),statistics.stdev(weather_report["Precipitation (in.)"]))


  