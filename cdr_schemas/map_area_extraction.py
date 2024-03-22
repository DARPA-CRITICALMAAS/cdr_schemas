from typing import List, Union, Optional
from enum import Enum

from pydantic import BaseModel
from common import GeomType


class MapAreaType(str, Enum):
    Map_Area = "map_area"
    Legend_Area = "legend_area"
    CrossSection = "cross_section"
    OCR = "ocr"


class Map_Area_Extraction(BaseModel):
    coordinates: List[List[List[Union[float, int]]]]
    type: GeomType = GeomType.Polygon
    category: str[MapAreaType]
    text: Optional[str]
