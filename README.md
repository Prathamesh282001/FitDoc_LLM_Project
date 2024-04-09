# LLM Nutrition and Workout Bot

## 1. Introduction

The LLM (Language Model) Nutrition and Workout Bot is an AI-powered chatbot designed to provide nutrition and workout recommendations based on user queries. The bot leverages OpenAI's GPT-3.5 model for natural language understanding and generation.

## 2. Features

- Provides nutrition advice and workout recommendations based on user queries.
- Retrieves data from API Ninjas' nutrition and exercise APIs.
- Generates responses in a conversational format.

## 3. Architecture Overview

The project consists of three main components:

- `app.py`: This file contains the main script for the chatbot. It handles user interactions and calls the necessary functions to retrieve and generate responses.
- `llm.py`: This module interacts with the OpenAI GPT-3.5 model and formulates prompts based on the context and user questions.
- `prompt.py`: Provides a function to generate a prompt template for the GPT-3.5 model.

## 4. Usage

To use the LLM Nutrition and Workout Bot:

1. Ensure you have the necessary dependencies installed (see Dependencies section).
2. Run the `app.py` script.
3. Interact with the bot by asking nutrition or workout-related questions.
4. Receive responses tailored to your query.

## 5. Dependencies

The project requires the following dependencies:

- Python 3.x
- `openai` library
- `requests` library
- `chainlit` library
You can install these dependencies using `pip`:

```
pip install
```

## 6. Future Improvements

- Offer diet recommendations tailored to user-specific data such as gender, weight, height, fitness goals, and allergies.

## Libraries & Tools used

1. Python
2. GooglePalm
3. API Ninjas
4. Jupyter notebook as IDE

![Screenshot (25)](https://github.com/Prathamesh282001/FitDoc_LLM_Project/assets/122107260/fba93d63-bd9a-4026-9060-339dfd959cc6)

![Screenshot (26)](https://github.com/Prathamesh282001/FitDoc_LLM_Project/assets/122107260/4538b2b4-c7d4-4992-a892-71651715271e)

![Screenshot (27)](https://github.com/Prathamesh282001/FitDoc_LLM_Project/assets/122107260/fbefd761-b4e1-440e-a265-a2809d8f77eb)

