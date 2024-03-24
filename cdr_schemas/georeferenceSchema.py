from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum
from rasterio.CRS import CRS
from rasterio.transform import Affine

class GroundControlPoint(BaseModel):
    """Sub-field of GeoreferenceSchema"""
    pixel_x : Union[float, int]
    pixel_y : Union[float, int]
    latitude : Union[float, int]
    longitude : Union[float, int]
    confidence : Optional[float]

class GeoreferenceSchema(BaseModel):
    """Schema for results of georeference extraction from a map"""
    # Provenance
    model : str = Field(description="Name of the model that was used to generate this data.")
    model_version : str = Field(description="Version number of the model used to generate this data.")
    
    # Data
    crs : Optional[CRS] = Field(description="The EPSG number for the crs. Should be in the format \"EPSG:####\" or an equivelent that can be read by rasterio.CRS.from_string()")
    transform : Optional[Affine] = Field(description="")
    ground_control_points : Optional[List[GroundControlPoint]] = Field(description="A list of of ground control points that can be used to create a transform.")
    confidence : Optional[float] = Field(description="The model's confidence level in this prediction.")

    def build_transform_from_gcps():
        #TODO
        #build rasterio transform from gpcs
        raise NotImplementedError