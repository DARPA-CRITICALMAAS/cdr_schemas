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
    """
    Properties of the polygon.
    """

    id: str = Field(description="your internal id")
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(
        description="model version used for extraction"
    )
    confidence: Optional[float] = Field(
        description="The prediction probability from the ML model"
    )

    model_config = ConfigDict(protected_namespaces=())


class PolygonFeature(BaseModel):
    """
    Polygon feature.
    """

    type: str = GeoJsonType.Feature
    geometry: Polygon
    properties: PolygonProperty


class PolygonFeatureCollection(BaseModel):
    """
    All polygon features for legend item.
    """

    type: GeomType.FeatureCollection
    features: Optional[List[PolygonFeature]]


class MapUnit(BaseModel):
    """
    Map unit information for legend item.
    """

    age_text: Optional[str]
    b_age: Optional[float]
    b_interval: Optional[str]
    description: Optional[str]
    lithology: Optional[str]
    name: Optional[str]
    t_age: Optional[float]
    t_interval: Optional[str]
    comments: Optional[str]


class PolygonLegendAndFeauturesResult(BaseModel):
    """
    Polygon legend item metadata along with associated polygon features found.
    """

    id: str = Field(description="your internal id")
    map_unit: Optional[MapUnit]
    abbreviation: Optional[str]
    legend_bbox: Optional[List[Union[float, int]]] = Field(
        description="""The extacted bounding box of the legend item. 
        Column value from left, row value from bottom."""
    )
    category: Optional[str]
    color: Optional[str]
    description: Optional[str]
    pattern: Optional[str]
    polygon_features: Optional[PolygonFeatureCollection]