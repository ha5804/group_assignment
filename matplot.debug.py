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

def my_plot(year , rate_list , user_country, len_user_input):
    color_list = ["red", "orange", "green", "blue", "purple", "pink", "gray", "brown", "gray", "gold", "silver", "cyan", "navy"]
    while True:
        print()
        user_input2 = input("데이터 시각화를 희망하시면 yes, 아니면 no라고 입력하세요: ")
        if user_input2 == "no":
            break
        elif user_input2 == "yes":
            for i in range(len_user_input):
                plt.plot(year, rate_list[i].iloc[0][1:], label = user_country[0], color = color_list[i], marker = '.')
