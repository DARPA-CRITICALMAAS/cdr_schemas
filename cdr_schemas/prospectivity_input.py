from enum import Enum
from typing import List, Optional, Tuple, Union

from geojson_pydantic import MultiPolygon
from pydantic import BaseModel, Field

from cdr_schemas.prospectivity_models import (
    NeuralNetTrainConfig,
    NeuralNetUserOptions,
    SOMTrainConfig,
)


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


class TransformMethod(str, Enum):
    LOG = "log"
    ABS = "abs"
    SQRT = "sqrt"


class ImputeMethod(str, Enum):
    MEAN = "mean"
    MEDIAN = "median"


class Impute(BaseModel):
    impute_method: ImputeMethod
    window_size = List[int] = Field(
        default=(3, 3),
        description="Size of window centered around pixel to be imputed.",
    )


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


# TA3 TO CDR:
# TA3 can send this with the raster as their model output.
class ProspectivityOutputLayer(BaseModel):
    system: str
    system_version: str
    model: str
    model_version: str
    model_run_id: str = Field(description="Connect this output to a model run")
    cma_id: str = Field(description="id of the cma")
    title: str = Field(description="Title for prospectivity layer")


# MTRI to CDR:
# send to cdr to create new cma. Will be associated with template raster uploaded
class CreateCriticalMineralAssessment(BaseModel):
    crs: str
    extent: MultiPolygon
    resolution: Tuple[int, int]
    mineral: str
    description: str


# CDR to Anyone
class CriticalMineralAssessment(CreateCriticalMineralAssessment):
    cma_id: str = Field(description="ID of the cma")
    download_url: str = Field(description="url to view template raster")


# MTRI UI TO CDR:
# define preprocessing actions
class DefineProcessDataLayer(BaseModel):
    cma_id: str = Field(description="ID of the cma")
    data_source_id: str = Field(description="Data source id used to create this layer")
    title: str = Field(description="Title to use for processed layer")
    transform_method: Union[TransformMethod, Impute] = Field(
        default="", description="Transformation method used"
    )
    scaling_method: ScalingType = Field(default="", description="Scaling type if any")
    normalization_method: str = Field(default="", description="normalization method")


# CDR to TA3:
# define preprocessing actions
class CreateProcessDataLayer(BaseModel):
    cma: CriticalMineralAssessment = Field(
        description="CMA with all information needed for processing"
    )
    data_source: DataSource = Field(description="Data source to create this layer")
    title: str = Field(description="Title to use for processed layer")
    transform_method: Union[TransformMethod, Impute] = Field(
        default="", description="Transformation method used"
    )
    scaling_method: ScalingType = Field(default="", description="Scaling type if any")
    normalization_method: str = Field(default="", description="normalization method")


# TA3 TO CDR:
# Send along with a processed data layer used for training to support their model output.
# TA3 can send each layer of the training stack used to generate the output one layer at a time
class SaveProcessedDataLayer(BaseModel):
    model_run_id: str = Field(
        description="Connect this processed data layer to a model run output layer"
    )
    data_source_id: str = Field(description="Data source id used to create this layer")
    cma_id: str = Field(description="ID of the cma")
    title: str = Field(description="Title for processed layer")
    system: str
    system_version: str
    transform_method: Union[TransformMethod, Impute] = Field(
        default="", description="Transformation method used"
    )
    scaling_method: ScalingType = Field(default="", description="Scaling type if any")
    normalization_method: str = Field(default="", description="normalization method")


# MTRI UI to CDR:
# defines the cma, model training config and layer preprocessing steps
class CreateProspectModelMetaData(BaseModel):
    cma_id: str = Field(description="CMA id")
    system: str
    system_version: str
    author: str
    date: str
    organization: str
    train_config: Union[SOMTrainConfig, NeuralNetTrainConfig, NeuralNetUserOptions]
    evidence_layers: List[DefineProcessDataLayer] = Field(
        description="Datasource and preprocess steps"
    )


# CDR to TA3: EVENT
# provides a model run id, cma
class ProspectModelMetaData(BaseModel):
    model_run_id: str = Field(description="CDR id of the model run")
    cma: CriticalMineralAssessment = Field(description="CMA info")
    train_config: Union[SOMTrainConfig, NeuralNetTrainConfig, NeuralNetUserOptions]
    evidence_layers: List[CreateProcessDataLayer]
