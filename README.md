#L.I.T.A. — Lifetime, I’m Always There

L.I.T.A. is an emotionally aware AI companion designed to detect user emotions and respond with empathy, context, and conversational continuity. Powered by transformer-based emotion analysis and generative AI, the system aims to create meaningful, human-centered digital interactions.

Overview

L.I.T.A. receives user text input, identifies the dominant emotion, and generates responses that combine structured emotional grounding with adaptive dialogue. Each interaction is stored as part of an evolving emotional journey, enabling users to reflect on their session-level mood patterns.

Features

Emotion Detection
	•	Utilizes the pre-trained model j-hartmann/emotion-english-distilroberta-base.
	•	Extracts dominant emotion and confidence scores.
	•	Cached using Streamlit resource caching for efficient inference.

Empathetic Response System
	•	Layer 1: Curated emotion-specific supportive statements.
	•	Layer 2: GPT-powered adaptive responses based on conversational context.
	•	Ensures both reliability and personalization.

Conversational Memory
	•	Tracks user inputs, detected emotions, and AI responses throughout the session.
	•	Displays an emotional timeline in reverse chronological order.
	•	Creates continuity and a sense of being understood.

Minimalist UI
	•	Built with Streamlit for real-time interaction.
	•	Dark-themed, minimal, low-distraction interface.
	•	Clean visual separation of user input, detected emotion, and AI response.

Methodology

L.I.T.A. follows a structured methodology grounded in affective computing and modern NLP practices. User input is captured through a minimal Streamlit interface designed for clarity and emotional comfort. The text is processed using a transformer-based emotion classifier that identifies the dominant emotional tone. A two-layer empathetic response framework then generates output: a curated supportive statement provides emotional grounding, while a generative AI model produces a contextually adaptive response informed by recent conversation history. Each exchange is stored in session memory, forming an accessible emotional journey for the user and reinforcing connection and continuity within the session.

Installation

1. Clone the Repository

git clone <your-repo-url>
cd <repo-folder>

2. Install Dependencies

pip install -r requirements.txt

3. Set Your OpenAI API Key

export OPENAI_API_KEY="your-key-here"

4. Run the Application

streamlit run app.py

Project Structure

LITA/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── assets/                 # Optional UI assets (logos, images, etc.)

Future Enhancements
	•	Multi-modal emotion detection (voice tone, facial cues)
	•	Long-term memory across sessions
	•	Personalized emotional profiles
	•	Mood trend visualization
	•	Well-being tool integration (journaling, grounding exercises)

⸻

License

This project is licensed under the MIT License.
