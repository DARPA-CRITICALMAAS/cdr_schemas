from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.common import (
    CRITICALMAAS_PIXEL,
    GeoJsonType,
    GeomType,
    ModelProvenance,
)


class Polygon(BaseModel):
    """
    Individual polygon segmentation of a polygon feature.
    """

    coordinates: List[List[List[Union[float, int]]]] = Field(
        description="""The coordinates of the polygon. Format is expected to
                    be [x,y] coordinate pairs where the top left is the origin
                    (0,0)."""
    )
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
    confidence: Optional[Union[float | int]] = Field(
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

    # TODO Someone needs to add full descriptions to these fields
    age_text: Optional[str] = None
    b_age: Optional[float] = None
    b_interval: Optional[str] = None
    lithology: Optional[str] = None
    name: Optional[str] = None
    t_age: Optional[float] = None
    t_interval: Optional[str] = None
    comments: Optional[str] = None


class PolygonLegendAndFeaturesResult(BaseModel):
    """
    Polygon map unit metadata along with associated polygon segmentation found.
    """

    id: str = Field(description="your internal id")

    # Legend Fields
    # TODO move to a more sensible location
    legend_provenance: Optional[ModelProvenance] = Field(
        default=None, description="Where the data originated from."
    )
    label: Optional[str] = Field(default=None, description="Label of the map unit")
    abbreviation: Optional[str] = Field(
        default=None, description="Abbreviation of the map unit label."
    )
    description: Optional[str] = Field(
        default=None, description="Description of the map unit"
    )
    legend_bbox: Optional[List[Union[float, int]]] = Field(
        default=None,
        description="""The rough 2 point bounding box of the map units label.
                    Format is expected to be [x1,y1,x2,y2] where the top left
                    is the origin (0,0).""",
    )
    legend_contour: Optional[List[List[Union[float, int]]]] = Field(
        default=None,
        description="""The more precise polygon bounding box of the map units
                    label. Format is expected to be [x,y] coordinate pairs
                    where the top left is the origin (0,0).""",
    )
    color: Optional[str] = Field(default=None, description="The color of the map unit")
    pattern: Optional[str] = Field(
        default=None, description="The pattern of the map unit"
    )
    ### TODO Agreed on Apr 15th call that category can be removed
    category: Optional[str] = Field(default=None, description="TODO - what is this?")
    map_unit: Optional[MapUnit] = Field(
        default=None, description="Human annotated information on the map unit"
    )

    # Segmentation Fields
    crs: Optional[str] = Field(
        default=CRITICALMAAS_PIXEL,
        description="""What projection the geometry of the segmentation are in,
                    Default is CRITICALMAAS_PIXEL which specifies pixel coordinates.
                    Possible values are {CRITICALMAAS_PIXEL, EPSG:*}""",
    )
    cdr_projection_id: Optional[str] = Field(
        default=None,
        description="""If non-pixel coordinates are used the cdr projection id of the
                    georeference that was used to create them is required.""",
    )
    polygon_features: Optional[PolygonFeatureCollection] = Field(
        default=None, description="All polygon features for legend item."
    )
