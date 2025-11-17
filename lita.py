# import streamlit as st
# from transformers import pipeline

# st.set_page_config(
#     page_title="L.I.T.A. - Lifetime, I'm Always There",
#     page_icon="🤖",
#     layout="centered"
# )

# st.markdown("""
#     <style>
#     body {
#         background-color: #0e1117;
#         color: #e0e0e0;
#         font-family: 'Inter', sans-serif;
#     }
#     .stApp {
#         background-color: #0e1117;
#     }
#     h1, h2, h3 {
#         color: #66c0f4;
#         text-align: center;
#         font-weight: 500;
#     }
#     textarea {
#         background-color: #1b1f27 !important;
#         color: #e0e0e0 !important;
#         border: 1px solid #30363d !important;
#         border-radius: 10px !important;
#         padding: 12px !important;
#         font-size: 15px !important;
#     }
#     div.stButton > button:first-child {
#         background-color: #222831;
#         color: #f2f2f2;
#         border: 1px solid #30363d;
#         border-radius: 8px;
#         padding: 0.6em 2em;
#         font-size: 15px;
#         transition: 0.2s ease-in-out;
#     }
#     div.stButton > button:first-child:hover {
#         background-color: #66c0f4;
#         color: #0e1117;
#     }
#     .emotion-box {
#         background-color: #161b22;
#         border-left: 4px solid #66c0f4;
#         border-radius: 6px;
#         padding: 12px 16px;
#         margin-top: 20px;
#         font-size: 16px;
#         color: #e0e0e0;
#     }
#     .response-box {
#         background-color: #1b1f27;
#         border-left: 4px solid #3aafa9;
#         border-radius: 6px;
#         padding: 14px 18px;
#         margin-top: 12px;
#         font-size: 15px;
#         color: #cccccc;
#     }
#     footer {
#         text-align: center;
#         color: #777;
#         font-size: 12px;
#         margin-top: 30px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1>L.I.T.A.</h1>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align:center; color:#999;'>Lifetime, I'm Always There</h3>", unsafe_allow_html=True)
# st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)

# @st.cache_resource
# def load_model():
#     return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

# emotion_model = load_model()

# responses = {
#     "joy": "That’s great to hear! Keep embracing that positivity 🌼",
#     "sadness": "It’s okay to feel sad. Allow yourself to rest and reflect 💙",
#     "anger": "Try to pause and breathe — calm is just a few breaths away 🌿",
#     "fear": "You’re safe here. Facing your fears slowly makes you stronger 🌙",
#     "surprise": "Unexpected moments often bring growth 🌠",
#     "disgust": "It’s alright to feel off. Let the feeling pass with time 🕊️",
#     "neutral": "I’m listening — tell me more about what’s on your mind ☕"
# }

# user_input = st.text_area("L.I.T.A. wants to know how are you feeling today:", placeholder="Type something like 'I feel anxious about exams'")

# if st.button("Analyze Emotion"):
#     if user_input.strip():
#         with st.spinner("Analyzing your emotion..."):
#             result = emotion_model(user_input)[0]
#             emotion = result["label"].lower()

#             st.markdown(f"<div class='emotion-box'>Detected Emotion: <b>{emotion.capitalize()}</b></div>", unsafe_allow_html=True)

#             response_text = responses.get(emotion, "I'm here with you 💖")
#             st.markdown(f"<div class='response-box'>{response_text}</div>", unsafe_allow_html=True)

#     else:
#         st.warning("Please enter a message first.")

# st.markdown("<footer>© 2025 L.I.T.A. - Lifetime, I'm Always There</footer>", unsafe_allow_html=True)

import streamlit as st
from transformers import pipeline
from openai import OpenAI
import random

st.set_page_config(
    page_title="L.I.T.A. - Lifetime, I'm Always There",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}
.stApp {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #66c0f4;
    text-align: center;
    font-weight: 500;
}
textarea {
    background-color: #1b1f27 !important;
    color: #e0e0e0 !important;
    border: 1px solid #30363d !important;
    border-radius: 10px !important;
    padding: 12px !important;
    font-size: 15px !important;
}
div.stButton > button:first-child {
    background-color: #222831;
    color: #f2f2f2;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 0.6em 2em;
    font-size: 15px;
    transition: 0.2s ease-in-out;
}
div.stButton > button:first-child:hover {
    background-color: #66c0f4;
    color: #0e1117;
}
.chat-history {
    background-color: #161b22;
    border-radius: 10px;
    padding: 15px;
    margin-top: 20px;
}
.response-box {
    background-color: #1b1f27;
    border-left: 4px solid #3aafa9;
    border-radius: 6px;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 15px;
    color: #cccccc;
}
footer {
    text-align: center;
    color: #777;
    font-size: 12px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>L.I.T.A.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#999;'>Lifetime, I'm Always There</h3>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)

@st.cache_resource
def load_emotion_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=False
    )

emotion_model = load_emotion_model()

responses = {
    "joy": [
        "That’s wonderful to hear! Keep shining 🌞",
        "Your happiness is contagious — I love hearing that 💛",
        "Joy suits you — keep it close 🌼"
    ],
    "sadness": [
        "It’s okay to feel this way. I’m right here 💙",
        "Even cloudy days have their purpose 🌧️",
        "This moment will pass — just hold on 🌙"
    ],
    "anger": [
        "Take a deep breath — peace will return 🌿",
        "Your feelings are valid. Let’s find calm 🔥",
        "You’re doing great. Don’t let anger dim your light 🌾"
    ],
    "fear": [
        "Courage means feeling fear and moving anyway 🌔",
        "You’re safe here — one step at a time 🌫️",
        "Bravery often hides behind fear 🌱"
    ],
    "surprise": [
        "Life loves to keep us guessing 🌠",
        "Whoa, didn’t see that coming either 😄",
        "Surprises are little sparks of change ✨"
    ],
    "disgust": [
        "It’s okay to feel off sometimes 🕊️",
        "Let’s take a pause — you deserve peace 🌊",
        "Not everything needs your energy. Release it 🌬️"
    ],
    "neutral": [
        "I’m listening — what’s on your mind ☕",
        "Sometimes being neutral means balance 🌤️",
        "It’s calm moments like this that help you reset 💭"
    ]
}

if "history" not in st.session_state:
    st.session_state["history"] = []

def analyze_emotion(text):
    result = emotion_model(text)[0]
    return result["label"].lower(), result["score"]

def get_response(emotion):
    return random.choice(responses.get(emotion, ["I'm here with you 💖"]))

def generate_chatbot_reply(user_text, emotion, base_response):
    try:
        client = OpenAI(api_key="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")
        system_prompt = (
            f"You are L.I.T.A., an empathetic AI companion. "
            f"The user feels {emotion}. Respond warmly and concisely (max 3 sentences)."
        )
        messages = [{"role": "system", "content": system_prompt}]
        for chat in st.session_state["history"][-2:]:
            messages.append({"role": "user", "content": chat["text"]})
            messages.append({"role": "assistant", "content": chat["response"]})
        messages.append({"role": "user", "content": user_text})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.8,
            max_tokens=150
        )
        return response.choices[0].message.content.strip() or base_response
    except Exception as e:
        st.warning(f"⚠️ Chatbot error: {str(e)}")
        return base_response

user_input = st.text_area(
    "L.I.T.A. wants to know how are you feeling today?",
    placeholder="Type something like 'I feel nervous but hopeful today...'"
)

if st.button("Analyze Emotion"):
    if user_input.strip():
        with st.spinner("Analyzing your emotion..."):
            emotion, confidence = analyze_emotion(user_input)
            base_response = get_response(emotion)
            ai_reply = generate_chatbot_reply(user_input, emotion, base_response)
            st.session_state["history"].append({
                "text": user_input,
                "emotion": emotion.capitalize(),
                "confidence": f"{confidence * 100:.2f}%",
                "response": ai_reply
            })
            
st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)

if st.session_state["history"]:
    st.markdown("<h3>Your Journey with L.I.T.A.</h3>", unsafe_allow_html=True)
    for chat in reversed(st.session_state["history"]):
        st.markdown(f"""
        <div class='chat-history'>
            <b>You:</b> {chat['text']}<br>
            <span style='color:#66c0f4;'>Detected Emotion:</span> {chat['emotion']} ({chat['confidence']})<br>
            <div class='response-box'><b>L.I.T.A.:</b> {chat['response']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<footer>© 2025 L.I.T.A. - Lifetime, I'm Always There</footer>", unsafe_allow_html=True)