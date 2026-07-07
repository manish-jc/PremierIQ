from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )

    def split(self, documents):

        return self.splitter.split_documents(documents)