from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union
from cdr_schemas.features.polygon_features import Polygon

class LegendItem(BaseModel):
    legend_id: str = Field(default="", description="CDR Legend ID")
    abbreviation: str = Field(default="", description="Abbreviation of legend item")
    description: str = Field(default="", description="Legend item description")
    px_bbox: List[Union[float, int]]
    color: str = Field(default="", description="Color")
    reference_id: Union[str,None] = Field(default=None, description="Legend id of older version of this legend item.")
    label: str= Field(default="", description="Label of legend item")
    pattern: str = Field(default="", description="If category polygon, this can be filled in with pattern type")
    px_geojson: Polygon
    cog_id: str = Field(default="", description="Cog id")
    category: str = Field(default="", description="Category of legend item. Polygon, point, or line.")
    system: str = Field(default="", description="System that published this item")
    system_version: str = Field(default="", description="System Version that published this item")
    model_id: str = Field(default="", description="CDR Model ID for the model used to generate this item")
    validated: bool= Field(default=False, description="Validated by human")
    confidence: Optional[float]=None
    map_unit_age_text: str = Field(default="", description="Age of Map Unit")
    map_unit_lithology: str = Field(default="", description="Map Unit lithology")
    map_unit_b_age: Optional[float]=None
    map_unit_t_age: Optional[float]=None

class LegendItemsResponse(BaseModel):
    legend_items: Optional[List[LegendItem]]