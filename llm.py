from openai import OpenAI
import requests
import json
from src.prompt import prompt_func

client = OpenAI(api_key="")

ninja_api_key = "2NygB48JuPFkfc/seQUvag==q0SyyvwM8BLi78bp"
body_parts=["abdominals","abductors","adductors","biceps","calves","chest","forearms","glutes","hamstrings","lats","lower_back",
        "middle_back","neck","quadriceps","traps","triceps"]


def ask_question(ninja_api_key,query,body_parts,model="gpt-3.5-turbo",temperature=0.1):
    api_url1 = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response1 = requests.get(api_url1, timeout=100, headers={'X-Api-Key': ninja_api_key})
    
    part = None
    for i in query.split():
        if i in body_parts:
            part = i
            
    api_url2 = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(part)
    response2 = requests.get(api_url2, timeout=100, headers={'X-Api-Key': ninja_api_key})
    
    res1 = json.loads(response1.text)
    res2 = json.loads(response2.text)

    prompt_mod = prompt_func(res1+res2,query)
    
    messages = [
        {"role":"system","content":prompt_mod}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,

    )

    return response.choices[0].message.content,messages
