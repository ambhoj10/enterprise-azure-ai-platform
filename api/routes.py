from uuid import uuid4

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.storage_service import StorageService
from services.search_service import SearchService

router = APIRouter()

# Initialize Services
storage_service = StorageService()
search_service = SearchService()


@router.get("/")
def api_root():
    return {
        "message": "Enterprise Azure AI Platform API"
    }


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    content = await file.read()

    result = storage_service.upload_file(
        file.filename,
        content
    )

    return result


@router.post("/search/index")
def create_search_index():

    return search_service.create_index()


@router.post("/search/document")
async def upload_document_to_search(
    file: UploadFile = File(...)
):

    content = await file.read()

    content_text = content.decode(
        "utf-8",
        errors="ignore"
    )

    search_service.upload_document(
        document_id=str(uuid4()),
        file_name=file.filename,
        content=content_text
    )

    return {
        "status": "indexed",
        "file_name": file.filename
    }
