from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour, Provenance

class TextUnit(BaseModel):
    """Sub-field of OCRTextSchema, describes an individual text unit from the map"""
    label : str
    geometry : Contour
    confidence : Optional[float]

class OCRTextSchema(BaseModel):
    """Schema for results of OCR text extraction from a map"""
    provenance : Provenance

    # Data
    features : List[TextUnit]