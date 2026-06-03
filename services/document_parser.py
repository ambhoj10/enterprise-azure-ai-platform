from pypdf import PdfReader


class DocumentParser:

    def extract_text(
        self,
        file_name,
        file_content
    ):

        if file_name.lower().endswith(".txt"):

            return file_content.decode(
                "utf-8",
                errors="ignore"
            )

        if file_name.lower().endswith(".pdf"):

            return self._extract_pdf_text(
                file_content
            )

        raise ValueError(
            f"Unsupported file type: {file_name}"
        )

    def _extract_pdf_text(
        self,
        file_content
    ):

        import io

        pdf_stream = io.BytesIO(
            file_content
        )

        reader = PdfReader(
            pdf_stream
        )

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text
