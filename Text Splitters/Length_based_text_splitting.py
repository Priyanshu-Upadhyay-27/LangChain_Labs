# It is a length based splitter which splits the text into chunks on the basis of length of characters or tokens
# provided. It is fast but strict which leads to splitting of text by avoiding the linguistics measures.
# Ex: missi and ng

from langchain.text_splitter import CharacterTextSplitter
text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to
exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to
advancements in technology here on Earth. Satellite communications, GPS, and even certain medical
imaging techniques trace their roots back to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0 ,# here, 0 characters will be overlap between 2 chunks.For 100 chunk size: 10-20 overlap is required
    separator=''
)
result = splitter.split_text(text)
print(result) # It will be a list of chunk
