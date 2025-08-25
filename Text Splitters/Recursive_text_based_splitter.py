# It is widely used text splitter which splits on the basis of separators like \n\n(paragraphs), \n(lines), " "(words)
# or ""(characters). Working Algo: One value called chunk_size is given(suppose 10 here) and the input is:

"""
Hello I am Priyanshu (20)
I am currently doing Btech (26)

I am living in Ghaziabad (24)
How are you (11)
"""
# Now the algo starts by checking the total characters of the inputs, if it is lower than chunk_size, then that input is
# a chunk, but if it is larger than the input is divided based on \n\n i.e. divided on the basis of para. Now the total
# character in each para are checked, if lower than the chunk_size, then are considered as chunks and if not, then again
# divided on the basis of \n i.e. divided on the basis of line. Now the total characters of each line are checked, if
# lower than good and if not then again it is divided on the basis of spaces i.e. words and if in this also, the
# chunk_size is smaller than total characters in words than at last no space i.e. characters. One thing is also there,
# if the no. of characters in the input gets too small from the chunk_size, then algo tries to recombine divided chunks
# to get the maximum length of chunks characters near to the chunk_size.

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to
exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to
advancements in technology here on Earth. Satellite communications, GPS, and even certain medical
imaging techniques trace their roots back to innovations driven by space programs.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)

result = text_splitter.split_text(text)

print(result)
print("Length =", len(result))
