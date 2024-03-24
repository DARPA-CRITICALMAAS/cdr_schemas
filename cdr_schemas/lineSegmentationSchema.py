from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour

class Line(BaseModel):
    label : str
    geometry : List[Contour]
    confidence : Optional[float]

class LineSegmentationSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    map_name : str = Field(description="The identifier of the map that this data was extracted from.")
    model : str = Field(description="Name of the model that was used to generate this data.")
    model_version : str = Field(description="Version number of the model used to generate this data.")
    
    # Data
    features : List[Line]