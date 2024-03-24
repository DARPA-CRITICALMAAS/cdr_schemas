from enum import Enum
from typing import Type, List
from pydantic import BaseModel

class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"

class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"

class Contour(BaseModel):
    geometry : List[List[float]]
