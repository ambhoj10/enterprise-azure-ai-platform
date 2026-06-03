from openai import AzureOpenAI

from app.config import settings


class OpenAIService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version="2024-02-15-preview",
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
        )

    def generate_response(
        self,
        prompt
    ):

        response = self.client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an enterprise AI assistant."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
