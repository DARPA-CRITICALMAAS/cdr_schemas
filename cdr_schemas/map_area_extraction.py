from typing import List, Union
from enum import Enum

from pydantic import BaseModel
from common import GeomType


class MapAreaType(str, Enum):
    Map_Area = "map_area"
    Legend_Area = "legend_area"
    CrossSection = "cross_section"


class Map_Area(BaseModel):
    coordinates: List[List[List[Union[float, int]]]]
    type: GeomType = GeomType.Polygon
    category: str[MapAreaType]
