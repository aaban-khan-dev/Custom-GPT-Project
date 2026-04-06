import os
from groq import Groq
from logger import logger
from dotenv import load_dotenv

class GroqClient:
    def __init__(self,model = "qwen/qwen3-32b"):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        self.client = Groq(api_key = self.api_key)
        self.logger = logger
        self.model = model

    def get_response(self,message,model = None):
        """
        Name: get_response
        Description: This function takes a message as input and returns a response from the Groq API.
        return : AI response as a string

        """

        try:

            model_to_use = model or self.model
            
            self.logger.info("Sending message to Groq API")

            if isinstance(message,str):
                message = [{"role": "user", "content": message}]

            chat_completion = self.client.chat.completions.create(
                messages = message,
                model = model_to_use
            )
            
            response = chat_completion.choices[0].message.content
            self.logger.info("Received response from Groq API")
            return response
        
        except Exception as e:
            self.logger.error(f"error communicating with Groq AI: {e}")
            return "Sorry, I'm having trouble connecting to the Groq API right now. Please try again later."
        
        