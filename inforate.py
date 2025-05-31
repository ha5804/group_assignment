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

for i in user_input:
    row = data[data[f"국가별"] == i]
    
    

# while True:
#     user_input2 = input("데이터 시각화를 희망하시면 yes, 아니면 no라고 입력하세요: ")
#     if user_input2 == "no":
#         False
#     elif user_input2 == "yes":
        
        
    

