from typing import List, Union, Optional
from enum import Enum

from pydantic import BaseModel, Field
from common import GeomType


class AreaType(str, Enum):
    Map_Area = "map_area"
    Legend_Area = "legend_area"
    CrossSection = "cross_section"
    OCR = "ocr"


class Area_Extraction(BaseModel):
    type: GeomType = GeomType.Polygon
    coordinates: List[List[List[Union[float, int]]]]
    bounds: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the area. 
        Column value from left, row value from bottom."""
    )
    category: str[AreaType]
    text: Optional[str] = Field(
        ...,
        description="""
            The text within the extraction area.
        """,
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )
