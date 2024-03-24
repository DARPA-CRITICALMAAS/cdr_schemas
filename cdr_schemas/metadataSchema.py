from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from common import Provenance

class map_color_scheme_types(str, Enum):
    """Enum for the possible values of map_color_scheme field of MapMetadata"""
    full_color = "full_color"
    monochrome = "monochrome"
    grayscale = "grayscale"

class map_shape_types(str, Enum):
    """Enum for the possible values of map_shape field of MapMetadata"""
    rectangler = "rectangler"
    non_rectangler = "non_rectangler"

class MetadataSchema(BaseModel):
    """Schema for results of metadata extraction from a map"""
    provenance : Provenance
    
    # Data Fields
    title : Optional[str] = Field(description="The title of the map.")
    authors : Optional[List[str]] = Field(description="The name of the author(s) of the map")
    organization : Optional[str] = Field(description="The organization that created the map")
    year : Optional[int] = Field(description="The year the map was made")
    scale : Optional[str] = Field(description="The scale the map is in. E.g. 1:24000")
    map_shape : Optional[map_shape_types] = Field(description="The shape of the map region, is it rectangular or non-rectangular.")
    map_color_scheme : Optional[map_color_scheme_types] = Field(description="The color scheme of the map, this can be full color, monocolor or greyscale.")
    physiographic_region : Optional[str] = Field(description="The physiographic region that the map comes from.")

    # Do we want these fields? They were specified in the TA1 Geopackage schema
    # url : Optional[str] = Field(description="The url that we use? CDR?")
    # source_url : Optional[str] = Field(description="The publisher url that the map orginal was taken from?")
    # publisher : Optional[str] = Field(description="The organization that published the map ")