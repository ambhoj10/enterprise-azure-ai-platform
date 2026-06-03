from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # Azure OpenAI

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    AZURE_OPENAI_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    )

    # Azure AI Search

    AZURE_SEARCH_ENDPOINT = os.getenv(
        "AZURE_SEARCH_ENDPOINT"
    )

    AZURE_SEARCH_API_KEY = os.getenv(
        "AZURE_SEARCH_API_KEY"
    )

    AZURE_SEARCH_INDEX = os.getenv(
        "AZURE_SEARCH_INDEX"
    )

    # Azure Storage

    AZURE_STORAGE_CONNECTION_STRING = os.getenv(
        "AZURE_STORAGE_CONNECTION_STRING"
    )

    AZURE_STORAGE_CONTAINER = os.getenv(
        "AZURE_STORAGE_CONTAINER"
    )

    # Application Insights

    APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv(
        "APPLICATIONINSIGHTS_CONNECTION_STRING"
    )


settings = Settings()
