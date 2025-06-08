import matplotlib as plt
import pandas as pd
my_data = pd.read_csv("rate.csv")
x = my_data["국가별"]
user_input = input().replace(' ','')
user_input = user_input.split(',')

for i in x:
    if (i in user_input):
        print(i)