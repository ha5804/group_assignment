import matplotlib as plt
import pandas as pd
my_data = pd.read_csv("rate.csv")
x = my_data["국가별"]
print(x)