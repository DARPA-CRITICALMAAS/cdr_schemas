from enum import Enum
from typing import List, Optional, Tuple, Union

from geojson_pydantic import MultiPolygon
from pydantic import BaseModel, Field
from cdr_schemas.prospectivity_models import NeuralNetTrainConfig, SOMTrainConfig

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
    window_size = Tuple[int, int] = Field(
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


# TA3 can send this with the raster as their model output. 
class ProspectivityLayer(BaseModel):
    system: str
    system_version: str
    model: str
    model_version: str
    model_run_id: str = Field(description="Connect this output to a model run")
    cma_id: str = Field(description="id of the cma")
    title: str = Field(description="Title for prospectivity layer")
    
    


# TA3 can send this along with a processed data layer used for training to support their model output. 
# If possible the ta3 teams can send the whole stack used to generate the output for reproducibility 
# by sending each layer with these metadata associating them with the model_run_id.
class ProcessedDataLayer(BaseModel):
    model_run_id: str = Field(description="Connect this processed data layer to a model run output layer")
    data_source_id: str = Field(description="Data source id used to create this layer")
    cma_id: str = Field(description="id of the cma")
    title: str = Field(description="title for processed layer")
    system: str
    system_version: str
    transform_method: Union[TransformMethod, Impute] = Field(default="", description="Transformation method used")
    scaling_method: ScalingType = Field(default="", description= "Scaling type if any")
    normalization_method: str = Field(default="",description="normalization method")
    


class CriticalMineralAssessment(BaseModel):
    crs: str
    extent: MultiPolygon
    resolution: Tuple[int, int]
    mineral: str
    description: str


# send to cdr to create new cma.
class CMATemplate(BaseModel):
    cma: CriticalMineralAssessment
    file_name: str = Field(
        ...,
        description="""
            Name of file uploaded for template raster.
        """,
    )


#### send to TA3
# send to cdr from Ericks UI
class StackMetaDataForCDR(BaseModel):
    cma_id: str = Field(description="CMA id")
    train_config: Union[SOMTrainConfig,NeuralNetTrainConfig]
    evidence_layer_ids: List[str] = Field(description= "Datasource ids in the cdr")


# What is sent from CDR to TA3 teams for a model run
class StackMetaDataForProcessing(BaseModel):
    model_run_id: str = Field(description="CDR id of the model run")
    cma_id: str = Field(description="CMA id")
    cma_template_url: str = Field(description= "s3 url to the template raster to help with processing")
    train_config: Union[SOMTrainConfig,NeuralNetTrainConfig]
    evidence_layers: List[DataSource]
