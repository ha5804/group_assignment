import matplotlib.pyplot as plt
import pandas as pd
my_data = pd.read_csv("rate.csv")
x = my_data["국가별"]
user_input = input().replace(' ','')
user_input = user_input.split(',')

contry = []
for i in x:
    if (i in user_input):
        contry.append(i)
x_list = []
for i in user_input:
    year = my_data[my_data["국가별"] == i]
    x_list.append(year)
print(x_list)
print(contry)
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
plt.figure(figsize = (10, 6))
plt.plot(year, x_list[0].iloc[0][1:])
plt.plot(year, x_list[1].iloc[0][1:])
plt.show()