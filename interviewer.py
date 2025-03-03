# interviewer.py

import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from sentiment_analyzer import SentimentAnalyzer
from config import QUESTIONS, PASS_THRESHOLD

class Interviewer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.analyzer = SentimentAnalyzer()
        self.total_score = 0
        self.responses = []
        self.scores = []

    def text_to_speech(self, text, filename='question.mp3'):
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            print("Transcribing...")
            text = self.recognizer.recognize_google(audio)
            print(f"Candidate response: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

    def ask_question(self, question):
        print(f"Interviewer: {question}")
        self.text_to_speech(question)
        response = self.speech_to_text()
        return response

    def conduct_interview(self):
        for idx, question in enumerate(QUESTIONS):
            response = self.ask_question(question)
            self.responses.append(response)
            score = self.analyzer.analyze(response)
            self.scores.append(score)
            print(f"Response Sentiment Score: {score}\n")
            self.total_score += score

    def evaluate_candidate(self):
        average_score = self.total_score / len(QUESTIONS)
        result = "Pass" if average_score >= PASS_THRESHOLD else "Fail"
        print(f"Candidate's Average Score: {average_score}")
        print(f"Final Decision: {result}")
        self.save_results(average_score, result)

    def save_results(self, average_score, result):
        if not os.path.exists('output'):
            os.makedirs('output')
        with open('output/results.txt', 'w') as f:
            for i, question in enumerate(QUESTIONS):
                f.write(f"Question {i+1}: {question}\n")
                f.write(f"Response: {self.responses[i]}\n")
                f.write(f"Sentiment Score: {self.scores[i]}\n\n")
            f.write(f"Candidate's Average Score: {average_score}\n")
            f.write(f"Final Decision: {result}\n")
