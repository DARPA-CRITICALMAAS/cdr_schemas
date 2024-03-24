from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum
from common import Contour, Provenance

# Option1 explictly defines the fields as part of the base schema object and is a little bit simpler in structure.
# Option2 is a little bit more modular. Albert slightly favors Option1 but doesn't have a strong opinion if others perfer option 2
# region Option1
class LayoutSchema(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    map_region : Optional[List[Contour]] = Field(description="The bounding contour for the area of the image the map is in.")
    point_legend : Optional[List[Contour]] = Field(description="The bounding contour for the area the point units of the legend are in.")
    line_legend : Optional[List[Contour]] = Field(description="The bounding contour for the area the line units of the legend are in.")
    polygon_legend : Optional[List[Contour]] = Field(description="The bounding contour for the area the polygon units of the legend are in.")
    cross_section : Optional[List[Contour]] = Field(description="The bounding contour for the area of the image the cross section is in.")
    correlation_diagram : Optional[List[Contour]] = Field(description="The bounding contour for the area of the image the correlation diagram is in.")
# region Option1

# region Option2
class region_segmentation_type(str, Enum):
    map = 'map'
    point_legend = 'point_legend'
    line_legend = 'line_legend'
    polygon_legend = 'polygon_legend'
    cross_section = 'cross_section'
    correlation_diagram = 'correlation_diagram'

class region_segmentation(BaseModel):
    """"""
    type : region_segmentation_type = Field(description="The type of region that is being defined.")
    geometry : List[List[float]] = Field(description="The bounding contour of the region being defined.")
    confidence : Optional[float] = Field(description="The model's confidence level in this prediction.")

class LayoutSchema2(BaseModel):
    """Schema for results of layout extraction from a map"""
    # Provenance
    provenance : Provenance
    
    # Data
    regions : List[region_segmentation] = Field(description="List containing all of the individual region segmentations for the map.")
# endregion Option2