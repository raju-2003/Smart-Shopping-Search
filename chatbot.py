import streamlit as st
import requests
import json
import secrets

def get_bot_response(user_input):
    url = "https://google.serper.dev/search"
    
    payload = json.dumps({
        "q": user_input
    })
    
    headers = {
        'X-API-KEY': secrets.SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    
    print(response_data)
    links = [result['link'] for result in response_data.get('organic', [])]
    print(links)
    return links

def main():
    st.title("Chatbot")

    user_input = st.text_input("You:")
    response_links = []

    if st.button("Send"):
        if user_input.strip() != '':
            response_links = get_bot_response(user_input)
            
    
    
    if response_links:
       for link in response_links:
                st.write(link)


if __name__ == "__main__":
    main()
