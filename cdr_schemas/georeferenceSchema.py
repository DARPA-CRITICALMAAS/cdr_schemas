from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum
from rasterio.CRS import CRS
from rasterio.transform import Affine
from rasterio.control import GroundControlPoint
from common import Provenance

# Could use this if Rasterio GroundControlPoint doesn't work
# class GroundControlPoint(BaseModel):
#     """Sub-field of GeoreferenceSchema"""
#     pixel_x : Union[float, int]
#     pixel_y : Union[float, int]
#     latitude : Union[float, int]
#     longitude : Union[float, int]
#     confidence : Optional[float]

class GeoreferenceSchema(BaseModel):
    """Schema for results of georeference extraction from a map"""
    provenance : Provenance
    
    # Data
    crs : Optional[CRS] = Field(description="The EPSG number for the crs. Should be in the format \"EPSG:####\" or an equivelent that can be read by rasterio.CRS.from_string()")
    transform : Optional[Affine] = Field(description="")
    ground_control_points : Optional[List[GroundControlPoint]] = Field(description="A list of of ground control points that can be used to create a transform.")
    confidence : Optional[float] = Field(description="The model's confidence level in this prediction.")

    def build_transform_from_gcps():
        #TODO
        #build rasterio transform from gpcs
        raise NotImplementedError