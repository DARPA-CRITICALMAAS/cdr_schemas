from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.common import GeomType


class AreaType(str, Enum):
    Map_Area = "Map_Area"
    Legend_Area = "Legend_Area"
    CrossSection = "CrossSection"
    OCR = "OCR"
    Polygon_Legend_Area = "Polygon_Legend_Area"
    Line_Point_Legend_Area = "Line_Point_Legend_Area"
    Line_Legend_Area = "Line_Legend_Area"
    Point_Legend_Area = "Point_Legend_Area"
    Correlation_Diagram = "Correlation_Diagram"


class Area_Extraction(BaseModel):
    """
    Area extraction of a cog.
    """

    type: GeomType = GeomType.Polygon
    coordinates: List[List[List[Union[float, int]]]]
    bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the area.
        Column value from left, row value from bottom."""
    )
    category: AreaType = Field(
        ...,
        description="""
            The type of area extraction.
        """,
    )
    text: Optional[str] = Field(
        ...,
        description="""
            The text within the extraction area.
        """,
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )

    model_config = ConfigDict(protected_namespaces=())
