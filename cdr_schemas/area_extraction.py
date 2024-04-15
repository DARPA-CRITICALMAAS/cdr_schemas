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
    coordinates: List[List[List[Union[float, int]]]] = Field(
        description="""The coordinates of the areas boundry. Format is expected
                    to be [x,y] coordinate pairs where the top left is the
                    origin (0,0)."""
    )
    bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extracted bounding box of the area.
                    Format is expected to be [x1,y1,x2,y2] where the top left
                    is the origin (0,0).""",
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

    # Model Provenance
    model: Optional[str] = Field(
        default=None, description="Name of the model used to generate this data"
    )
    model_version: Optional[str] = Field(
        default=None, description="Version of the model used to generate this data"
    )
    model_config = ConfigDict(protected_namespaces=())
    confidence: Optional[float] = Field(
        default=None, description="The prediction confidence of the model"
    )
