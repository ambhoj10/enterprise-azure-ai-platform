from azure.storage.blob import BlobServiceClient
from app.config import settings


class StorageService:

    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )

        self.container_name = settings.AZURE_STORAGE_CONTAINER

    def upload_file(self, file_name, file_data):

        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name,
            blob=file_name
        )

        blob_client.upload_blob(
            file_data,
            overwrite=True
        )

        return {
            "file_name": file_name,
            "container": self.container_name,
            "status": "uploaded"
        }
