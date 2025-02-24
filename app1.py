import nest_asyncio # type: ignore
nest_asyncio.apply()  # Allow nested event loops

import streamlit as st
import torch
import wolframalpha  # type: ignore
import wikipedia  # type: ignore
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer  # type: ignore
import yake  # type: ignore

# Configure Streamlit: disable file watcher to avoid Torch class inspection issues
st.set_option("server.fileWatcherType", "none")
st.set_page_config(page_title="Debate Chatbot", layout="wide")
st.title("🤖 AI Debate Chatbot (Fact & Evidence-Based)")

# Device Handling: Use MPS if available, otherwise CPU
device: str = "mps" if torch.backends.mps.is_available() else "cpu"
MODEL_NAME: str = "debate_model_finetuned"

@st.cache_resource
def load_model() -> tuple[AutoModelForCausalLM, AutoTokenizer]:
    """Loads and caches the AI debate model on MPS or CPU."""
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16  # Use half precision for MPS
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    return model, tokenizer

model, tokenizer = load_model()

# API Keys
WOLFRAM_APP_ID: str = "RRTPWP-LV8UT462U2"
NEWS_API_KEY: str = "2f95e9cb3cf44003b2e7e6e73be900c8"

class EvidenceGatherer:
    """Gathers evidence dynamically from Wolfram, Wikipedia, and News APIs."""
    def __init__(self) -> None:
        self.wolfram_client = wolframalpha.Client(WOLFRAM_APP_ID)
        self.keyword_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.3, windowsSize=1)

    def extract_keywords(self, text: str) -> list[str]:
        keywords = self.keyword_extractor.extract_keywords(text)
        return [kw[0] for kw in keywords[:3]]

    def get_wolfram_data(self, query: str) -> list[str]:
        try:
            res = self.wolfram_client.query(query)
            return [pod.text for pod in res.pods if pod.text]
        except Exception as e:
            return [f"⚠️ Wolfram Alpha failed to retrieve data: {e}"]

    def get_wikipedia_summary(self, query: str) -> str:
        try:
            page = wikipedia.page(query, auto_suggest=True)
            return f"📚 **{page.title}**\n{wikipedia.summary(query, sentences=2)}\n🔗 [Read more]({page.url})"
        except Exception as e:
            return f"⚠️ No Wikipedia page found: {e}"

    def get_news_articles(self, query: str) -> list[str]:
        try:
            url = f"https://newsapi.org/v2/everything?q={query}&sortBy=relevancy&pageSize=3&apiKey={NEWS_API_KEY}"
            response = requests.get(url).json()
            return [
                f"📰 **{article['title']}**\n{article['description']}\n🔗 [Read more]({article['url']})"
                for article in response.get('articles', [])
            ]
        except Exception as e:
            return [f"⚠️ News API failed to retrieve articles: {e}"]

def generate_response(topic: str, evidence: str) -> str:
    """Generates a structured debate response using the loaded model."""
    prompt = f"""
Debate Topic: {topic}
Collected Evidence:
{evidence}

Generate a compelling argument that:
1️⃣ Clearly presents the **position**  
2️⃣ Uses **factual evidence** for support  
3️⃣ Refutes **opposing arguments**  
4️⃣ Ends with a **strong conclusion**  

**Debate Response:**"""
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            inputs.input_ids,
            max_new_tokens=300,
            do_sample=True,          # Enable sampling for varied output
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output_ids[0].cpu(), skip_special_tokens=True)

st.subheader("🗣️ Chat with AI Debate Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input: str = st.chat_input("Enter your debate topic...")

if user_input:
    gatherer = EvidenceGatherer()
    with st.spinner("🔍 Gathering evidence..."):
        wiki_summary = gatherer.get_wikipedia_summary(user_input)
        wolfram_facts = gatherer.get_wolfram_data(user_input)
        news_articles = gatherer.get_news_articles(user_input)
    full_evidence = (
        f"{wiki_summary}\n\n📊 **Facts:**\n- " +
        "\n- ".join(wolfram_facts) +
        "\n\n📰 **Recent News:**\n- " +
        "\n- ".join(news_articles)
    )
    with st.spinner("🧠 Generating AI response..."):
        ai_response = generate_response(user_input, full_evidence)
    st.session_state.messages.append({"role": "user", "content": f"🗣️ {user_input}"})
    st.session_state.messages.append({"role": "assistant", "content": f"🤖 {ai_response}"})
    with st.chat_message("user"):
        st.markdown(f"🗣️ {user_input}")
    with st.chat_message("assistant"):
        st.markdown(f"🤖 {ai_response}")
