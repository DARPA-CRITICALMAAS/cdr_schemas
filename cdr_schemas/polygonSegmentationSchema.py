from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour, Provenance

class Polygon(BaseModel):
    """Sub-Field of PolygonSegmentationSchema. Represents a segmented polygon map unit"""
    label : str
    geometry : List[Contour]
    confidence : Optional[float]

class PolygonSegmentationSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    features : List[Polygon]
    