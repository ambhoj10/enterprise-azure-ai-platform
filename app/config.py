from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_DEPLOYMENT: str

    # Azure AI Search
    AZURE_SEARCH_ENDPOINT: str
    AZURE_SEARCH_API_KEY: str
    AZURE_SEARCH_INDEX: str

    # Azure Storage
    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER: str

    # Application Insights
    APPLICATIONINSIGHTS_CONNECTION_STRING: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
