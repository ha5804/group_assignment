import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rate.csv')
print("과거의 환율 변동을 통한 유익한 정보를 제공하는 프로그램입니다.\n" \
"조회하고 싶은 국가들중 미국을 포함한 5개의 국가를 입력하세요. :) \n" \
"입력형식은 희망하는 국가들을 쉼표(,)를 기준으로 작성해주세요! \n" 
"예시) 미국, 대한민국, 중국, 일본, 베트남")
print()

while True:
    user_input = input("입력: ").replace(' ','')
    user_input = user_input.split(',')
    for i in user_input:
        if i not in data["국가별"]:
            print("유호하지 않은 국가 입니다.\n 출력형식을 확인하거나 다시 입력해주세요!")
        else:
            print("입력한 국가가 유효합니다.\n")
    if len(user_input) == 5:
        break
    else:
        print("국가를 5개 입력해주세요")

    

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
x = data["국가별"]

user_country = [] #한그래프가 될 국가
for i in x:
    if (i in user_input):
        user_country.append(i)

rate_list = [] #y축에 들어갈 환율값
for i in user_input:
    rate = data[data["국가별"] == i]
    rate_list.append(rate)
# max_list = []
# for i in range(len(rate_list)):
#     max = 0
#     for j in range(10):
#         if (rate_list[i].iloc[0][j+1] >= max):
#             max = rate_list[i].iloc[0][j]
#     max_list.append(max)

# min_list = []
for i in range(len(rate_list)):
    a = rate_list[i].iloc[0][1:]
    print(a)
    
    



    
    
    

# while True:
#     print()
#     user_input2 = input("데이터 시각화를 희망하시면 yes, 아니면 no라고 입력하세요: ")
#     if user_input2 == "no":
#        break
#     elif user_input2 == "yes":
#         plt.figure(figsize = (10, 6))
#         plt.rc("font", family = "AppleGothic")
#         plt.plot(year, rate_list_norm[], label = user_country[0], color = 'red', marker = '.')
#         plt.plot(year, rate_list[1].iloc[0][1:], label = user_country[1], color = 'orange', marker = '.')
#         plt.plot(year, rate_list[2].iloc[0][1:], label = user_country[2], color = 'green', marker = '.')
#         plt.plot(year, rate_list[3].iloc[0][1:], label = user_country[3], color = 'blue', marker = '.')
#         plt.plot(year, rate_list[4].iloc[0][1:], label = user_country[4], color = 'purple', marker = '.')
#         plt.xlabel("year")
#         plt.ylabel("rate")
#         plt.legend(loc = "upper right")
#         plt.xticks(year, rotation = 45)
#         plt.grid(True, linestyle = ":")
#         plt.show()
#         break
#     else:
#         print("입력 형식을 다시 확인해주세요!")



            
            

        


        
        
    

