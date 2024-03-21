from typing import List, Union, Any, Optional
from pydantic import BaseModel, Field
from cdr_schemas.common import GeomType, add_class_name_property


class Point(BaseModel):
    """
    coordinates in line are (column from left, row from bottom).
    """
    coordinates: List[Union[float, int]]
    type: str = Field(default=GeomType.Point)


@add_class_name_property
class PointFeature(BaseModel):
    id: str
    geometry: Point
    model: str = Field(description="model name used for extraction")
    model_version: str = Field(description="model version used for extraction")
    name: Optional[str] = Field(description='The point feature name, such as prospect. Must match legend extraction')
    confidence: Optional[float] = Field(description='The prediction probability from the ML model')
    bbox: Optional[List[Union[float, int]]] = Field(description='The extacted bounding box from the ML model')
    dip: Optional[int]
    dip_direction: Optional[int]
 


@add_class_name_property
class PointFeatureCollection(BaseModel):
    crs: Optional[str] = Field(
        description="""
            If a feature has been georeference and geom_coordinates are filled in this crs should be filled in
            An example: "EPSG:3857"
        """
    )    
    features: List[PointFeature]