from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

# Constant for defining that a projection is in pixel coordinates
CRITICALMAAS_PIXEL = "pixel"


class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"


class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"


class ModelProvenance(BaseModel):
    model: str = Field(description="Name of the model used to generate this data")
    model_version: str = Field(
        description="Version of the model used to generate this data"
    )
    model_config = ConfigDict(protected_namespaces=())
    confidence: Optional[Union[float, int]] = Field(
        default=None, description="The prediction confidence of the model"
    )


class LegendDescription(BaseModel):
    """
    Legend description information.
    Each legend item can have multiple LegendDescriptions that
    combined are all areas and text that describe the legend item.
    """

    text: str = Field(default="", description="Description of the map unit")
    legend_description_bbox: List[Union[float, int]] = Field(
        default_factory=list,
        description="""The rough 2 point bounding boxs of the map units descriptions.
                    Format is expected to be [x1,y1,x2,y2] where the top left
                    is the origin (0,0).""",
    )
    legend_description_contour: List[List[Union[float, int]]] = Field(
        default_factory=list,
        description="""The more precise polygon bounding box of the map units
                    descriptions. Format is expected to be [x,y] coordinate pairs
                    where the top left is the origin (0,0).""",
    )
