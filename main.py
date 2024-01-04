from youtube_transcript_api import YouTubeTranscriptApi
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://mainaoai.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.environ['OPENAI_API_KEY']



video_url = input("Enter the video url: ")
video_id = video_url.split("=")[-1]
language = input("Enter the language (en/ja):")

transcripts = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
combined_transcipts = " ".join([item['text'] for item in transcripts])


prompt = [
  {"role": "system", "content": "You are a helpful assistant. Summarize the video with its transcipt provided by user. Reply in the same language as the transcript"},
  {"role": "user", "content": combined_transcipts},
]

def summarize():
  response = openai.ChatCompletion.create(
    engine="gpt35Turbo",
    messages = prompt,
    temperature=0.7,
    max_tokens=2800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )
  return response.choices[0].message.content


summary = summarize()
print(summary)

