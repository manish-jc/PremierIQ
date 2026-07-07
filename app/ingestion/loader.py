from langchain_community.document_loaders import DirectoryLoader, TextLoader


class DocumentLoader:

    def __init__(self, data_path="data"):
        self.data_path = data_path

    def load_documents(self):

        loader = DirectoryLoader(
            self.data_path,
            glob="**/*.md",
            loader_cls=TextLoader
        )

        documents = loader.load()

        return documents