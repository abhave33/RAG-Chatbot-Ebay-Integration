# 🛍️ RAG eBay Chatbot with Streamlit
![Screenshot](chatbotpic.png)
- Deployed on streamlit: https://rag-chatbot-ebay-integration-anj.streamlit.app/

This is a simple AI-powered shopping assistant built using:

- 🧠 OpenAI GPT (via `openai`)
- 🛒 Real-time eBay product search (eBay Finding API)
- ⚙️ Streamlit UI
- 💡 Natural language input (e.g., "Find me TVs under $1500")

## 🧪 How It Works

1. The user enters a natural-language shopping query.
2. The app uses the eBay API to find matching listings.
3. Results are passed to GPT-4 for summarization.
4. The chatbot responds conversationally with top products.

## 🚀 Run It Locally

```bash
pip install -r requirements.txt
streamlit run rag_ebay_chatbot.py
