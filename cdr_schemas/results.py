from typing import List, Optional

from pydantic import BaseModel, Field

from cdr_schemas.feature_results import FeatureResults
from cdr_schemas.georeference import GeoreferenceResults


class Results(BaseModel):
    """
    All results for map.
    """

    georef_results: Optional[List[GeoreferenceResults]] = Field(
        ...,
        description="""
            A list of georef results from systems.
        """,
    )
    extraction_results: Optional[List[FeatureResults]] = Field(
        ...,
        description="""
            A list of feature extraction results from systems.
        """,
    )
