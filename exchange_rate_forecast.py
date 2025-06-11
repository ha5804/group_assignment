from openai import OpenAI
import matplotlib.pyplot as plt

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
)


count_question = 0
user_count = 10


completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},  
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "system",
      "content": 
    }
  ]
)
print(completion.choices[0].message.content)



completion.choices[0].message.content