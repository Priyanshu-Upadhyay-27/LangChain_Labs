from langchain_community.chat_models import ChatOllama

model = ChatOllama(model = "mistral",
                   model_kwargs={"temperature": 0.7,
                                 "num_predict": 10}
                   )  # With open AI and other models, temperature attribute ranging from 0-2 yield creative output in increasing order

result = model.invoke("Write a poem on the topic, 'Rain' ")

print(result)