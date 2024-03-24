from pydantic import BaseModel, Field
from typing import List, Optional
from common import Provenance

class Point(BaseModel):
    label : str
    geometry : List[float]
    dip : Optional[float]
    dip_direction : Optional[float]
    confidence : Optional[float]

class PointSegmentationSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    features : List[Point]