import pyttsx3
import feedparser
import time
import os

# Function to play a .wav file
def play_wav_file(file_path):
    os.system("aplay " + file_path)  # Linux command to play .wav file

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

# Function to fetch and parse the Atom feed
def fetch_and_parse_feed(feed_url):
    feed = feedparser.parse(feed_url)

    processed_entries = set()

    while True:
        for entry in feed.entries:
            entry_id = entry.id
            if entry_id not in processed_entries:
                title = entry.title
                summary = entry.summary

                # Play .wav file before processing
                play_wav_file("notification.wav")

                # Convert title to speech
                text_to_speech("New entry: " + title)

                # Convert summary to speech
                text_to_speech(summary)

                processed_entries.add(entry_id)

        time.sleep(1)  # Check for new entries every second

# Usage
if __name__ == "__main__":
    feed_url = "https://api.weather.gov/alerts/active.atom?area=KS"
    fetch_and_parse_feed(feed_url)
