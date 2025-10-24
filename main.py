"""
YouTube Video Summarizer using OpenAI or Azure OpenAI
This script downloads YouTube video transcripts and generates summaries using OpenAI API or Azure OpenAI.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Determine API type (Azure or OpenAI)
API_TYPE = os.getenv('API_TYPE', 'openai').lower()  # 'azure' or 'openai'

if API_TYPE == 'azure':
    # Configure Azure OpenAI
    openai.api_type = "azure"
    openai.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')
    openai.api_version = os.getenv('AZURE_OPENAI_API_VERSION', '2023-07-01-preview')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    # Validate Azure-specific environment variables
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
    if not openai.api_base:
        raise ValueError("AZURE_OPENAI_ENDPOINT is not set. Please check your .env file.")
    
    DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-35-turbo')
    MODEL_NAME = None  # Not used for Azure
    print(f"Using Azure OpenAI with deployment: {DEPLOYMENT_NAME}")
else:
    # Configure OpenAI
    openai.api_type = "openai"
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    # Validate OpenAI-specific environment variables
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
    
    DEPLOYMENT_NAME = None  # Not used for OpenAI
    MODEL_NAME = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    print(f"Using OpenAI with model: {MODEL_NAME}")

MAX_TRANSCRIPT_LENGTH = 10000


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    elif "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    else:
        return url  # Assume it's already a video ID


def get_transcript(video_id, language):
    """Fetch transcript for the given video ID and language."""
    try:
        transcripts = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        combined_transcript = " ".join([item['text'] for item in transcripts])[:MAX_TRANSCRIPT_LENGTH]
        return combined_transcript
    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise Exception(f"No transcript found for language: {language}")
    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")


def summarize(transcript):
    """Generate summary using OpenAI or Azure OpenAI."""
    prompt = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Summarize the video with its transcript provided by user. Reply in the same language as the transcript."
        },
        {
            "role": "user",
            "content": transcript
        },
    ]
    
    try:
        if API_TYPE == 'azure':
            # Azure OpenAI uses 'engine' parameter
            response = openai.ChatCompletion.create(
                engine=DEPLOYMENT_NAME,
                messages=prompt,
                temperature=0.7,
                max_tokens=2800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
        else:
            # OpenAI uses 'model' parameter
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=prompt,
                temperature=0.7,
                max_tokens=2800,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error generating summary: {str(e)}")


def main():
    """Main function to run the YouTube summarizer."""
    print("=" * 60)
    print("YouTube Video Summarizer")
    print("=" * 60)
    
    try:
        # Get user input
        video_url = input("Enter the YouTube video URL: ").strip()
        if not video_url:
            print("Error: Video URL cannot be empty.")
            return
        
        language = input("Enter the language code (en/ja): ").strip().lower()
        if language not in ['en', 'ja']:
            print("Warning: Only 'en' and 'ja' are tested. Proceeding anyway...")
        
        # Extract video ID
        video_id = extract_video_id(video_url)
        print(f"\nVideo ID: {video_id}")
        
        # Fetch transcript
        print(f"Fetching transcript in '{language}'...")
        transcript = get_transcript(video_id, language)
        print(f"Transcript length: {len(transcript)} characters")
        
        # Generate summary
        print("\nGenerating summary with Azure OpenAI...")
        summary = summarize(transcript)
        
        # Display result
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(summary)
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()

