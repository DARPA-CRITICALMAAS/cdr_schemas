from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour, Provenance

class Line(BaseModel):
    """Sub-Field of LineSegmentationSchema. Represents a segmented line map unit"""
    label : str
    geometry : List[Contour]
    confidence : Optional[float]

class LineSegmentationSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    features : List[Line]