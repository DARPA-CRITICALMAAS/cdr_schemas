from pydantic import BaseModel, Field
from typing import List, Optional
from common import Contour, Provenance

class PolygonOccurance(BaseModel):
    """Sub-field of PolygonMapUnit, describes an individual segmentation of a polygon map unit"""
    geometry : Contour
    confidence : Optional[float]

class PolygonMapUnit(BaseModel):
    """Sub-field of PolygonSegmentationSchema, describes a polygon map unit in the map"""
    label : str
    occurances : List[PolygonOccurance]
    confidence : Optional[float]

class PolygonSegmentationSchema(BaseModel):
    """Schema for results of polygon segmentation from a map"""
    provenance : Provenance

    # Data
    features : List[PolygonMapUnit]
    