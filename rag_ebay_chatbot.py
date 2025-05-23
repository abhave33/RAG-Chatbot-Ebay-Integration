import os
import requests
import streamlit as st
import openai

# 🔑 Set your API keys
os.environ["OPENAI_API_KEY"] = "your-key"
openai.api_key = os.environ["OPENAI_API_KEY"]
EBAY_APP_ID = "your-app-id"

# 📡 eBay API Function
def query_ebay(query, app_id=EBAY_APP_ID):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    params = {
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": app_id,
        "RESPONSE-DATA-FORMAT": "JSON",
        "keywords": query,
        "paginationInput.entriesPerPage": "5",
    }

    response = requests.get(url, params=params)
    try:
        data = response.json()
        print("🔍 eBay response:", data)  # 👈 This shows the actual structure
    except Exception as e:
        print("❌ Failed to parse JSON:", e)
        print("Raw response text:", response.text)
        return []

    # Safely attempt to extract results
    try:
        items = data["findItemsByKeywordsResponse"][0]["searchResult"][0].get("item", [])
        return [item["title"][0] for item in items]
    except KeyError:
        print("⚠️ Unexpected eBay API structure:", data)
        return []
# 🧠 Use OpenAI GPT to format the response
def generate_response(user_query, listings):
    joined = "\n".join(f"- {title}" for title in listings)
    prompt = f"""
You are a shopping assistant. A user asked: "{user_query}"

Here are eBay results:
{joined}

Generate a helpful, conversational response summarizing the best listings.
"""
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]

# 🖼️ Streamlit UI
st.set_page_config(page_title="eBay GPT Shopping Assistant", layout="centered")
st.title("🛒 eBay AI Chatbot")
st.write("Type what you're looking for. I’ll find and summarize live eBay listings!")

query = st.text_input("What are you shopping for?", placeholder="e.g., TVs under $1500")

if st.button("Search") and query:
    with st.spinner("Searching eBay..."):
        items = query_ebay(query)
        if not items:
            st.error("No listings found.")
        else:
            answer = generate_response(query, items)
            st.subheader("🧠 Smart Response")
            st.write(answer)
