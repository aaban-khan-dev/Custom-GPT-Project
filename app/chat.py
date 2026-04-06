from .api_client import GroqClient

class ChatManager:

    def __init__(self):
        self.client = GroqClient()
        self.conversation_history = []

    
    def add_message(self,role,content):
        
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def get_response(self,user_message,model = None):
        """
        Name: get_response
        Description: Get concise or detailed response based on user input
        return : response from groq client

        """
        user_message_lower = user_message.lower()

        if any(keyword in user_message_lower for keyword in ["what is","define"]):
            prompt = f"provide concise definition of: {user_message}"
        
        elif "explain" in user_message_lower:
            prompt = f"provide detailed explanation with examples of: {user_message}"
        
        elif "code" in user_message_lower():
            prompt = f"provide code example for: {user_message}"

        elif "compare" in user_message_lower():
            prompt = f"compare and contrast: {user_message}"
        
        else:
            prompt = f"Respond concisely to: {user_message}"

        self.add_message("user", prompt)

        ai_response = self.client.get_response(self.conversation_history, model = model)

        self.add_message("assistant", ai_response)

        return ai_response
        