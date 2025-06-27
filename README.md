# Instagram Profile Bot

## Description
This Python script uses Selenium to automate logging into Instagram, navigating to a specific profile, following it, and extracting key information. To appear more like a regular user, the bot incorporates randomized delays between actions.

## ⚠️ Important Disclaimer
**This tool is for educational purposes only.**
- Please ensure you comply with Instagram's Terms of Service.
- Use responsibly. Automated interactions may violate Instagram's policies.
- The creator is not responsible for any account restrictions that may occur.

## Features
- **Secure Automated Login**: Logs in using credentials stored in a `.env` file.
- **Profile Following**: Navigates to a predefined profile and follows it if not already following.
- **Data Extraction**: Scrapes the profile's username, bio, and statistics (posts, followers, and following).
- **Human-Like Delays**: Uses randomized delays between actions to mimic human behavior and avoid detection.
- **Data Export**: Saves the extracted data to a text file.

## Setup

### 1. Dependencies
Install the required Python libraries:
```bash
pip install selenium python-dotenv
```
You will also need a webdriver compatible with your browser (e.g., ChromeDriver for Google Chrome).

### 2. Credentials
Create a `.env` file in the `instagram_automation` directory and add your Instagram credentials:
```
INSTAGRAM_USERNAME="your_username"
INSTAGRAM_PASSWORD="your_password"
```

## Usage
To run the bot, execute the script from within the `instagram_automation` directory:
```bash
python instagram_bot.py
```
The bot will log in, perform the actions, and create a `cbitosc_profile.txt` file with the extracted data.

## Output File
The script generates a `cbitosc_profile.txt` file with the following structure:
```
username: cbitosc
bio: Bio not found
posts: 89 posts
followers: 2,117 followers
following: 10 following
