# import streamlit as st
# from transformers import pipeline
# from openai import OpenAI
# import time
# import random

# st.set_page_config(page_title="L.I.T.A.", page_icon="🤖", layout="centered")

# # ---------------- SESSION STATE -----------------
# if "screen" not in st.session_state:
#     st.session_state.screen = "menu"
# if "mood" not in st.session_state:
#     st.session_state.mood = None
# if "chat" not in st.session_state:
#     st.session_state.chat = []
# if "answers" not in st.session_state:
#     st.session_state.answers = {}
# if "typing" not in st.session_state:
#     st.session_state.typing = False

# questions = {
#     "q1": "How often have you felt down or hopeless recently?",
#     "q2": "How often have you felt anxious or on edge?",
#     "q3": "How often have you struggled to relax or focus?"
# }

# options = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

# @st.cache_resource
# def load_emotion_model():
#     return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

# # ---------------- THEME -----------------
# def apply_theme(mood):
#     colors = {
#         "joy": "#1b2b1b",
#         "neutral": "#1b1f27",
#         "sadness": "#151a2e",
#         "fear": "#2b1b1b",
#         "anger": "#2e1a1a"
#     }
#     bg = colors.get(mood, "#0e1117")

#     st.markdown(f"""
#     <style>
#     body {{ background-color: {bg}; color: #e0e0e0; }}
#     .user-msg {{ animation: fade 0.5s; background:#222; padding:10px; border-radius:8px; margin:8px 0; }}
#     .bot-msg {{ animation: slide 0.5s; background:#1b1f27; padding:10px; border-left:4px solid #66c0f4; border-radius:8px; margin:8px 0; }}
#     @keyframes fade {{ from {{opacity:0}} to {{opacity:1}} }}
#     @keyframes slide {{ from {{transform:translateX(-10px); opacity:0}} to {{transform:translateX(0); opacity:1}} }}
#     </style>
#     """, unsafe_allow_html=True)

# # ---------------- ANALYZE CHECK-IN -----------------
# def analyze_checkin(ans):
#     total = sum(options[v] for v in ans.values())
#     if total <= 2: return "joy"
#     elif total <= 4: return "neutral"
#     elif total <= 6: return "sadness"
#     elif total <= 7: return "fear"
#     else: return "anger"

# # ---------------- AI REPLY -----------------
# def ai_reply(text, mood):
#     try:
#         client = OpenAI(api_key="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")
#         prompt = f"You are L.I.T.A., an empathetic AI. The user's mood is {mood}. Respond naturally in under 3 sentences."
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": prompt},
#                 {"role": "user", "content": text}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception:
#         return "Something went wrong, but I'm still here."

# # ---------------- MENU SCREEN -----------------
# if st.session_state.screen == "menu":
#     st.markdown("<h1 style='text-align:center;'>Welcome to L.I.T.A.</h1>", unsafe_allow_html=True)

#     if st.button("Start Mood Check-In"):
#         st.session_state.screen = "checkin"
#         st.rerun()

# # ---------------- CHECK-IN SCREEN -----------------
# elif st.session_state.screen == "checkin":
#     st.markdown("<h2 style='text-align:center;'>Mood Check-In</h2>", unsafe_allow_html=True)

#     with st.form("form"):
#         for key, q in questions.items():
#             st.session_state.answers[key] = st.radio(q, list(options.keys()), key=key)
#         submit = st.form_submit_button("Submit")

#     if submit:
#         st.session_state.mood = analyze_checkin(st.session_state.answers)
#         apply_theme(st.session_state.mood)
#         st.session_state.screen = "chat"
#         st.rerun()

# # ---------------- CHAT SCREEN -----------------
# elif st.session_state.screen == "chat":
#     apply_theme(st.session_state.mood)
#     st.markdown("<h2 style='text-align:center;'>Chat with L.I.T.A.</h2>", unsafe_allow_html=True)

#     for sender, msg in st.session_state.chat:
#         if sender == "user":
#             st.markdown(f"<div class='user-msg'><b>You:</b> {msg}</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='bot-msg'><b>L.I.T.A.:</b> {msg}</div>", unsafe_allow_html=True)

#     if st.session_state.typing:
#         st.markdown("<div class='bot-msg'><i>L.I.T.A. is typing...</i></div>", unsafe_allow_html=True)

#     user_input = st.text_input("You:")

#     if st.button("Send"):
#         if user_input.strip():
#             st.session_state.chat.append(("user", user_input))
#             st.session_state.typing = True
#             st.rerun()

#     if st.session_state.typing:
#         time.sleep(1)
#         last_user_msg = st.session_state.chat[-1][1]
#         bot = ai_reply(last_user_msg, st.session_state.mood)
#         st.session_state.chat.append(("bot", bot))
#         st.session_state.typing = False
#         st.rerun()

# st.markdown("<footer style='text-align:center;color:#888;margin-top:30px;'>© 2025 L.I.T.A.</footer>", unsafe_allow_html=True)

import streamlit as st
from transformers import pipeline
from openai import OpenAI
import time
import datetime

st.set_page_config(page_title="L.I.T.A.", page_icon="🤖", layout="centered")

if "screen" not in st.session_state: st.session_state.screen = "menu"
if "mood" not in st.session_state: st.session_state.mood = None
if "chat" not in st.session_state: st.session_state.chat = []
if "answers" not in st.session_state: st.session_state.answers = {}
if "typing" not in st.session_state: st.session_state.typing = False

questions = {
    "q1": "How often have you felt down or hopeless recently?",
    "q2": "How often have you felt anxious or on edge?",
    "q3": "How often have you struggled to relax or focus?"
}

options = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)


def base_style():
    st.markdown("""
    <style>

    body {
        background: radial-gradient(circle at top, #202533 0, #050608 55%) !important;
        color: #eaeaea !important;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, sans-serif;
    }

    .app-wrapper {
        width: 760px;
        max-width: 90%;
        margin: 40px auto;
    }

    .glass {
        background: rgba(255,255,255,0.06);
        padding: 26px;
        border-radius: 20px;
        box-shadow: 0 18px 45px rgba(0,0,0,0.45);
        border: 1px solid rgba(255,255,255,0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 18px;
    }

    .title {
        text-align: center;
        margin-bottom: 10px;
        font-size: 2rem;
        font-weight: 700;
    }

    .subtitle {
        text-align: center;
        opacity: 0.85;
        font-size: 1rem;
        margin-bottom: 15px;
    }

    /* CHAT BUBBLES */
    .user-msg {
        background: rgba(255,255,255,0.12);
        padding: 12px 16px;
        border-radius: 16px 16px 4px 16px;
        max-width: 80%;
        margin-left: auto;
        margin-bottom: 10px;
        animation: fade 0.25s ease-out;
        box-shadow: 0 6px 18px rgba(0,0,0,0.4);
    }

    .bot-msg {
        background: rgba(102,192,244,0.12);
        padding: 12px 16px;
        border-radius: 16px 16px 16px 4px;
        max-width: 80%;
        margin-right: auto;
        margin-bottom: 10px;
        border-left: 2px solid #66c0f4;
        animation: slide 0.25s ease-out;
        box-shadow: 0 6px 18px rgba(0,0,0,0.45);
    }

    @keyframes fade { from {opacity:0; transform:translateY(4px);} to {opacity:1;} }
    @keyframes slide { from {opacity:0; transform:translateY(7px);} to {opacity:1;} }

    /* FIX THE BLACK INPUT BOX */
    input[type="text"], textarea, .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
        padding: 14px 16px !important;
        color: #ededed !important;
        border-radius: 14px !important;
        box-shadow: 0 6px 18px rgba(0,0,0,0.35) !important;
        width: 100% !important;
        font-size: 16px !important;
    }

    .stTextInput > div {
        background: transparent !important;
    }

    input[type="text"]:focus {
        outline: none !important;
        border: 1px solid rgba(255,255,255,0.35) !important;
        background: rgba(255,255,255,0.14) !important;
    }

    .center-btn button {
        width: 100%;
        padding: 12px;
        border-radius: 999px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.2);
        font-size: 1.1rem;
        transition: 0.25s;
    }

    .center-btn button:hover {
        background: rgba(255,255,255,0.22);
    }

    footer {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 25px;
    }

    </style>
    """, unsafe_allow_html=True)


def analyze_checkin(ans):
    total = sum(options[v] for v in ans.values())
    if total <= 2: return "joy"
    elif total <= 4: return "neutral"
    elif total <= 6: return "sadness"
    elif total <= 7: return "fear"
    return "anger"


def ai_reply(text, mood):
    try:
        client = OpenAI(api_key="YOUR_KEY")  
        prompt = (
            f"You are L.I.T.A., a soft and empathetic AI companion. "
            f"The user's mood is {mood}. Reply warmly in 2–3 concise sentences."
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "I'm still here with you, even though something on my side went wrong."


base_style()

st.markdown("<div class='app-wrapper'>", unsafe_allow_html=True)


if st.session_state.screen == "menu":
    st.markdown("<h1 class='title'>L.I.T.A.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Lifetime, I'm Always There</p>", unsafe_allow_html=True)

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
    if st.button("Start Mood Check-In"):
        st.session_state.screen = "checkin"
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


elif st.session_state.screen == "checkin":
    st.markdown("<h2 class='title'>Mood Check-In</h2>", unsafe_allow_html=True)
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    with st.form("checkin"):
        for key, q in questions.items():
            st.session_state.answers[key] = st.radio(q, list(options.keys()), key=key)
        submitted = st.form_submit_button("Continue")

    st.markdown("</div>", unsafe_allow_html=True)

    if submitted:
        st.session_state.mood = analyze_checkin(st.session_state.answers)
        st.session_state.screen = "chat"
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else st.rerun()


elif st.session_state.screen == "chat":
    st.markdown("<h2 class='title'>L.I.T.A.</h2>", unsafe_allow_html=True)
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    for sender, msg in st.session_state.chat:
        if sender == "user":
            st.markdown(f"<div class='user-msg'><b>You</b><br>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-msg'><b>L.I.T.A.</b><br>{msg}</div>", unsafe_allow_html=True)

    user_input = st.text_input("You:")

    if st.button("Send") and user_input.strip():
        st.session_state.chat.append(("user", user_input))
        with st.spinner("L.I.T.A. is typing..."):
            reply = ai_reply(user_input, st.session_state.mood)
        st.session_state.chat.append(("bot", reply))
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<footer>© L.I.T.A. by Harshvardhanam</footer>", unsafe_allow_html=True)
