from typing import List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict
from cdr_schemas.common import GeomType, GeoJsonType


class Polygon(BaseModel):
    """
    coordinates in line are  (column from left, row from bottom).
    """

    coordinates: List[List[List[Union[float, int]]]]
    type: str = Field(default=GeomType.Polygon)


class PolygonProperty(BaseModel):
    id: str = Field(description="your internal id")
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
    id: str = Field(description="your internal id for map_unit")
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
    Polygon legend item along with associated polygon features found.
    """

    id: int
    map_unit: Optional[MapUnit]
    abbreviation: Optional[str]
    legend_bbox: Optional[List[Union[float, int]]] = Field(
        description="The extacted bounding box of the legend item"
    )
    category: Optional[str]
    color: Optional[str]
    description: Optional[str]
    pattern: Optional[str]
    polygon_features: Optional[PolygonFeatureCollection]
