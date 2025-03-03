# AI Voice Interviewer

An AI-powered voice interviewer that conducts a five-question interview on ERP systems for metal work companies, analyzes candidate responses using sentiment analysis, and decides to pass or fail candidates based on their scores.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Outputs](#outputs)
- [Notes](#notes)
- [Enhancements](#enhancements)
- [License](#license)

## Introduction

This application simulates an AI interviewer that interacts with candidates through voice. It focuses on evaluating knowledge about ERP systems in the metal work industry. By leveraging speech recognition and sentiment analysis, it provides an objective assessment of candidate responses.

## Features

- **Voice Interaction**: Asks questions and captures responses via voice.
- **Fixed Question Set**: Contains five predefined questions specific to ERP systems for metal work companies.
- **Sentiment Analysis**: Analyzes responses to gauge sentiment polarity.
- **Scoring System**: Calculates scores based on sentiment to evaluate candidates.
- **Pass/Fail Decision**: Determines candidate suitability based on their overall score.
- **Result Logging**: Saves detailed interview results for review.

## Project Structure

```plaintext
ai_voice_interviewer/
├── data/
├── models/
├── output/
│   └── results.txt
├── requirements.txt
├── main.py
├── interviewer.py
├── sentiment_analyzer.py
├── config.py
└── README.md
data/: Placeholder for data resources.

models/: Placeholder for models (if extended).

output/: Stores interview transcripts and results.

requirements.txt: Lists all Python dependencies.

main.py: Entry point of the application.

interviewer.py: Handles the interview process.

sentiment_analyzer.py: Performs sentiment analysis.

config.py: Contains configuration variables.

README.md: Project documentation.

Requirements
Python 3.x

Libraries:

SpeechRecognition

PyAudio

gTTS

playsound

TextBlob

Installation
Clone the Repository

bash
git clone https://github.com/Ut277/ai_interviewer.git
cd ai_voice_interviewer
Set Up Virtual Environment

bash
python -m venv venv
Activate Virtual Environment

Windows:

bash
venv\Scripts\activate
Unix or MacOS:

bash
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Note: If you encounter issues installing PyAudio, you may need to install it using system-specific instructions.

Usage
Run the application using:

bash
python main.py
Process:

The interviewer will ask five questions aloud.

Candidate responses are recorded via microphone.

Responses are transcribed to text.

Sentiment analysis is performed on each response.

Scores are calculated, and a pass/fail decision is displayed.

Detailed results are saved in output/results.txt.

Configuration
Adjust settings in config.py:

python
# config.py

QUESTIONS = [
    "Can you explain how ERP systems benefit metal work companies?",
    "What challenges do metal work companies face when implementing ERP systems?",
    "How does an ERP system improve operational efficiency in metal fabrication?",
    "Can you discuss any trends in ERP solutions for the metal industry?",
    "How would you ensure data security within an ERP system for a metal works company?"
]

PASS_THRESHOLD = 0.1  # Adjust the threshold as needed
QUESTIONS: Modify or add questions as desired.

PASS_THRESHOLD: Set the minimum average sentiment score required to pass.

Outputs
Transcripts and Scores: Saved in output/results.txt.

Example Output:

plaintext
Question 1: Can you explain how ERP systems benefit metal work companies?
Response: [Candidate's response]
Sentiment Score: 0.2

...

Candidate's Average Score: 0.15
Final Decision: Pass
Notes
Speech Recognition:

Ensure your microphone is set up and functioning.

Background noise can affect transcription accuracy.

PyAudio Installation:

Windows: You might need to install PyAudio from a precompiled binary.

Visit: PyAudio Binaries

Unix/MacOS: You may need to install portaudio libraries first.

Internet Connection:

Required for gTTS and SpeechRecognition when using Google's services.
