from enum import Enum
from typing import Type, List
from pydantic import BaseModel, Field

SCHEMA_VERSION_NUMBER = "1.6"

class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"

class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"

class Contour(BaseModel):
    geometry : List[List[float]]

class Provenance(BaseModel):
    version : str = Field(description="Version number of the schema", default=SCHEMA_VERSION_NUMBER)
    map_name : str = Field(description="Identifier of the map that this data was extracted from. AKA name of the map")
    model : str = Field(description="Name of the model that was used to generate this data.")
    model_version : str = Field(description="Version number of the model used to generate this data.")