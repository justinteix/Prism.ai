# Prism.ai

Prism.ai is an AI-powered home assistant that leverages the advanced capabilities of GPT-4 to provide a smarter, more efficient home assistant experience. Prism.ai offers insightful recommendations and answers to your queries using natural language processing.

## Table of Contents
- [Features](##features)

- [Installation](##installation)

- [Usage](##usage)

- [Configuration](##configuration)

- [Contributing](##contributing)

- [License](##license)

- [Acknowledgments](##acknowledgments)

## Features
- **Voice Activation**: Prism.ai listens for the wake word "Hey Prism" and responds to your voice commands.

- **Natural Language Understanding**: Prism.ai uses GPT-4 to comprehend and respond to your spoken queries naturally.

- **Text-to-Speech**: Prism.ai can convert responses into speech, making interaction seamless.

- **Speech Recognition**: Prism.ai listens and understands spoken commands using Google's Speech Recognition API.

- **Audio Feedback**: Prism.ai provides audio feedback with sound effects and speech responses.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/justinteix/Prism.ai.git
```

2. Navigate to the project directory:
````bash
cd prism.ai
````

3. Create a Python virtual environment:
````bash
python3 -m venv venv
````
4. Activate the virtual environment:
- For Windows:
````bash
venv\Scripts\activate
````
- For macOS/Linux:
````bash
source venv/bin/activate
````

5. Install the required dependencies:
```bash
pip install -r requirements.txt
````

6. Create a .env file with your OpenAI API key:
````bash
echo "OPENAI_API_KEY=your_openai_api_key" > .env
````

## Usage
1. Ensure you have a microphone and speaker connected to your system.

2. Start the Prism.ai application:
````bash
python brain.py
````

3. The application will listen for the wake word "Hey Prism" and respond to your voice commands.

## Configuration
You may configure Prism.ai through environment variables in a .env file:

- OPENAI_API_KEY: Your OpenAI API key to use GPT-4 and other services.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Released under the
[MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgments
Using OpenAI's GPT-4 and Text to speech API, as well as Google's Speech Recognition API, to power the Prism.ai.