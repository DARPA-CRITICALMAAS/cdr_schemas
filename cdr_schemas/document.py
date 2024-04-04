from typing import Optional

from pydantic import BaseModel, Field


class DocumentProvenance(BaseModel):
    """JSON model for Document Provenance"""

    external_system_name: str = Field(
        ..., description="Name of system storing document"
    )
    external_system_id: str = Field(None, description="The system ID of the document")
    external_system_url: str = Field(
        None, description="Name of system storing document"
    )


class Document(BaseModel):
    """JSON model for user-facing document metadata"""

    id: str = Field(..., description="The internal ID of the document")
    title: str = Field(..., description="Title of the document")
    is_open: bool = Field(
        ...,
        description="Whether document is open or not.",
    )

    pages: Optional[int] = Field(None, description="Document page count")

    provenance: Optional[list[DocumentProvenance]] = Field(
        None, description="provenance list"
    )

    system: str = Field(
        ...,
        description="""
            The name of the system used.
        """,
    )
    system_version: str = Field(
        ...,
        description="""
            The version of the system used.
        """,
    )


class DocumentExtraction(BaseModel):
    """JSON model for user-facing document metadata"""

    id: str | None = Field(None, description="The internal ID of the xtraction")
    document_id: str = Field(None, description="The internal ID of the source document")
    extraction_type: str = Field(
        ..., description="The type of model that produced the extraction"
    )
    extraction_label: str = Field(
        ..., description="The classification of the extraction within its model"
    )
    score: float | None = Field(None, description="The confidence of the extraction")
    bbox: tuple[float, float, float, float] | None = Field(
        None, description="The bounding box of the extraction"
    )
    page_num: int | None = Field(None, description="The page number of the extraction")
    external_link: str | None = Field(None, description="A link to the extraction")
    data: dict | None = Field(
        None, description="Extra information about the extraction"
    )

    system: str = Field(
        ...,
        description="""
            The name of the system used.
        """,
    )
    system_version: str = Field(
        ...,
        description="""
            The version of the system used.
        """,
    )
