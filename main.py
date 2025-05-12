# Die main.py wird nur verwendet, wenn man das RAG über die Konsole verwenden möchte.

from src.rag_pipeline import run_rag

if __name__ == "__main__":
    folder_path = "data"
    print("RAG-Bot für mehrere PDFs – Frage stellen oder 'exit' tippen.")

    while True:
        question = input("\n❓ Deine Frage: ")
        if question.lower() in ["exit", "quit"]:
            break

        response = run_rag(folder_path, question)
        print("\n💬 Antwort:\n")
        print(response)
