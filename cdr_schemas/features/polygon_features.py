from typing import List, Optional, Union
from pydantic import BaseModel, ConfigDict, Field
from cdr_schemas.common import ModelProvenance, GeomType

class PolygonSegmentation(BaseModel):
    """
    Polygon feature.
    """

    # Provenance
    provenance: ModelProvenance = Field(
        description="Where the data orginated from.")

    # Data
    geometry: List[List[List[Union[float, int]]]]
    geom_type: GeomType = GeomType.Polygon
    id: str = Field(
        description="""Each polygon geometry has a unique id. The ids are used 
                    to link the polygon geometries is px-coord and geo-coord.""")   

class PolygonLegend(BaseModel):
    """
    Legend information for a polygon map unit.
    """
    # Provenance
    provenance: ModelProvenance = Field(
        description="Where the data orginated from.")

    # Data
    label: Optional[str] = Field(
        default=None,
        description="Label of the map unit")
    abbreviation: Optional[str] = Field(
        default=None,
        description="Abbreviation of the map unit label.")
    description: Optional[str] = Field(
        default=None,
        description="Description of the map unit")
    legend_bbox: Optional[List[List[Union[float, int]]]] = Field(
        default=None,
        description="The bounding box of the map units label.")
    color: Optional[str] = Field(
        default=None,
        description="The color of the map unit's legend")
    pattern: Optional[str] = Field(
        default=None,
        description="The pattern of the map unit's legend")
    overlay: Optional[bool] = Field(
        default=None,
        description="Wheather or not the map unit can be overlayed on other map units")
    
    # What is this?
    # category: Optional[str] = Field(
    #     default=None,
    #     description="TODO - what is this?")

    # I would remove these as i don't think we have any system that fills them in 
    # age_text: Optional[str] = None
    # b_age: Optional[float] = None
    # b_interval: Optional[str] = None
    # lithology: Optional[str] = None
    # name: Optional[str] = None
    # t_age: Optional[float] = None
    # t_interval: Optional[str] = None
    # comments: Optional[str] = None


# Is object that can be sent to the CDR on its own/ is this a _Result??? or is it just a subfield of feature_results
class PolygonMapUnit(BaseModel):
    """
    Polygon map unit metadata along with associated polygon segmentation found.
    """

    legend = PolygonLegend
    segmentation = Optional[List[PolygonSegmentation]] = Field(
        default=None,
        description="All polygon features for legend item.")
    
    # What is this 
    # id: str = Field(description="your internal id")

    # Why do we have any link to georeferencing in the segmentation result. One of the big reasons to change to this format
    # was to decouple georeferecing from segmentation. All results should be in image coords space.
    # crs: Optional[str] = Field(
    #     default=None, 
    #     description="values={CRITICALMAAS:pixel, EPSG:*}")
    # cdr_projection_id: Optional[str] = Field(
    #     default=None,
    #     description="A cdr projection id used to georeference the features") ### TODO Could use some more explanation