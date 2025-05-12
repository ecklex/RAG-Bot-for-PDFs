import gradio as gr
from src.rag_pipeline import run_rag

def answer_question(message, history):
    folder_path = "data"
    if not message.strip():
        return "Bitte gib eine Frage ein."
    return run_rag(folder_path, message)

chat = gr.ChatInterface(
    fn=answer_question,
    chatbot=gr.Chatbot(type="messages", line_breaks=True, elem_classes="chatbot-container"),
    title="📚 Carla enhanced",
    description="Stelle eine Frage. Der Bot zeigt dir relevante Textstellen mit Seitenzahl.",
    submit_btn="Frage stellen",
    theme="soft"
)

if __name__ == "__main__":
    chat.launch(share=False)
