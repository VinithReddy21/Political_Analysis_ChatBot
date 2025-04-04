# 🧠 Cyberpunk Reddit Sentiment Analyzer

An AI-powered Streamlit app that fetches real-time Reddit posts, analyzes political sentiment using VADER, summarizes key discussions, and answers your political questions using powerful transformer models like BART and FLAN-T5.

---

## 🚀 Features

- 🔍 Search Reddit for any political or social topic  
- 📊 Analyze sentiment (Positive, Negative, Neutral) of Reddit post titles  
- 🧠 Get a summarized version of the discussions  
- 🤖 Ask an AI chatbot political questions based on Reddit insights  
- 🌐 Covers national, international, and local topics  

---

## 🔧 Tech Stack

- **Frontend:** Streamlit  
- **Reddit API:** PRAW (Python Reddit API Wrapper)  
- **Sentiment Analysis:** NLTK's VADER  
- **Summarization:** `facebook/bart-large-cnn`  
- **Question Answering:** `google/flan-t5-base`  
- **Visualization & Data:** pandas, matplotlib  

---

## 📦 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/cyberpunk-reddit-analyzer.git
cd cyberpunk-reddit-analyzer
2. Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4. Download NLTK VADER Lexicon:
This will happen automatically on the first run, or you can run it manually:

python
Copy
Edit
import nltk
nltk.download('vader_lexicon')
🗝️ Set Up Reddit API
Go to the Reddit Developer Portal

Create a new application (choose "script")

Note your:

client_id

client_secret

username

password

Replace the placeholders in your code in this section:

python
Copy
Edit
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_username",
    password="your_password",
    user_agent="YourAppName by u/YourUsername"
)
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
🧪 Example Use Cases
You can search for topics like:

"Politics in Kerala"

"Upcoming US elections"

"Russia Ukraine conflict"

"Local elections in Hyderabad"

Ask the chatbot questions like:

Who is predicted to win the Kerala elections?

What is the sentiment around Biden's presidency?

Are people supporting the latest policy update in Europe?

📌 Notes
🔐 Make sure your Reddit API credentials are kept secure and not shared publicly.

💡 This app can be extended to include:

Upcoming election dates & polling stations

Live political news using public news APIs

Location-aware election insights

📸 UI Preview
Streamlit UI with dark cyberpunk styling

Sentiment distribution charts

Reddit post table with sentiment labels

AI-powered Q&A and topic summaries

📄 License
MIT License

✨ Author
Made with ⚡ by B Sai Vinith Reddy

yaml
Copy
Edit
