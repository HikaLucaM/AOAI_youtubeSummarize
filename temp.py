from youtube_transcript_api import YouTubeTranscriptApi

video_url = input("Enter the video url: ")
video_id = video_url.split("=")[-1]
language = input("Enter the language (en/ja):")

transcripts = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
combined_transcipts = " ".join([item['text'] for item in transcripts])



