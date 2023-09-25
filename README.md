# Voice Assistant README

This repository contains the source code for a simple Python-based voice assistant. This voice assistant can perform various tasks such as searching Wikipedia, opening web browsers, and interacting with YouTube. Below, you'll find information on how to set up and use this voice assistant.

## Features

- **Wikipedia Search:** You can ask the voice assistant to search for information on Wikipedia, and it will provide a summary of the topic.

- **Web Browsing:** You can instruct the voice assistant to open popular websites like YouTube and Google.

- **Time:** You can ask the voice assistant for the current time.

- **YouTube Search and Play:** You can ask the voice assistant to search for videos on YouTube and play the top result.

## Setup

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/voice-assistant.git
   ```

2. **Install Dependencies:** Ensure you have the required Python libraries installed. You can install them using `pip`:

   ```
   pip install pyttsx3 webbrowser wikipedia speech_recognition youtube-search googlesearch-python
   ```

3. **Voice Configuration:** In the code, the voice engine is configured to use `sapi5` and the first available voice. Make sure you have the necessary text-to-speech voices installed on your system.

4. **Browser Path:** Update the `browser_path` variable with the correct path to your web browser executable. The example provided is for Google Chrome.

## Usage

1. Run the Python script:

   ```
   python voice_assistant.py
   ```

   This will start the voice assistant.

2. Once the voice assistant is running, it will greet you based on the time of day (morning, afternoon, or evening).

3. You can give voice commands by saying them aloud. The voice assistant will recognize your command and execute the corresponding action. For example:

   - To search Wikipedia: "Wikipedia [your query]"
   - To open YouTube: "Open YouTube"
   - To ask for the time: "What's the time?"

4. To exit the voice assistant, you can say "Stop listening," and it will stop listening and close.

## Customization

You can customize the voice assistant by modifying the code to add more commands or change its behavior. The code provided is a basic starting point, and you can extend it to suit your needs.

## Contributions

Contributions to this voice assistant project are welcome! Feel free to submit issues or pull requests to improve its functionality or add new features.

## License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy using your voice assistant! If you have any questions or encounter any issues, please feel free to reach out for assistance.
