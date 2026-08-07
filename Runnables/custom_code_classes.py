from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass

###############################################################################
class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_data):
        # Acts like LangChain's .format()
        return self.template.format(**input_data)


class NakliLLM(Runnable):
    def __init__(self):
        print("LLM Created")
        self.response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

    def invoke(self, input_data):
        # Acts like LangChain's .predict()
        # Randomly picks a response to simulate AI generation
        response = random.choice(self.response_list)
        return {"response": response}


class NakliStrOutputParser(Runnable):
    def invoke(self, input_data):
        # Extracts just the string from the LLM's dictionary output
        return input_data["response"]

########################################################################################################


class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        # Loop through all runnables in the chain
        for runnable in self.runnable_list:
            # The output of the current runnable becomes the input for the next
            input_data = runnable.invoke(input_data)

        # Return the output of the final step
        return input_data

##########################################################################################################
# 1. Initialize components
template = NakliPromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)
llm = NakliLLM()
parser = NakliStrOutputParser()

# 2. Connect components using the Connector
chain = RunnableConnector([template, llm, parser])

# 3. Invoke the chain!
result = chain.invoke({
    "length": "short",
    "topic": "India"
})

print(result)