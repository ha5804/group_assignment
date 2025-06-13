import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI

data = pd.read_csv("rate.csv")
#pandas로 환율 데이터 읽기
print("과거의 환율 변동을 통한 유익한 정보를 제공하는 프로그램입니다.\n" \
"조회하고 싶은 국가들중 미국을 포함한 국가들을 입력하세요. :) \n" \
"입력형식은 희망하는 국가들을 쉼표(,)를 기준으로 작성해주세요! \n" 
"예시) 미국, 대한민국, 중국, 일본, 베트남")
print()

#my_plot함수를 따로 지정해서, 
# 입력한 국가 수를 인자로 받아 유동적으로 plot할 수 있도록 설정
def my_plot(year , rate_list , user_country, len_user_input):
    color_list = ["red", "orange", "green", "blue", "purple", "pink", "gray", "brown", "gray", "gold", "silver", "cyan", "navy"]
    while True:
        print()
        user_input2 = input("데이터 시각화를 희망하시면 yes, 아니면 no라고 입력하세요: ")
        if user_input2 == "no":
            break
        elif user_input2 == "yes":
            # label = []
            # rate_list_plt = []
            plt.figure(figsize = (10, 6))
            plt.rc("font", family = "DejaVu Sans")
            for i in range(len_user_input):
                plt.plot(year, rate_list[i].iloc[0][1:], label = user_country[i], color = color_list[i], marker = '.')
            plt.xlabel("year")
            plt.ylabel("rate")
            plt.yscale('log')
            plt.legend(loc = "upper right")
            plt.xticks(year, rotation = 45)
            plt.grid(True, linestyle = ":")
            plt.show()
            break
        else:
            print("입력 형식은 yes , no 입니다. 다시 입력해주세요!")
            print()

#while문을 통해 반복적으로 국가 입력 받기. + 예외처리
while True:
    user_input = input("입력: ").replace(' ','')
    user_input = user_input.split(',')
    for i in user_input:
        if i not in data["국가별"].values:
            print("유효하지 않은 국가 입니다.\n출력형식을 확인하거나 다시 입력해주세요!")
            break
    else:
        break

#csv의 데이터 plot 편의성 위해 미리 year 리스트 작성
year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
x = data["국가별"] #x값을 국가로 설정

user_country = [] #한그래프가 될 국가
for i in x:
    if (i in user_input):
        user_country.append(i)

rate_list = [] #y축에 들어갈 환율값
for i in user_input:
    rate = data[data["국가별"] == i]
    rate_list.append(rate)

#========================call plot function=======================
my_plot(year, rate_list, user_country, len(user_input))

#========================run LLM======================
print("\n\n\n============================================"
      "\n방금 보신 자료에 대한 궁금중을 풀어드립니다!"
      "\n--ex)미국의 환율은 왜 1이야? 한국어로 간단하게 답변해줘--"
      "\n위 양식으로 질문하시면 좀더 빠르고 정확한 답변이 가능합니다 :)")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


count_question = 0
user_count = 10

while True:
    user_q = input("\n환율에 관한 궁금한 점들을 물어보세요!\n""종료를 희망하시면 exit이라고 적어주세요: ")
    if(user_q.lower() == "exit"):
        break
    
    else:
       completion = client.chat.completions.create(
          model="meta-llama/llama-3.3-8b-instruct:free",
          messages=[{"role": "system","content": user_q}])
       #반복 질문할때마다 count 추가하기
       count_question += 1 
       user_count += 1
       print(completion.choices[0].message.content)

#plot시각화 위해 예시 스코어 리스트 준비해놓기
score_1 = [10, 8 ,9 ,10, 7 ,8 ,4 , 6, 8, 7]
score_2 = [8, 8 ,5 ,10, 7 ,7 ,4 , 9, 9, 7]
score_3 = [9, 9 ,1 ,7, 10 ,2 ,5 , 3, 8, 9]

x_label = ["spped", "accuracy", "clarity", "mean_score"]
print(f"\n{count_question}번의 질문에 대한 간단한 설문 부탁드립니다!\n""다음 질문에 대해서 1~10점 사이로 숫자만 작성해주세요.")

s_1 = int(input("\n답변의 속도는 적당했나요?: "))
score_1.append(s_1)
print(f"입력 점수 : {s_1}")
s_2 = int(input("\n질문에 대한 궁금증이 해결되었나요?: "))
score_2.append(s_2)
print(f"입력점수: {s_2}")
s_3 = int(input("\n답변이 너무 어렵지 않았나요?: "))
score_3.append(s_3)
print(f"입력점수: {s_3}")
print("\n설문에 응해주셔서 감사합니다!")

total_score = sum(score_1 + score_2 + score_3)
mean_score = total_score / (3 * len(score_1))
y_score = [sum(score_1) / user_count, sum(score_2)/ user_count, sum(score_3)/ user_count, mean_score]

plt.figure(figsize=(10,6))
plt.bar(x_label, y_score, color='skyblue', edgecolor = 'black')
plt.title("Our Program Score From Evaluate")
plt.xticks(x_label)
plt.grid(True, linestyle = ':')
plt.show()