import chainlit as cl
from src.llm import ask_question

ninja_api_key = "2NygB48JuPFkfc/seQUvag==q0SyyvwM8BLi78bp"
body_parts=["abdominals","abductors","adductors","biceps","calves","chest","forearms","glutes","hamstrings","lats","lower_back",
        "middle_back","neck","quadriceps","traps","triceps"]


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    
    response,messages = ask_question(ninja_api_key,message.content,body_parts)
    messages.append({"role":"user","content":message.content})
    messages.append({"role":"assistant","content":response})
    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()
