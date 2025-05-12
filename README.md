# RAG (Retrieval-Augmented Generation) Bot for PDFs

Dieses Projekt implementiert einen lokalen Retrieval-Augmented Generation (RAG) Bot, der Fragen zu mehreren PDF-Dokumenten beantworten kann. Der Bot kombiniert die Extraktion von Text aus PDFs, die Erstellung von Embeddings, die Indexierung mit FAISS und die Generierung von Antworten mithilfe eines lokalen LLM (Large Language Model). Die Daten werden nicht nach außen gegeben.

---

## 📋 Inhaltsverzeichnis

- [RAG (Retrieval-Augmented Generation) Bot for PDFs](#rag-retrieval-augmented-generation-bot-for-pdfs)
  - [📋 Inhaltsverzeichnis](#-inhaltsverzeichnis)
  - [✨ Features](#-features)
  - [🛠 Voraussetzungen](#-voraussetzungen)
  - [🚀 Installation](#-installation)
  - [Projektstruktur](#projektstruktur)
  - [🛠 Technologien](#-technologien)
  - [📜 Lizenz](#-lizenz)

---

## ✨ Features

- **PDF-Verarbeitung**: Extrahiert Text aus PDF-Dokumenten und verarbeitet Metadaten wie Titel und Autor.
- **Text-Chunks**: Zerlegt den Text in kleinere, verarbeitbare Abschnitte.
- **Embeddings**: Erstellt Embeddings für Text-Chunks mithilfe von SentenceTransformers.
- **FAISS-Indexierung**: Nutzt FAISS, um schnelle und effiziente Ähnlichkeitssuchen durchzuführen.
- **Antwortgenerierung**: Verwendet ein lokales LLM (z. B. Mistral oder Nous-Hermes), um Antworten basierend auf den relevanten Textstellen zu generieren.
- **Web-Interface**: Ein benutzerfreundliches Interface mit Gradio.
- **Konsolenmodus**: Alternativ kann der Bot direkt über die Konsole verwendet werden.

---

## 🛠 Voraussetzungen

- Python 3.8 oder höher
- Pip (Python-Paketmanager)

---

## 🚀 Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/dein-benutzername/rag-bot.git
   cd rag-bot

2. **Abhängigkeiten installieren:** Stelle sicher, dass alle notwendigen Pakete installiert sind:
    ````
    pip install -r requirements.txt
    ````

## 🖥 Verwendung
### Web-Interface
Starte das Web-Interface mit Gradio:
````
python web_ui.py
````
Das Interface wird lokal bereitgestellt. Hier kannst du Fragen stellen, und der Bot zeigt dir relevante Textstellen aus den PDFs an.

### Konsolenmodus
Starte den Bot im Konsolenmodus:
````
python main.py
````
Gib deine Frage ein, und der Bot liefert dir eine Antwort. Beende den Modus mit ```control+c```.

## Projektstruktur
```
RAG/
├── data/                          # Ordner für PDF-Dateien
├── requirements.txt               # Abhängigkeiten
├── main.py                        # Konsolenmodus
├── web_ui.py                      # Web-Interface
├── src/                           # Quellcode
│   ├── extract_pdf.py             # Extrahiert Text aus PDFs
│   ├── chunker.py                 # Zerlegt Text in Chunks
│   ├── embedder.py                # Erstellt Embeddings
│   ├── indexer.py                 # FAISS-Indexierung
│   ├── local_llm.py               # Lokales LLM für Antwortgenerierung
│   ├── rag_pipeline.py            # Hauptpipeline für RAG
└── README.md                      # Dokumentation
```
## 🛠 Technologien
* [FAISS](https://github.com/facebookresearch/faiss): Für effiziente Ähnlichkeitssuche.
* [SentenceTransformers](https://www.sbert.net): Für die Erstellung von Embeddings.
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/): Für die PDF-Verarbeitung.
* [Gradio](https://www.gradio.app): Für das Web-Interface.
* [Ollama](https://ollama.com): Für die lokale LLM-Integration.

## 📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei LICENSE.
