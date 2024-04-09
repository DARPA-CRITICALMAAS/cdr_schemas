from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from .ta3_input import StackMetaData


from pydantic import BaseModel, StrictStr

class Accelerator(Enum):
    CPU: "cpu"
    GPU: "gpu"
class SRITrainConfig(BaseModel):
    _target_: StrictStr

    default_root_dir: StrictStr

    min_epochs: int  # prevents early stopping
    max_epochs: int

    accelerator: Accelerator
    devices: int

    # mixed precision for extra speed-up
    precision: int

    # perform a validation loop twice every training epoch
    val_check_interval: float

    # set True to to ensure deterministic results
    # makes training slower but gives more reproducibility than just setting seeds
    deterministic: bool


class NeighborhoodFunction(Enum):
    GAUSSIAN: "gaussian"
    BUBBLE: "bubble"

class SOMType(Enum):
    TOROID: "toroid"
    SHEET: "sheet"

class NeighborhoodDecay(Enum):
    LINEAR: "linear"
    EXPONENTIAL: "exponential"

class LearningRateDecay(Enum):
    LINEAR: "linear"
    EXPONENTIAL: "exponential"

class SOMInitialization(Enum):
    RANDOM: "random"
    PCA: "pca"

class SOMGrid(Enum):
    HEXAGONAL: "hexagonal"
    RECTANGULAR: "rectangular"
class BeakTrainConfig(BaseModel):
    dimensions_x: int
    dimensions_y: int
    num_epochs: int
    num_initializations: int
    neighborhood_function: NeighborhoodFunction
    som_type: SOMType
    neighborhood_decay: NeighborhoodDecay
    learning_rate_decay: LearningRateDecay
    initial_learning_rate: float
    final_learning_rate: float
    som_initialization: SOMInitialization
    som_grid: SOMGrid

class SRIModel(BaseModel):
    train_config: SRITrainConfig
    pass

class BeakModel(BaseModel):
    train_config: BeakTrainConfig
    pass

class CMAModel(BaseModel):
    title: Optional[str] = Field(
        ...,
        description="""
            Title of the model.
        """,
    )
    date: Optional[int] = Field(
        ...,
        description="""
            Date that the model was made. i.e. 2012
        """,
    )
    authors: Optional[List[str]] = Field(
        ...,
        description="""
            Creators of the model
        """,
    )
    organization: Optional[str] = Field(
        ...,
        description="""
            Organization that created the model
        """,
    )
    cma_model_type: Union[SRIModel, BeakModel]

    training_data: StackMetaData
