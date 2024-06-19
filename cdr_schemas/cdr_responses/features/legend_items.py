from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field

from cdr_schemas.features.polygon_features import Polygon


class ProjectedFeature(BaseModel):
    cdr_projection_id: str = Field(description="CDR Projection id used for transform.")
    feature_type: str = Field(description="Feature type. polygon, point, line")
    projected_geojson: Optional[Polygon] = Field(
        description="Projected polygon geojson in EPSG 4326"
    )
    projected_bbox: Optional[Polygon] = Field(description="Projected bbox in EPSG 4326")


class PolygonExtractionResponse(BaseModel):
    polygon_id: str = Field(default="", description="CDR Polygon ID")
    cog_id: str = Field(default="", description="Cog ID")
    px_bbox: List[Union[float, int]]
    px_geojson: Polygon
    reference_id: Union[str, None] = Field(
        default=None, description="Polygon id of older version of this polygon."
    )
    confidence: Optional[float] = None
    model_id: str = Field(
        default="", description="CDR Model ID for the model used to generate this item"
    )
    system: str = Field(default="", description="System that published this item")
    system_version: str = Field(
        default="", description="System Version that published this item"
    )
    validated: bool = Field(default=False, description="Validated by human")
    legend_id: str = Field(default="", description="Associated CDR Legend ID")
    projected_feature: Optional[List[ProjectedFeature]]
    legend_item: Optional[Any] = Field(
        default=None,
        description="Some cdr endpoints can allow a legend item data attached to each feature.",
    )


class PointExtractionResponse(BaseModel):
    point_id: str = Field(default="", description="CDR Point ID")
    cog_id: str = Field(default="", description="Cog ID")
    px_bbox: List[Union[float, int]]
    px_geojson: Polygon
    dip: Optional[Union[int, None]] = Field(
        default=None, description="Point dip value."
    )
    dip_direction: Optional[Union[int, None]] = Field(
        default=None, description="Point dip direction value."
    )
    reference_id: Union[str, None] = Field(
        default=None, description="Point id of older version of this point."
    )
    confidence: Optional[float] = None
    model_id: str = Field(
        default="", description="CDR Model ID for the model used to generate this item"
    )
    system: str = Field(default="", description="System that published this item")
    system_version: str = Field(
        default="", description="System Version that published this item"
    )
    validated: bool = Field(default=False, description="Validated by human")
    legend_id: str = Field(default="", description="Associated CDR Legend ID")
    projected_feature: Optional[List[ProjectedFeature]]
    legend_item: Optional[Any] = Field(
        default=None,
        description="Some cdr endpoints can allow a legend item data attached to each feature.",
    )


class LineExtractionResponse(BaseModel):
    line_id: str = Field(default="", description="CDR Line ID")
    cog_id: str = Field(default="", description="Cog ID")
    px_bbox: List[Union[float, int]]
    px_geojson: Polygon
    dash_pattern: str = Field(default="", description="Dash pattern of line")
    symbol: str = Field(default="", description="symbol on line")
    reference_id: Union[str, None] = Field(
        default=None, description="Line id of older version of this line."
    )
    confidence: Optional[float] = None
    model_id: str = Field(
        default="", description="CDR Model ID for the model used to generate this item"
    )
    system: str = Field(default="", description="System that published this item")
    system_version: str = Field(
        default="", description="System Version that published this item"
    )
    validated: bool = Field(default=False, description="Validated by human")
    legend_id: str = Field(default="", description="Associated CDR Legend ID")
    projected_feature: Optional[List[ProjectedFeature]]
    legend_item: Optional[Any] = Field(
        default=None,
        description="Some cdr endpoints can allow a legend item data attached to each feature.",
    )


class LegendItemResponse(BaseModel):
    legend_id: str = Field(default="", description="CDR Legend ID")
    abbreviation: str = Field(default="", description="Abbreviation of legend item")
    description: str = Field(default="", description="Legend item description")
    px_bbox: List[Union[float, int]]
    color: str = Field(default="", description="Color")
    reference_id: Union[str, None] = Field(
        default=None, description="Legend id of older version of this legend item."
    )
    label: str = Field(default="", description="Label of legend item")
    pattern: str = Field(
        default="",
        description="If category polygon, this can be filled in with pattern type",
    )
    px_geojson: Polygon
    cog_id: str = Field(default="", description="Cog id")
    category: str = Field(
        default="", description="Category of legend item. Polygon, point, or line."
    )
    system: str = Field(default="", description="System that published this item")
    system_version: str = Field(
        default="", description="System Version that published this item"
    )
    model_id: str = Field(
        default="", description="CDR Model ID for the model used to generate this item"
    )
    validated: bool = Field(default=False, description="Validated by human")
    confidence: Optional[float] = None
    map_unit_age_text: str = Field(default="", description="Age of Map Unit")
    map_unit_lithology: str = Field(default="", description="Map Unit lithology")
    map_unit_b_age: Optional[float] = None
    map_unit_t_age: Optional[float] = None

    point_extractions: List[PointExtractionResponse] = Field(
        default_factory=list,
        description="Optionally added point extractions associated with this legend item",
    )
    polygon_extractions: List[PolygonExtractionResponse] = Field(
        default_factory=list,
        description="Optionally added polygon extractions associated with this legend item",
    )
    line_extractions: List[LineExtractionResponse] = Field(
        default_factory=list,
        description="Optionally added line extractions associated with this legend item",
    )
