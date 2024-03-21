from typing import List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict
from cdr_schemas.common import GeomType, add_class_name_property
from enum import Enum

class DashType(str, Enum):
    Point = "solid"
    LineString = "dash"
    Polygon = "dotted"


class Line(BaseModel):
    """
    coordinates in line are  (column from left, row from bottom).
    """
    pix_coordinates: List[List[Union[float, int]]]
    geom_coordinates: Optional[List[List[Union[float, int]]]]
    type: str = Field(default=GeomType.LineString)
    

@add_class_name_property
class LineFeature(BaseModel):
    id: str = Field(description="Your internal id")
    geometry: Line
    name: Optional[str] = Field(description="the line feature's name, such as fault line. must align with legend extraction")
    model: Optional[str] = Field(description="model name used for extraction")
    model_version: Optional[str] = Field(description="model version used for extraction")
    direction: Optional[int] = Field(default=0, decription='direction range [0, 360]')
    description: Optional[str]
    dash_type: Optional[DashType] = Field(default=None, description= "values = {solid, dash, dotted}")
    symbol: Optional[str]=None

    model_config = ConfigDict(protected_namespaces=())



@add_class_name_property
class LineFeatureCollection(BaseModel):
    crs: Optional[str] = Field(
        description="""
            If a feature has been georeference and geom_coordinates are filled in this crs should be filled in
            An example: "EPSG:3857"
        """
    )    
    features: Optional[List[LineFeature]]