import matplotlib.pyplot as plt
import pandas as pd
my_data = pd.read_csv("rate.csv")
user_input = input().replace(' ','')
user_input = user_input.split(',')
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
x = my_data["국가별"]

user_country = [] #한그래프가 될 국가
for i in x:
    if (i in user_input):
        user_country.append(i)

rate_list = [] #y축에 들어갈 환율값
for i in user_input:
    rate = my_data[my_data["국가별"] == i]
    rate_list.append(rate)

plt.rc("font", family = "AppleGothic")
plt.plot(year, rate_list[0].iloc[0][1:], label = user_country[0], color = 'blue', marker = '.')
plt.plot(year, rate_list[1].iloc[0][1:], label = user_country[1], color = 'red', marker = '.')
plt.plot(year, rate_list[2].iloc[0][1:], label = user_country[2], color = 'green', marker = '.')
plt.plot(year, rate_list[3].iloc[0][1:], label = user_country[3], color = 'orange', marker = '.')
plt.plot(year, rate_list[4].iloc[0][1:], label = user_country[4], color = 'yellow', marker = '.')
plt.show()
