# test_rag.py

from rag import answer_question

question = input("Ask a question: ")

answer, sources = answer_question(question)

print("\nANSWER:\n")
print(answer)

print("\nSOURCES:\n")

for source in sources:
    print(source)

