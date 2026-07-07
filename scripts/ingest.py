from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_FOLDER = Path("data")

documents = []

# Read every markdown file
for file in DATA_FOLDER.rglob("*.md"):

    text = file.read_text(encoding="utf-8")

    documents.append(
        Document(
            page_content=text,
            metadata={
                "source": file.name,
                "category": file.parent.name
            }
        )
    )

print(f"Loaded {len(documents)} documents.\n")

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.\n")

# Print chunks
for i, chunk in enumerate(chunks, start=1):

    print("=" * 60)
    print(f"Chunk {i}")

    print(chunk.metadata)

    print()

    print(chunk.page_content)

    print()