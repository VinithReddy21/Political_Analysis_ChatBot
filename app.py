import praw
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime
from transformers import pipeline

nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Load Reddit API (update with your actual credentials)
# Reddit API Setup (Replace with your credentials)
reddit = praw.Reddit(
    client_id="KATdqJrEoBC_KvjG1qEWSg",
    client_secret="HUCwtBpmkYle5K-O-_LXwPeMX0e2nA",
    username="EntrepreneurSea2025",
    password="vinith2158vin",
    user_agent="CyberpunkAnalyzer by  u/EntrepreneurSea2025"
)

# Load LLM chatbot (summarizer + question answering)
from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, framework="pt")

qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    framework="pt"  # Force PyTorch backend
)

# Function to fetch posts
def fetch_reddit_posts(query, limit=100):
    posts = []
    for submission in reddit.subreddit("all").search(query, limit=limit):
        posts.append({
            "title": submission.title,
            "score": submission.score,
            "url": submission.url,
            "created": datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d'),
            "comments": submission.num_comments
        })
    return pd.DataFrame(posts)

# Sentiment Analysis
def analyze_sentiment(df):
    df['sentiment'] = df['title'].apply(lambda title: sia.polarity_scores(title)['compound'])
    df['label'] = df['sentiment'].apply(lambda score: 'Positive' if score > 0.1 else ('Negative' if score < -0.1 else 'Neutral'))
    return df

# Chatbot Answer Generator
def chatbot_answer(context, question):
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
    response = qa_pipeline(prompt, max_length=100, do_sample=False)
    return response[0]['generated_text']

# UI
st.set_page_config(page_title="Cyberpunk Reddit Sentiment Analyzer", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: black;
        color: #00ffcc;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #ff0055;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Cyberpunk Reddit Sentiment Analyzer")
st.write("Search Reddit posts, visualize sentiment, and prepare for deeper AI-driven insights.")

query = st.text_input("🔎 Enter your topic or keyword:", "Politics in Kerala")
limit = st.slider("Number of posts to fetch:", 10, 200, 100)

if st.button("Analyze Reddit Sentiment"):
    with st.spinner("Fetching posts..."):
        df = fetch_reddit_posts(query, limit)
        df = analyze_sentiment(df)

        st.subheader("📊 Sentiment Distribution")
        st.bar_chart(df['label'].value_counts())

        st.subheader("📰 Sample Posts")
        st.dataframe(df[['title', 'label', 'score', 'comments']].head(10))

        with st.expander("📃 Show Raw Data"):
            st.write(df)

        summary_text = " ".join(df['title'].tolist())[:3000]
        summary = summarizer(summary_text, max_length=200, min_length=50, do_sample=False)

        st.subheader("🧠 Summary of Reddit Discussions")
        st.write(summary[0]['summary_text'])

        st.subheader("🤖 Ask AI about the topic")
        user_question = st.text_input("Type your question for the AI (e.g., Who might win the Kerala elections?)")
        if user_question:
            ai_response = chatbot_answer(summary[0]['summary_text'], user_question)
            st.success(ai_response)

st.markdown("---")
st.caption("Made with ⚡ by B Sai Vinith Reddy")
