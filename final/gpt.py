import requests
import json # 這有兩個方法 dumps (物件轉字串) 跟 loads (字串轉物件)
from pprint import pp # 為了印出來漂亮

openai_api_key = ''

def get_completion(messages, model="gpt-4", temperature=0, max_tokens=300):
    payload = { "model": model, "temperature": temperature, "messages": messages, "max_tokens": max_tokens }

    headers = { "Authorization": f'Bearer {openai_api_key}', "Content-Type": "application/json" }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers = headers, data = json.dumps(payload) )
    obj = json.loads(response.text)
    if response.status_code == 200 :
        return obj["choices"][0]["message"]["content"]
    else :
        return obj["error"]

def get_response():
    # 讀取文字檔
    text = ''
    with open('./result.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    print(f'錯誤文本: {text}')
    user_message = f"我会提供含有错字的文本，请帮我改成正确的文本，并告诉我错字在第几个字元，用提供的格式回传: 可能有错字的文本:{text} 格式:\n正确文本: ....\n错字: (以下为markdown语法)\n \
    | 位置 | 错字 | 正确字 |\n \
    | -------- | -------- | -------- |\n \
    | position | 错字 | 对字 |"

    messages = [
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = get_completion(messages, temperature=0)
    # print(response)
    with open('./wrong.txt', 'w', encoding='utf-8') as file:
        file.write(response)
    file.close()
