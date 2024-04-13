from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.common import GeoJsonType, GeomType


class Polygon(BaseModel):
    """
    coordinates in line are  (column from left, row from bottom).
    """

    coordinates: List[List[List[Union[float, int]]]]
    type: GeomType = GeomType.Polygon


class PolygonProperty(BaseModel):
    """
    Properties of the polygon.
    """

    model: Optional[str] = Field(
        default=None, description="Name of the model used for extraction"
    )
    model_version: Optional[str] = Field(
        default=None, description="Version of the model used for extraction"
    )
    confidence: Optional[float] = Field(
        default=None, description="The prediction confidence of the model"
    )

    model_config = ConfigDict(protected_namespaces=())


class PolygonFeature(BaseModel):
    """
    Polygon feature.
    """

    type: GeoJsonType = GeoJsonType.Feature
    id: str = Field(
        description="""Each polygon geometry has a unique id.
                The ids are used to link the polygon geometries is px-coord and geo-coord."""
    )
    geometry: Polygon
    properties: PolygonProperty


class PolygonFeatureCollection(BaseModel):
    """
    All polygon features for legend item.
    """

    type: GeoJsonType = GeoJsonType.FeatureCollection
    features: Optional[List[PolygonFeature]] = None


class MapUnit(BaseModel):
    """
    Map unit information for legend item.
    """

    # TODO Add details on what these fields are / are we keeping them
    age_text: Optional[str] = None
    b_age: Optional[float] = None
    b_interval: Optional[str] = None
    lithology: Optional[str] = None
    name: Optional[str] = None
    t_age: Optional[float] = None
    t_interval: Optional[str] = None
    comments: Optional[str] = None


class PolygonLegendAndFeatureResult(BaseModel):
    """
    Polygon map unit metadata along with associated polygon segmentation found.
    """

    id: str = Field(description="your internal id")

    # Legend Fields
    label: Optional[str] = Field(default=None, description="Label of the map unit")
    abbreviation: Optional[str] = Field(
        default=None, description="Abbreviation of the map unit label."
    )
    description: Optional[str] = Field(
        default=None, description="Description of the map unit"
    )
    legend_bbox: Optional[List[List[Union[float, int]]]] = Field(
        default=None, description="The bounding box of the map units label."
    )
    color: Optional[str] = Field(default=None, description="The color of the map unit")
    pattern: Optional[str] = Field(
        default=None, description="The pattern of the map unit"
    )
    category: Optional[str] = Field(
        default=None, description="TODO - what is this?"
    )  ### TODO
    map_unit: Optional[MapUnit] = Field(
        default=None, description="Human annotated information on the mab unit"
    )

    # Segmentation Fields
    crs: Optional[str] = Field(
        default=None, description="values={CRITICALMAAS:pixel, EPSG:*}"
    )
    cdr_projection_id: Optional[str] = Field(
        default=None,
        description="A cdr projection id used to georeference the features",
    )  ### TODO Could use some more explanation
    polygon_features: Optional[PolygonFeatureCollection] = Field(
        default=None, description="All polygon features for legend item."
    )
