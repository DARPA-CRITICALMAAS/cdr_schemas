from enum import Enum
from typing import List, Optional, Tuple, Union

from geojson_pydantic import MultiPolygon
from pydantic import BaseModel, Field


class InterpolationType(str, Enum):
    """Enum for the possible values of type field of MapUnit"""

    LINEAR = "linear"
    CUBIC = "cubic"
    NEAREST = "nearest"
    NONE = "none"


class ScalingType(str, Enum):
    """Enum for the possible values of type field of MapUnit"""

    MINMAX = "minmax"
    MAXABS = "maxabs"
    STANDARD = "standard"


class LayerCategory(str, Enum):
    GEOPHYSICS = "geophysics"
    GEOLOGY = "geology"
    GEOCHEMISTRY = "geochemistry"


class LayerDataType(str, Enum):
    CONTINUOUS = "continuous"
    BINARY = "binary"


class DataFormat(str, Enum):
    TIF = "tif"
    SHP = "shp"


class DataSource(BaseModel):
    DOI: Optional[str]
    authors: Optional[List[str]]
    publication_date: Optional[str]
    category: Optional[Union[LayerCategory, str]]
    subcategory: Optional[str]
    description: Optional[str]
    derivative_ops: Optional[str]
    type: LayerDataType
    resolution: Optional[tuple]
    format: DataFormat
    download_url: Optional[str]


class TransformMethod(str, Enum):
    LOG = "log"
    ABS = "abs"
    SQRT = "sqrt"


class ImputeMethod(str, Enum):
    MEAN = "mean"
    MEDIAN = "median"


class Impute(BaseModel):
    impute_method: ImputeMethod
    window_size: Tuple[int, int] = Field(
        default=(3, 3),
        description="Size of window centered around pixel to be imputed.",
    )


class ProcessedDataLayer(BaseModel):
    title: Optional[str]
    transform_method: Union[TransformMethod, Impute]
    scaling_method: ScalingType
    normalization_method: str  # source: LayerDataType


class CriticalMineralAssessment(BaseModel):
    crs: str
    extent: MultiPolygon
    resolution: Tuple[int, int]
    mineral: str
    description: str


class CMATemplate(BaseModel):
    cma: CriticalMineralAssessment
    file: str  # path to template raster defining extent,crs for resampling


class StackMetaData(BaseModel):
    title: Optional[str] = Field(
        ...,
        description="""
            Title of the map/cog.
        """,
    )
    year: Optional[int] = Field(
        ...,
        description="""
            Year the map was made. i.e. 2012
        """,
    )
    crs: Optional[str] = Field(
        ...,
        description="""
            CRS of the map. i.e. "EPSG:4267"
        """,
    )
    authors: Optional[List[str]] = Field(
        ...,
        description="""
            Creators of the dataset
        """,
    )
    organization: Optional[str] = Field(
        ...,
        description="""
            Organization that created the map
        """,
    )

    evidence_layers: List[ProcessedDataLayer]
