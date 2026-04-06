import os
from groq import Groq
from logger import logger
from dotenv import load_dotenv


class GroqClient:
    def __init__(self, model="qwen/qwen3-32b"):
        load_dotenv()

        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.client = Groq(api_key=self.api_key)
        self.logger = logger
        self.model = model

    def get_response(self, message, model=None):
        """
        Send message(s) to Groq API and return response
        """

        try:
            model_to_use = model or self.model

            # ensure correct format
            if isinstance(message, str):
                message = [{"role": "user", "content": message}]

            if not isinstance(message, list):
                raise ValueError("Message must be a string or list of dicts")

            self.logger.info(
                f"Sending request to Groq API | model={model_to_use} | messages={len(message)}"
            )

            chat_completion = self.client.chat.completions.create(
                messages=message,
                model=model_to_use
            )

            response = chat_completion.choices[0].message.content

            self.logger.info("Received response from Groq API")

            return response

        except Exception as e:
            self.logger.exception("Error communicating with Groq AI")
            return "Sorry, I'm having trouble connecting to the Groq API right now. Please try again later."