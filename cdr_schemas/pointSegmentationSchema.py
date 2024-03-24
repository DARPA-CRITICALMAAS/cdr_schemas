from pydantic import BaseModel, Field
from typing import List, Optional
from common import Provenance

class PointOccurance(BaseModel):
    """Sub-field of PointMapUnit, describes an individual occurance of a point map unit in the map"""
    geometry : List[float]
    dip : Optional[float]
    dip_direction : Optional[float]
    confidence : Optional[float]

class PointMapUnit(BaseModel):
    """Sub-field of PointSegmentationSchema, describes a point map unit in the map"""
    label : str
    occurances : List[PointOccurance]
    confidence : Optional[float]
    
class PointSegmentationSchema(BaseModel):
    """Schema for results of point segmentation from a map"""
    provenance : Provenance
    
    # Data
    features : List[PointMapUnit]