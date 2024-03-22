from typing import List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict
from cdr_schemas.common import GeomType, add_class_name_property, GeoJsonType
from enum import Enum


class DashType(str, Enum):
    Point = "solid"
    LineString = "dash"
    Polygon = "dotted"


class Line(BaseModel):
    """
    coordinates in line are  (column from left, row from bottom).
    """

    coordinates: List[List[Union[float, int]]]
    type: str = Field(default=GeomType.LineString)


class LineProperty(BaseModel):
    id: str = Field(description="your internal id")
    model: str = Field(description="model name used for extraction")
    model_version: str = Field(description="model version used for extraction")
    description: Optional[str]
    symbol: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())


@add_class_name_property
class LineFeature(BaseModel):
    type: str = GeomType.Feature
    geometry: Line
    properties: LineProperty


@add_class_name_property
class LineFeatureCollection(BaseModel):
    type: GeomType.FeatureCollection
    features: Optional[List[LineFeature]]


class LineFeatureResult(BaseModel):
    id: int
    name: Optional[str]
    dash_pattern: Optional[DashType] = Field(
        default=None, description="values = {solid, dash, dotted}"
    )
    description: Optional[str]
    symbol: Optional[str]

    line_features: Optional[LineFeatureCollection]
