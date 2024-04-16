from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class MapShapeTypes(str, Enum):
    """Enum for the possible values of map_shape field of MapMetadata."""

    rectangular = "rectangular"
    non_rectangular = "non_rectangular"


class MapColorSchemeTypes(str, Enum):
    """Enum for the possible values of map_color_scheme field of MapMetadata"""

    full_color = "full_color"
    monochrome = "monochrome"
    grayscale = "grayscale"


class MapMetaData(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="""
            Title of the map/cog.
        """,
    )
    year: Optional[int] = Field(
        default=None,
        description="""
            Year the map was made. i.e. 2012
        """,
    )
    crs: Optional[str] = Field(
        default=None,
        description="""
            CRS of the map. i.e. "EPSG:4267"
        """,
    )
    authors: List[str] = Field(
        default_factory=list,
        description="""
            Authors of the map
        """,
    )
    organization: Optional[str] = Field(
        default=None,
        description="""
            Organization that created the map
        """,
    )
    scale: Optional[int] = Field(
        default=None,
        description="""
            Scale of the map. 24000 would be equivalent to 1:24000
        """,
    )
    quadrangle_name: Optional[str] = Field(
        default=None,
        description="""
            If map is based on a quadrangle location we can save the name here.
        """,
    )
    map_shape: Optional[MapShapeTypes] = Field(
        default=None,
        description="""
            If the map area(s) has a rectangle shape.
        """,
    )
    map_color_scheme: Optional[MapColorSchemeTypes] = Field(
        default=None,
        description="""
            Color scheme of the map.
        """,
    )
    publisher: Optional[str] = None
    state: Optional[str] = None

    model: str
    model_version: str

    model_config = ConfigDict(protected_namespaces=())


class CogMetaData(BaseModel):
    cog_id: str
    system: str
    system_version: str
    multiple_maps: Optional[bool] = None
    map_metadata: List[MapMetaData] = Field(
        default_factory=list,
        description="""
            Maps metadata
        """,
    )
