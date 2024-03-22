from pydantic import BaseModel, Field
from typing import List, Optional

from cdr_schemas.point_features import PointFeatureResult
from cdr_schemas.polygon_features import PolygonFeautureResult
from cdr_schemas.line_features import LineFeatureResult


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
    line_feature_results: Optional[List[LineFeatureResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated line feature results.
        """,
    )
    point_feature_results: Optional[List[PointFeatureResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated point feature results.
        """,
    )
    polygon_feature_results: Optional[List[PolygonFeautureResult]] = Field(
        ...,
        description="""
            A list of legend extractions with associated polygon feature results. 
        """,
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
