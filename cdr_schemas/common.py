from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"

class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"

class ModelProvenance(BaseModel):
    model: Optional[str] = Field(
        default=None,
        description="Name of the model used to generate this data")
    model_version: Optional[str] = Field(
        default=None,
        description="Version of the model used to generate this data")
    model_config = ConfigDict(protected_namespaces=())
    confidence: Optional[float] = Field(
        default=None,
        description="The prediction confidence of the model")
