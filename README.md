# 🧠 URL Simplifier & Audio Narrator

This Python-based tool extracts content from any URL, simplifies it using Cohere's large language model (LLM), and optionally converts the summary into an audio narration (MP3). Ideal for quick understanding of complex articles and listening on the go.

---

## 🚀 Features

- 🌐 Fetches and parses raw text from a webpage
- 🧠 Simplifies the content using Cohere's `command` model
- 🔊 Converts simplified text to speech (MP3)
- 💾 Stores the summary and audio file in the `outputs/` folder

---

## 🛠 Tech Stack

- Python 3.8+
- Cohere API (https://cohere.com/)
- BeautifulSoup & Requests (for web scraping)
- gTTS or pyttsx3 (for text-to-speech)
- python-dotenv for environment variable management

---

## 📁 Folder Structure

.
├── main.py
├── .env
├── prompts/
│   └── simplify.txt
├── outputs/
│   ├── summary.txt
│   └── narration.mp3
├── utils/
│   ├── fetch_content.py
│   └── tts.py

---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/url-simplifier.git
cd url-simplifier

### 2. Install Dependencies

pip install -r requirements.txt

Make sure your `requirements.txt` includes:

cohere  
requests  
beautifulsoup4  
gtts  
python-dotenv

### 3. Add Your Cohere API Key

Create a `.env` file in the root directory:

COHERE_API_KEY=your_cohere_api_key_here

---

## ▶️ How to Use

1. Run the script:

python main.py

2. Paste a valid URL when prompted.  
3. The tool will extract and simplify the text.  
4. You'll be asked whether to generate audio narration.  
5. Results will be saved in the `outputs/` folder:
   - summary.txt — simplified text
   - narration.mp3 — optional audio file

---

## 📄 Example Prompt Template (`prompts/simplify.txt`)

Please simplify the following text for a general audience:

{input}

You can modify the prompt to adjust tone, reading level, or purpose.

---

## 🧠 Future Improvements

- [ ] Add support for PDFs and .txt files  
- [ ] Streamlit/Gradio web interface  
- [ ] Multiple TTS engine options  
- [ ] Language detection and translation

---

## 👨‍💻 Author

Siddhant Kaushik  
📧 siddhantintern@gmail.com  
🌐 https://github.com/siddhantcookie

---

## ⚠️ Disclaimer

This tool only uses publicly accessible content and is intended for personal, educational, or productivity use. Please respect content ownership and platform terms of service.
