from pydantic import BaseModel


class Document(BaseModel):

    id: str

    file_name: str

    content: str
