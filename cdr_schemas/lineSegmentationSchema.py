from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour, Provenance

class LineOccurance(BaseModel):
    """Sub-field of LineMapUnit, describes an individual segmentation of a line map unit"""
    geometry : Contour
    confidence : Optional[float]

class LineMapUnit(BaseModel):
    """Sub-field of LineSegmentationSchema, describes a line map unit in the map"""
    label : str
    occurances : List[LineOccurance]
    confidence : Optional[float]

class LineSegmentationSchema(BaseModel):
    """Schema for results of line segmentation from a map"""
    provenance : Provenance
    
    # Data
    features : List[LineMapUnit]