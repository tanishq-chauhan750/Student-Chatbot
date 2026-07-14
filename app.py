import streamlit as st

# Custom styling for professional look
st.set_page_config(page_title="StudentBot", page_icon="🎓")
st.title("🎓 Student Support System")
st.subheader("Powered by AI (Simplified Version)")

# Knowledge Base
kb = {
    "fees": "The last date for fee submission is 30th July. Please visit the accounts portal.",
    "library": "Library hours: 9:00 AM to 6:00 PM (Monday-Saturday).",
    "exam": "The odd semester exams are scheduled to begin from 15th August.",
    "internship": "For internship letters, please contact the TPO cell at tpo@college.edu.",
    "help": "I can help with: Fees, Library, Exams, and Internship queries."
}

def get_response(query):
    query = query.lower()
    for key in kb:
        if key in query:
            return kb[key]
    return "I am sorry, I couldn't understand that. Please email support@college.edu."

if "chat" not in st.session_state: st.session_state.chat = []

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("Ask about fees, exams, library..."):
    st.session_state.chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    response = get_response(prompt)
    st.session_state.chat.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"): st.markdown(response)