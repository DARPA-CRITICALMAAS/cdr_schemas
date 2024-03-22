from typing import List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict
from cdr_schemas.common import GeomType, GeoJsonType


class Polygon(BaseModel):
    """
    coordinates in polygon are (col, row).
    """

    coordinates: List[List[List[Union[float, int]]]]
    type: str = Field(default=GeomType.Polygon)


class PolygonProperty(BaseModel):
    id: str = Field(description="Your internal id")
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )

    model_config = ConfigDict(protected_namespaces=())


class PolygonFeature(BaseModel):
    type: str = GeoJsonType.Feature
    geometry: Polygon
    properties: PolygonProperty


class PolygonFeatureCollection(BaseModel):
    type: GeomType.FeatureCollection
    features: Optional[List[PolygonFeature]]


class MapUnit(BaseModel):
    id: int
    age_text: Optional[str]
    b_age: Optional[float]
    b_interval: Optional[str]
    description: Optional[str]
    lithology: Optional[str]
    name: Optional[str]
    t_age: Optional[float]
    t_interval: Optional[str]
    comments: Optional[str]


class PolygonFeautureResult(BaseModel):
    """
    Legend item along with associated polygon features found.
    """

    id: int
    map_unit: Optional[MapUnit]
    abbreviation: Optional[str]
    category: Optional[str]
    color: Optional[str]
    description: Optional[str]
    pattern: Optional[str]
    polygon_features: Optional[PolygonFeatureCollection]
