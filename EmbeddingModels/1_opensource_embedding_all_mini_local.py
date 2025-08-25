from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

document = ["Machine Learning is the field of training algorithms on specific pre-processed data.",
            "Antananarivo is the capital of Madagascar, which is also an animated movie.",
            "OpenAI is the pioneer company in the field of chat models like chatgpt.",
            "My favourite car is BMW and Rolls Royce.",
            "One hot encoder is used when preference of classifying data doesn't matter and vice versa for ordinal encoder"]

result = embedding.embed_documents(document)

print(str(result))