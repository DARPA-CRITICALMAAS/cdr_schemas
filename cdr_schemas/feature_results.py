from pydantic import BaseModel, Field
from typing import List, Optional

from cdr_schemas.point_features import PointLegendAndFeaturesResult
from cdr_schemas.polygon_features import PolygonLegendAndFeauturesResult
from cdr_schemas.line_features import LineLegendAndFeaturesResult
from cdr_schemas.map_area_extraction import MapArea


class FeatureResults(BaseModel):
    """
    Feature Extraction Results.
    """

    cog_id: str = Field(
        ...,
        description="""
            Cog id.
        """,
    )
    line_feature_results: Optional[List[LineLegendAndFeaturesResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated line feature results.
        """,
    )
    point_feature_results: Optional[List[PointLegendAndFeaturesResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated point feature results.
        """,
    )
    polygon_feature_results: Optional[List[PolygonLegendAndFeauturesResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated polygon feature results. 
        """,
    )
    map_areas: Optional[List[MapArea]]
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
