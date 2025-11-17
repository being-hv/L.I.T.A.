

L.I.T.A. — Lifetime, I’m Always There

L.I.T.A. is an emotionally aware AI companion designed to identify user emotions and respond with empathy, continuity, and conversational depth. Built with Streamlit and powered by transformer-based emotion analysis and generative AI, L.I.T.A. aims to create meaningful human–AI interactions rooted in psychological safety and emotional understanding.

⸻

Overview

L.I.T.A. analyzes user input, detects the dominant emotion, and generates responses that combine structured emotional grounding with adaptive conversational reasoning. The system blends affective computing principles with human-centered design to create a companion that listens, remembers, and responds with care. Each interaction is stored as part of an evolving emotional journey, allowing users to reflect on their emotional patterns throughout a session.

⸻

Key Features

Emotion Detection
	•	Uses the pre-trained model j-hartmann/emotion-english-distilroberta-base for contextual emotion classification.
	•	Provides a confidence score for each detected emotion.
	•	Ensures smooth inference through Streamlit’s resource caching.

Empathetic Response System
	•	Layer 1: Curated emotion-specific supportive statements.
	•	Layer 2: GPT-based adaptive replies incorporating recent conversation context.
	•	Combines reliability (static responses) with personalization (generative responses).

Conversational Memory
	•	Stores session-level user inputs, detected emotions, and AI responses.
	•	Displays the complete emotional journey in reverse chronological order.
	•	Enhances continuity and connection within a single session.

Minimalist User Interface
	•	Built with Streamlit for real-time interaction.
	•	Dark-themed, low-distraction design to reduce cognitive strain.
	•	Clean message containers and structured layout for readability.

⸻

Methodology

L.I.T.A. follows a structured methodology centered on emotional interpretation, empathetic communication, and user-focused design. The system begins by receiving text input through a Streamlit interface designed for comfort and clarity. The input is processed using a transformer-based emotion classification model, which identifies the user’s dominant emotion with high contextual sensitivity. Curated responses provide immediate emotional grounding, while a generative AI model produces adaptive replies based on the detected emotion and conversational history. Finally, each interaction is saved to session memory, enabling users to trace their evolving emotional state and reinforcing a sense of continuity throughout the experience.

⸻

Installation
	1.	Clone the repository

git clone <your-repo-url>
cd <repo-folder>


	2.	Install dependencies

pip install -r requirements.txt


	3.	Add your OpenAI API key

export OPENAI_API_KEY="your-key-here"


	4.	Run the application

streamlit run app.py



⸻

Project Structure

/LITA
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── assets/                 # Optional UI assets or logos


⸻

Future Improvements
	•	Multi-modal emotion recognition (voice, sentiment patterns)
	•	Long-term memory across sessions
	•	Personalization based on user preferences
	•	Mood trend analytics
	•	Integration with well-being tools or journaling features

⸻

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with attribution.

⸻

