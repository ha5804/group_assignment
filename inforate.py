import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rate.csv')
print("과거의 환율 변동을 통한 유익한 정보를 제공하는 프로그램입니다.\n" \
"조회하고 싶은 국가들중 미국을 포함한 5개의 국가를 입력하세요. :) \n" \
"입력형식은 희망하는 국가들을 쉼표(,)를 기준으로 작성해주세요! \n" 
"예시) 미국, 대한민국, 중국, 일본, 베트남")


user_input = input("입력: ").replace(' ','')
user_input = user_input.split(',')
#print(user_input)

rate_dic = {}
for i in user_input:
    row = data[data[f"국가별"] == i]
    key = row.iloc[0, 0]
    val = row.iloc[0, 1:]
    rate_dic[key] = [i for i in val.values]

country = []
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
rate = []

for k , v in rate_dic.items():
    rate.append(v)
    country.append(k)
print(country)
print(rate)
print(year)
rate_1 = rate[0]
rate_2 = rate[1]
rate_3 = rate[2]
rate_4 = rate[3]
rate_5 = rate[4]
print(rate_1)
print(rate_2)
print(rate_3)
print(rate_4)
print(rate_5)


while True:
    user_input2 = input("데이터 시각화를 희망하시면 yes, 아니면 no라고 입력하세요: ")
    if user_input2 == "no":
       False
    elif user_input2 == "yes":
        fig, ax = plt.subplots()
        ax.set_title("국가별 10년 환율", fontsize = 8)
        ax.set_xlabel("YEAR", fontsize = 8)
        ax.set_ylabel("RATE", fontsize = 8)
        ax.plot(year, rate_1, color = 'red', label = country[0], marker = '.')
        ax.plot(year, rate_2, color = 'blue', label = country[1], marker = '.')
        ax.plot(year, rate_3, color = 'green', label = country[2], marker = '.')
        ax.plot(year, rate_4, color = 'yellow', label = country[3], marker = '.')
        ax.plot(year, rate_5, color = 'orange', label = country[4], marker = '.')
        ax.tick_params("x", labelsize = 7)
        ax.tick_params("y", labelsize = 7)
        ax.set_xticks(year)
        ax.set_yticks(False)
        plt.legend()
        plt.show()
        break


            
            

        


        
        
    

