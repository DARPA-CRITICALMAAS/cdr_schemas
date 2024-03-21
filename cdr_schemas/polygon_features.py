from typing import List, Optional, Union
from pydantic import BaseModel, Field
from cdr_schemas.common import GeomType, add_class_name_property
from enum import Enum

class Polygon(BaseModel):
    """
    coordinates in polygon are (col, row).
    """
    pix_coordinates: List[List[List[Union[float, int]]]]
    geom_coordinates: Optional[List[List[List[Union[float, int]]]]]
    type: str = Field(default=GeomType.Polygon)


@add_class_name_property
class PolygonType(BaseModel):
    name: Optional[str] = Field(description="the polygon feature's name. must align with legend extraction")
    color: Optional[str] = Field(description= "color is Hex_color_code") 
    pattern: Optional[str]
    abbreviation: Optional[str]
    description: Optional[str]
    category: Optional[str]    


@add_class_name_property
class GeologicUnit(BaseModel):
    name: str
    description: Optional[str]=None
    comments: Optional[str]=None
    age_text: Optional[str]=None
    t_interval: Optional[str]=None
    b_interval: Optional[str]=None
    t_age: Optional[int]=None
    b_age: Optional[int]=None
    lithology: Optional[List[str]]=None


@add_class_name_property
class PolygonProperty(BaseModel):
    PolygonType: PolygonType
    GeologicUnit: Optional[GeologicUnit]
    

@add_class_name_property
class PolygonFeature(BaseModel):
    id: str = Field(description="Your internal id")
    geometry: Polygon
    properties: PolygonProperty 
    

@add_class_name_property
class PolygonFeatureCollection(BaseModel):
    crs: Optional[str] = Field(
        description="""
            If a feature has been georeference and geom_coordinates are filled in this crs should be filled in
            An example: "EPSG:3857"
        """
    )    
    features: Optional[List[PolygonFeature]]