from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """You are an expert in Romanian laws
Here are some relevant informations: {infos}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("Introduceti o intrebare sau un subiect (press X to exit): ")
    print("\n\n_____________________________________ ")

    if question == "X" or question == "x":
        break

    result = chain.invoke({"infos ":[], "question": question})
    
    print(result)

