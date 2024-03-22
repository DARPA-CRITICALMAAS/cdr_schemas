from typing import List, Union, Any, Optional
from pydantic import BaseModel, Field
from cdr_schemas.common import GeomType, GeoJsonType


class Point(BaseModel):
    """
    coordinates in line are (column from left, row from bottom).
    """

    coordinates: List[Union[float, int]]
    type: str = Field(default=GeomType.Point)


class PointProperties(BaseModel):
    id: str
    model: str = Field(description="model name used for extraction")
    model_version: str = Field(description="model version used for extraction")
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )
    bbox: Optional[List[Union[float, int]]] = Field(
        description="The extacted bounding box from the ML model"
    )
    dip: Optional[int]
    dip_direction: Optional[int]


class PointFeature(BaseModel):
    type: GeoJsonType.Feature
    geometry: Point
    properties: PointProperties


class PointFeatureCollection(BaseModel):
    type: GeoJsonType.FeatureCollection
    features: List[PointFeature]


class PointFeatureResult(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    point_features: Optional[List[PointFeatureCollection]]
