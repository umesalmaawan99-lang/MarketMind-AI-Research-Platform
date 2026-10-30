from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL_NAME

class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME

    def chat_completion(self, messages: list, temperature: float = 0.2, response_format=None) -> str:
        """Sends a chat completion request to OpenAI."""
        try:
            kwargs = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
            }
            if response_format:
                kwargs["response_format"] = response_format

            response = self.client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {e}")

# Singleton client instance
llm_client = LLMClient()