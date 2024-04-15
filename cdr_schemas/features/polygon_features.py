from typing import List, Optional, Union

from pydantic import BaseModel, Field

from cdr_schemas.common import CRITICALMAAS_PIXEL, ModelProvenance


class Polygon(BaseModel):
    """
    Individual contiguous polygon of a segmentation for a polygon map unit.
    """

    # Provenance
    provenance: ModelProvenance = Field(description="Where the data originated from.")

    # Data
    crs: Optional[str] = Field(
        default=CRITICALMAAS_PIXEL,
        description="""What projection the geometry of the segmentation are in,
                    Default is CRITICALMAAS_PIXEL which specifies pixel coordinates.
                    Possible values are {CRITICALMAAS:pixel, EPSG:*}""",
    )
    cdr_projection_id: Optional[str] = Field(
        default=None,
        description="""If non-pixel coordinates are used the cdr projection id of the
                    georeference that was used to create them is required.""",
    )
    geometry: List[List[Union[float, int]]] = Field(
        description="""The coordinates of polygon. Format is expected to be [x,y]
                    coordinate pairs where the top left is the origin (0,0)."""
    )

    # Why are we returning internal ids for polygons? also when would this ever not be GeomType.Polygon, this is a polygon segmentation
    # geom_type: GeomType = GeomType.Polygon
    # id: str = Field(
    #     description="""Each polygon geometry has a unique id. The ids are used
    #                 to link the polygon geometries is px-coord and geo-coord.""")


class PolygonLegend(BaseModel):
    """
    Legend information for a polygon map unit.
    """

    # Provenance
    provenance: ModelProvenance = Field(description="Where the data originated from.")

    # Data
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
    color: Optional[str] = Field(
        default=None, description="The color of the map unit's legend"
    )
    pattern: Optional[str] = Field(
        default=None, description="The pattern of the map unit's legend"
    )
    overlay: Optional[bool] = Field(
        default=None,
        description="Wheather or not the map unit can be overlayed on other map units",
    )

    # TODO Someone else will need to add full descriptions to these fields
    age_text: Optional[str] = None
    b_age: Optional[float] = None
    b_interval: Optional[str] = None
    lithology: Optional[str] = None
    name: Optional[str] = None
    t_age: Optional[float] = None
    t_interval: Optional[str] = None
    comments: Optional[str] = None

    # Agreed on Apr 15th call that this field can be removed
    # category: Optional[str] = Field(
    #     default=None,
    #     description="what is this?")


class PolygonMapUnit(BaseModel):
    """
    Polygon map unit metadata along with associated polygon segmentation found.
    """

    legend: Optional[PolygonLegend] = Field(
        default=None, description="Legend information for polygon map unit."
    )
    segmentation: Optional[List[Polygon]] = Field(
        default=None,
        description="List of polygons that make up the segmentation for the polygon map unit.",
    )

    # What is this?
    # id: str = Field(description="your internal id")
