from app.services.rag_service import split_text

sample_text = """
Artificial Intelligence is transforming the world.
Machine learning enables systems to learn patterns.
Deep learning uses neural networks.
""" * 100

chunks = split_text(sample_text)

print(len(chunks))
print(chunks[0])