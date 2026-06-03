from azure.core.credentials import AzureKeyCredential

from azure.search.documents import SearchClient

from azure.search.documents.indexes import (
    SearchIndexClient
)

from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchFieldDataType
)

from app.config import settings


class SearchService:

    def __init__(self):

        self.index_client = SearchIndexClient(
            endpoint=settings.AZURE_SEARCH_ENDPOINT,
            credential=AzureKeyCredential(
                settings.AZURE_SEARCH_API_KEY
            )
        )

    def create_index(self):

        fields = [
            SimpleField(
                name="id",
                type=SearchFieldDataType.String,
                key=True
            ),
            SimpleField(
                name="file_name",
                type=SearchFieldDataType.String
            ),
            SimpleField(
                name="content",
                type=SearchFieldDataType.String
            )
        ]

        index = SearchIndex(
            name=settings.AZURE_SEARCH_INDEX,
            fields=fields
        )

        self.index_client.create_or_update_index(
            index
        )

        return {
            "index": settings.AZURE_SEARCH_INDEX,
            "status": "created"
        }

    def get_search_client(self):

        return SearchClient(
            endpoint=settings.AZURE_SEARCH_ENDPOINT,
            index_name=settings.AZURE_SEARCH_INDEX,
            credential=AzureKeyCredential(
                settings.AZURE_SEARCH_API_KEY
            )
        )

    def upload_document(
        self,
        document_id,
        file_name,
        content
    ):

        search_client = self.get_search_client()

        documents = [
            {
                "id": document_id,
                "file_name": file_name,
                "content": content
            }
        ]

        result = search_client.upload_documents(
            documents=documents
        )

        return result
