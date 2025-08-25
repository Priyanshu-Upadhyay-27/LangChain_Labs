from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings


"""from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)"""


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = ["Machine Learning is the field of training algorithms on specific pre-processed data.",
            "Antananarivo is the capital of Madagascar, which is also an animated movie.",
            "OpenAI is the pioneer company in the field of chat models like chatgpt.",
            "My favourite car is BMW and Rolls Royce.",
            "One hot encoder is used when preference of classifying data doesn't matter and vice versa for ordinal encoder in machine learning",
            "Autoencoders are used in deep learning to reduce the size of data"
            ]

query = "which is the pioneer company in chat models ?"

doc_embedding = embeddings.embed_documents(document)

query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(scores)) , key=lambda x:x[1])[-1]

print(index)
print("The Similarity Score is", score)
print("The Answer is below: \n", document[index])

