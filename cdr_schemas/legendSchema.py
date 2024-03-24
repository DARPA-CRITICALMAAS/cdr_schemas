from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum
from common import Contour, Provenance

class MapUnitType(str, Enum):
    """Enum for the possible values of  type field of MapUnit"""
    POINT = 'point'
    LINE = 'line'
    POLYGON = 'polygon'
    UNKNOWN = 'unknown'
    def ALL():
        return [MapUnitType.POINT, MapUnitType.LINE, MapUnitType.POLYGON, MapUnitType.UNKNOWN]
    def ALL_KNOWN():
        return [MapUnitType.POINT, MapUnitType.LINE, MapUnitType.POLYGON]

class MapUnit(BaseModel):
    """Sub-field of Legend"""
    type : MapUnitType = Field(description="The type of feature the map unit is. Possible values are 'Point', 'Line', 'Polygon' or 'Unknown'.")
    label : Optional[str] = Field(description="The full name of a map unit.")
    abbreviation : Optional[str] = Field(description="The short abbreviation of a map units label, for polygons this is often a 3-4 letter code.")
    description : Optional[str] = Field(description="The corrasponding description for a map unit label in the legend.")
    color : Optional[str] = Field(description="The hex code of the median color of a map units label. If a map unit is patterned this will not mean anything.")
    pattern : Optional[bool] = Field(description="boolean value which indicates weather a polygon label is a patterned label E.g. Not a solid color label")
    overlay : Optional[bool] = Field(description="Boolean value that indicates wheather a polygon label is an overlay E.g. a map unit that can appear on top of other polygon map units.")
    bbox : Optional[Contour] = Field(description="The list of xy coordinates that define the bounding box for a map unit.")

class LegendSchema(BaseModel):
    """Schema for results of legend extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    features : List[MapUnit] = Field(description="The list of map units for this legend")