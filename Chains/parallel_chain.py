from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

text = """1.4. Support Vector Machines
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It tries to find the best boundary known as hyperplane that separates different classes in the data. It is useful when you want to do binary classification like spam vs. not spam or cat vs. dog.

The main goal of SVM is to maximize the margin between the two classes. The larger the margin the better the model performs on new and unseen data.


Key Concepts of Support Vector Machine
Hyperplane: A decision boundary separating different classes in feature space and is represented by the equation wx + b = 0 in linear classification.
Support Vectors: The closest data points to the hyperplane, crucial for determining the hyperplane and margin in SVM.
Margin: The distance between the hyperplane and the support vectors. SVM aims to maximize this margin for better classification performance.
Kernel: A function that maps data to a higher-dimensional space enabling SVM to handle non-linearly separable data.
Hard Margin: A maximum-margin hyperplane that perfectly separates the data without misclassifications.
Soft Margin: Allows some misclassifications by introducing slack variables, balancing margin maximization and misclassification penalties when data is not perfectly separable.
C: A regularization term balancing margin maximization and misclassification penalties. A higher C value forces stricter penalty for misclassifications.
Hinge Loss: A loss function penalizing misclassified points or margin violations and is combined with regularization in SVM.
Dual Problem: Involves solving for Lagrange multipliers associated with support vectors, facilitating the kernel trick and efficient computation.
How does Support Vector Machine Algorithm Work?
The key idea behind the SVM algorithm is to find the hyperplane that best separates two classes by maximizing the margin between them. This margin is the distance from the hyperplane to the nearest data points (support vectors) on each side.

Multiple hyperplanes separating the data from two classes
Multiple hyperplanes separate the data from two classes
The best hyperplane also known as the "hard margin" is the one that maximizes the distance between the hyperplane and the nearest data points from both classes. This ensures a clear separation between the classes. So from the above figure, we choose L2 as hard margin. Let's consider a scenario like shown below:

Selecting hyperplane for data with outlier
Selecting hyperplane for data with outlier
Here, we have one blue ball in the boundary of the red ball.
"""


load_dotenv()

#Note Generation Task
gem_model_1 = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
prompt1 = PromptTemplate(
    template="Generate short and simple notes for the following text :\n {text}",
    input_variables=["text"]
)

#Quiz Generation Task
hug_model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-30B-A3B",
    task="text-generation",
    )
hug_model_2 = ChatHuggingFace(llm=hug_model)
prompt2 = PromptTemplate(
    template="""Assume yourself as a teacher for the following notes provided : \n {text} \n Now, Generate a 5 question
    quiz which covers fundamental to advance""",
    input_variables=["text"]
)

# Merging into a single document
oll_model_3 = ChatOllama(model="mistral")
prompt3 = PromptTemplate(
        template="""You are a document combiner. Your ONLY job is to combine two sections without changing their content.
    
    CRITICAL INSTRUCTIONS:
    - DO NOT summarize, shorten, or modify the content in any way
    - DO NOT rewrite or rephrase anything
    - Simply combine the sections with proper headings
    - Keep ALL original formatting, bullet points, and details EXACTLY as provided
    
    NOTES SECTION (copy exactly as-is):
    {notes}
    
    QUIZ SECTION (copy exactly as-is):
    {quiz}
    
    Your response should be:
    ## ----------------------------------------------NOTES--------------------------------------------
    [exact copy of notes section above]
    
    ## ----------------------------------------------QUIZ---------------------------------------------
    [exact copy of quiz section above]
    
    Remember: DO NOT modify, summarize, or change anything. Just copy and format.""",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()
# now we will be using runnable parallel to create notes and quiz in a parallel manner and generating them will be part one
# and merging them will be part 2

parallel_chain = RunnableParallel({
    "notes": prompt1 | gem_model_1 | parser,
    "quiz": prompt2 | hug_model_2 | parser
})

print("---------------------Intermediate_output : Dictionary with keys: notes and quiz------------")
intermediate = parallel_chain.invoke({"text": text})
print("Generation:\n", intermediate)
print("---------------------------------End of the dictionary-----------------------------------")

merge_chain = prompt3 | oll_model_3 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"text": text})

print(result)

# Print the graph structure
print("\n=== Chain Graph Structure ===")
try:
    chain.get_graph().print_ascii()
except Exception as e:
    print(f"Graph visualization error: {e}")


