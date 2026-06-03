from uuid import uuid4

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from models.chat import ChatRequest

from services.storage_service import StorageService
from services.search_service import SearchService
from services.openai_service import OpenAIService
from services.document_parser import DocumentParser

router = APIRouter()

# Initialize Services
storage_service = StorageService()
search_service = SearchService()
openai_service = OpenAIService()
document_parser = DocumentParser()


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

    content_text = document_parser.extract_text(
        file.filename,
        content
    )

    search_service.upload_document(
        document_id=str(uuid4()),
        file_name=file.filename,
        content=content_text
    )

    return {
        "status": "indexed",
        "file_name": file.filename,
        "content_length": len(content_text)
    }


@router.post("/chat")
def chat(
    request: ChatRequest
):

    documents = search_service.search_documents(
        request.question
    )

    if not documents:

        return {
            "question": request.question,
            "answer": (
                "I could not find the answer in the indexed documents."
            ),
            "sources": []
        }

    context = "\n\n".join(
        [
            f"Source: {doc['file_name']}\n"
            f"Content: {doc['content']}"
            for doc in documents
        ]
    )

    prompt = f"""
You are an Enterprise AI Knowledge Assistant.

IMPORTANT RULES:

1. Answer ONLY using the provided context.
2. Do NOT use your general knowledge.
3. If the answer is not present in the context, respond:

   "I could not find the answer in the indexed documents."

4. Cite the source document when possible.

Context:

{context}

Question:

{request.question}
"""

    answer = openai_service.generate_response(
        prompt
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": [
            doc["file_name"]
            for doc in documents
        ]
    }


@router.get("/health")
def health_check():

    return {
        "status": "healthy"
    }
