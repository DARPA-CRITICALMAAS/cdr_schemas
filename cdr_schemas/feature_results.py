
from pydantic import BaseModel, Field
from typing import List, Optional

from cdr_schemas.point_features import PointFeatureCollection
from cdr_schemas.polygon_features import PolygonFeatureCollection
from cdr_schemas.line_features import LineFeatureCollection


class FeatureResults(BaseModel):
    """
    Georeference Results.
    """

    cog_id: str = Field(
        ...,
        description="""
            Cog id.
        """,
    )
    line_feature_results: Optional[List[LineFeatureCollection]] = Field(
        ...,
        description = """
            A list of line feature extraction results. 
        """
    ) 
    point_feature_results: Optional[List[PointFeatureCollection]] = Field(
        ...,
        description = """
            A list of point feature extraction results. 
        """
    ) 
    polygon_feature_results: Optional[List[PolygonFeatureCollection]] = Field(
        ...,
        description = """
            A list of polygon feature extraction results. 
        """
    ) 
    system: str = Field(
        ...,
        description="""
            The name of the system used.
        """,
    )
    system_version: str = Field(
        ...,
        description="""
            The version of the system used.
        """,
    )