from openai import OpenAI
import matplotlib.pyplot as plt

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
)


count_question = 0
user_count = 10

while True:
    user_q = input("환율에 관한 궁금한 점들을 물어보세요!\n""종료를 희망하시면 exit이라고 적어주세요: ")
    if(user_q.lower() == "exit"):
        break
    
    else:
       completion = client.chat.completions.create(
          model="meta-llama/llama-3.3-8b-instruct:free",
          messages=[{"role": "system","content": user_q}])
       count_question += 1
       user_count += 1
       print(completion.choices[0].message.content)

score_1 = []
score_2 = []
score_3 = []

x_label = ["spped", "accuracy", "clarity", "mean_score"]
print(f"{count_question}번의 질문에 대한 간단한 설문 부탁드립니다!\n""다음 질문에 대해서 1~10점 사이로 숫자만 작성해주세요.")

score_1.append(int(input("답변의 속도는 적당했나요?: ")))
score_2.append(int(input("질문에 대한 궁금증이 해결되었나요?: ")))
score_3.append(int(input("답변이 너무 어렵지 않았나요?: ")))
print("설문에 응해주셔서 감사합니다!")