# It works on the division of input text on the basis of semantic meaning of the text provided. Suppose two topics are
# covered in a single paragraph, then we will not be able to split them based on there particular topics for feeding to
# the LLM So we use Semantic text splitter where embeddings of the input is generated and cosine similarity is calculated
# between each line of text. When there is a sudden drop in the similarity, then it shows the meaning of the sentence gets changed
# and new topic is started. This is how, chunks are divided.

from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next
season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier
League (IPL) is the biggest cricket league in the world. People all over the world watch the
matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in
cities and villages. When such attacks happen, they leave behind pain and sadness. To fight
terrorism, we need strong laws, alert security forces, and support from people who care
about peace and safety.
"""

splitter = SemanticChunker(
    GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.3
)

chunks = splitter.create_documents([docs])
content = [doc.page_content for doc in chunks]
print("Length=", len(chunks))
print(content)


