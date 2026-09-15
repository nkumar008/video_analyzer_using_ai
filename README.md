YouTube Video Analyzer

A Streamlit-based AI application that analyzes YouTube videos and generates useful insights from their transcripts using an AI agent.

## Features

- Enter a YouTube video URL
- Extract the video transcript
- Analyze the transcript using an AI model
- Generate a clear and useful response based on the video content
- Simple and interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Agno
- OpenAI
- YouTube Transcript API
- python-dotenv

## Project Structure

    youtube-analyzer/
    ui.py
    youtube_analyzer.py
    requirements.txt
    .gitignore
    README.txt

## Installation

1. Clone the repository:

       git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder:

       cd youtube-analyzer

3. Create a virtual environment:

       python -m venv venv

4. Activate the virtual environment on Windows:

       venv\Scripts\activate

5. Install the required packages:

       pip install -r requirements.txt

## API Key Setup

Create a `.env` file in the project directory:

    OPENAI_API_KEY=your_openai_api_key

Never upload your `.env` file or API key to GitHub.

## Run the Application

Start the Streamlit application with:

    streamlit run ui.py

The application will open in your browser.

## Deployment

This project can be deployed using Streamlit Community Cloud.

Select the GitHub repository and set the main file to:

    ui.py

For deployment, add your OpenAI API key using Streamlit Secrets instead of uploading the `.env` file.

## Author

Created as an AI/GenAI learning project.
