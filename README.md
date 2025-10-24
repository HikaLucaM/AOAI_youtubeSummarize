# YouTube Video Summarizer with OpenAI/Azure OpenAI

A Python script that fetches YouTube video transcripts and generates summaries using OpenAI or Azure OpenAI.

## ✨ Features

- 📝 Automatic YouTube video transcript fetching
- 🤖 High-quality summarization using OpenAI or Azure OpenAI (GPT)
- 🔄 Support for both APIs (OpenAI and Azure OpenAI)
- 🌏 Multi-language support (English, Japanese, etc.)
- 🔒 Secure API configuration using environment variables

## 📋 Prerequisites

- Python 3.7 or higher
- **Either** Azure OpenAI Service **OR** OpenAI API account with API access
- YouTube video with available transcripts

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/HikaLucaM/AOAI_youtubeSummarize.git
cd AOAI_youtubeSummarize
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy the `.env.example` file to `.env` and fill in your API credentials:

```bash
cp .env.example .env
```

#### Option A: Using Azure OpenAI

Edit `.env` file:

```env
API_TYPE=azure
OPENAI_API_KEY=your_azure_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo
```

#### Option B: Using OpenAI

Edit `.env` file:

```env
API_TYPE=openai
OPENAI_API_KEY=sk-your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

### 4. Run the script

```bash
python main.py
```

## 💡 Usage

1. Run the script
2. Enter the YouTube video URL
3. Enter the language code (e.g., `en` for English, `ja` for Japanese)
4. Wait for the summary

### Example

```
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the language code (en/ja): en

Video ID: dQw4w9WgXcQ
Fetching transcript in 'en'...
Transcript length: 5432 characters

Generating summary with Azure OpenAI...

============================================================
SUMMARY
============================================================
[Summary will be displayed here]
============================================================
```

## ⚠️ Limitations

- **Transcript length limit**: The script processes up to 10,000 characters of transcript. Very long videos may be truncated.

- **Transcript availability**: Only works with videos that have transcripts available (auto-generated or manual).

- **Language support**: While the script supports multiple languages, you need to specify the correct language code for the video.

## 🔧 Configuration

You can modify the following parameters in `main.py`:

- `MAX_TRANSCRIPT_LENGTH`: Maximum transcript length to process (default: 10,000)
- `temperature`: OpenAI temperature parameter (default: 0.7)
- `max_tokens`: Maximum tokens for the summary (default: 2,800)

## 📝 License

MIT License - Feel free to use and modify this project.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📸 Screenshots

![image](https://github.com/hikaruminagawa/AOAI_youtubeSummarize/assets/96165184/ba9400fe-e566-4c23-ad51-d0afa7149f18)
![image](https://github.com/hikaruminagawa/AOAI_youtubeSummarize/assets/96165184/772dbf15-0497-49d7-aa03-8613aff0b195)

## 🔗 Related Resources

- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
