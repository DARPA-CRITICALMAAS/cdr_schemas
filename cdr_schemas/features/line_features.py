from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.common import (
    CRITICALMAAS_PIXEL,
    GeoJsonType,
    GeomType,
    ModelProvenance,
)


class DashType(str, Enum):
    solid = "solid"
    dash = "dash"
    dotted = "dotted"


class Line(BaseModel):
    """
    Individual line segmentation of a line feature.
    """

    coordinates: List[List[Union[float, int]]] = Field(
        description="""The coordinates of the line. Format is expected to
                    be [x,y] coordinate pairs where the top left is the origin
                    (0,0)."""
    )
    type: GeomType = GeomType.LineString


class LineProperty(BaseModel):
    """
    Properties of the line.
    """

    # Model Provenance
    model: Optional[str] = Field(
        default=None, description="Name of the model used to generate this data"
    )
    model_version: Optional[str] = Field(
        default=None, description="Version of the model used to generate this data"
    )
    model_config = ConfigDict(protected_namespaces=())
    confidence: Optional[Union[float | int]] = Field(
        default=None, description="The prediction confidence of the model"
    )

    # Line Properties
    dash_pattern: Optional[DashType] = Field(
        default=None, description="values = {solid, dash, dotted}"
    )
    symbol: Optional[str] = Field(  # TODO add description
        default=None, description="TODO : Add description"
    )


class LineFeature(BaseModel):
    """
    Line Feature.
    """

    type: GeoJsonType = GeoJsonType.Feature
    id: str = Field(
        description="""Each line geometry has a unique id.
                    The ids are used to link the line geometries is px-coord and geo-coord."""
    )
    geometry: Line
    properties: LineProperty


class LineFeatureCollection(BaseModel):
    """
    All line features for legend item.
    """

    type: GeoJsonType = GeoJsonType.FeatureCollection
    features: Optional[List[LineFeature]] = None


class LineLegendAndFeaturesResult(BaseModel):
    """
    Line legend item with metadata and associated line features found.
    """

    id: str = Field(description="your internal id")

    # Legend Fields
    # TODO move to a more sensible location
    legend_provenance: Optional[ModelProvenance] = Field(
        default=None, description="Where the data originated from."
    )
    name: Optional[str] = Field(
        default=None, description="Label of the map unit in the legend"
    )
    abbreviation: Optional[str] = Field(
        default=None, description="Abbreviation of the map unit label."
    )
    description: Optional[str] = Field(
        default=None, description="Description of the map unit in the legend"
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
    line_features: Optional[LineFeatureCollection] = None
