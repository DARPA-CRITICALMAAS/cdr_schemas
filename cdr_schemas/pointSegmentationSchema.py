from pydantic import BaseModel, Field
from typing import List, Optional

class Point(BaseModel):
    label : str
    geometry : List[float]
    dip : Optional[float]
    dip_direction : Optional[float]
    confidence : Optional[float]

class PointSegmentationSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    map_name : str = Field(description="The identifier of the map that this data was extracted from.")
    model : str = Field(description="Name of the model that was used to generate this data.")
    model_version : str = Field(description="Version number of the model used to generate this data.")
    
    # Data
    features : List[Point]