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
