from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt | model


def chat():
    context = ""
    print("Welcome to AI chatbot! Type exist to end Chat")

    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context,"question":user_input})
        print(result)
        context += f"\nUser: {user_input} \n AI:{result}"

if __name__ == '__main__':
    chat()