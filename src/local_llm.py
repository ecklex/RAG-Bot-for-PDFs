
import ollama

def ask_local_llm(context, question):
    prompt = f"""Du bist ein freundlicher und hilfsbereiter Assistent. Begrüße den Nutzer, beantworte die Frage basierend auf dem bereitgestellten Kontext und frage, ob die Antwort hilfreich war.

Kontext:
{context}

Frage:
{question}

Antwort:"""

    response = ollama.chat(
        model='mistral',  # oder 'nous-hermes', 'llama3'
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
