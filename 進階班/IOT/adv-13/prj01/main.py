import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0.0)
from langchain_core.messages import HumanMessage

while True:
    ans = input("請輸入想跟AI說的話: ")
    print(
        model.invoke(
            [
                HumanMessage(
                    content="""
    開燈是'ON'，關燈是'OFF'
    開門是'open'，關門是'close'
    你是一個負責開燈跟關燈的管理員以及開車庫門跟關車庫門的管理員
    你只能根據使用者的回應來決定要回答'ON'或'OFF'以及'open'或'close'
    不能回答其他的字串
                """
                ),
                HumanMessage(content=ans),
            ]
        ).content
    )
