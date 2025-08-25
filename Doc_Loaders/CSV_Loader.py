from langchain_community.document_loaders import CSVLoader
# Here every row in csv file is converted into a langchain document object which can be later used with langchain
# components.

loader = CSVLoader(file_path="Iris.csv")

result = loader.load()

print(result[0])