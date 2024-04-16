from typing import List, Optional

from pydantic import BaseModel, Field

from cdr_schemas.area_extraction import Area_Extraction
from cdr_schemas.features.line_features import LineLegendAndFeaturesResult
from cdr_schemas.features.point_features import PointLegendAndFeaturesResult
from cdr_schemas.features.polygon_features import PolygonLegendAndFeaturesResult
from cdr_schemas.metadata import CogMetaData


class FeatureResults(BaseModel):
    """
    Feature Extraction Results.
    """

    system: str = Field(description="The name of the system used to generate results.")
    system_version: str = Field(
        description="The version of the system used to generate results."
    )
    cog_id: str = Field(description="Cog id.")
    line_feature_results: Optional[List[LineLegendAndFeaturesResult]] = Field(
        default=[],
        description="""A list of legend extractions with associated line
                    feature results.""",
    )
    point_feature_results: Optional[List[PointLegendAndFeaturesResult]] = Field(
        default=[],
        description="""A list of legend extractions with associated point
                    feature results.""",
    )
    polygon_feature_results: Optional[List[PolygonLegendAndFeaturesResult]] = Field(
        default=[],
        description="""A list of legend extractions with associated polygon
                    feature results.""",
    )
    cog_area_extractions: Optional[List[Area_Extraction]] = Field(
        default=[],
        description="""Higher level extraction pulled off a cog - legend area,
                    map area, ocr text area, etc.""",
    )
    cog_metadata_extractions: Optional[List[CogMetaData]] = Field(
        default=[], description="Metadata extractions pulled off a cog."
    )
