from enum import Enum
from typing import  Optional, Tuple

from pydantic import BaseModel, Field

class Accelerator(str, Enum):
    CPU = "cpu"
    GPU = "gpu"


class NeuralNetUserOptions(BaseModel):
    smoothing: Optional[float] = Field(
        default=0.5,
        description="Controls certainty of data labels. Low smoothing results in large gradients between low vs high prospectivity areas. High smoothing results in incremental gradients between low vs high prospectivity areas.",
    )
    dropout: Optional[float] = Field(
        default=0.5,
        description="Dropout influences variance of network outputs. Low dropout results in deterministic prospectivity map. High dropout results in probabilistic prospectivity map.",
    )
    negative_sampling_fraction: Optional[Tuple[float, float]] = Field(
        default=(0.0, 0.25)
    )


class NeuralNetTrainConfig(BaseModel):
    min_epochs: int  # prevents early stopping
    max_epochs: int

    accelerator: Accelerator

    # mixed precision for extra speed-up
    precision: int

    # perform a validation loop twice every training epoch
    val_check_interval: float

    # set True to to ensure deterministic results
    # makes training slower but gives more reproducibility than just setting seeds
    deterministic: bool


class NeighborhoodFunction(str, Enum):
    GAUSSIAN = "gaussian"
    BUBBLE = "bubble"


class SOMType(str, Enum):
    TOROID = "toroid"
    SHEET = "sheet"


class NeighborhoodDecay(str, Enum):
    LINEAR = "linear"
    EXPONENTIAL = "exponential"


class LearningRateDecay(str, Enum):
    LINEAR = "linear"
    EXPONENTIAL = "exponential"


class SOMInitialization(str, Enum):
    RANDOM = "random"
    PCA = "pca"


class SOMGrid(str, Enum):
    HEXAGONAL = "hexagonal"
    RECTANGULAR = "rectangular"


class SOMTrainConfig(BaseModel):
    size: int = Field(default=20, description="Dimension of generated SOM space")
    dimensions_x: Optional[int] = Field(
        default=20, description="Dimension of generated SOM space in x"
    )
    dimensions_y: Optional[int] = Field(
        default=20, description="Dimension of generated SOM space in y"
    )
    num_initializations: int = Field(
        default=5, description="Number of initializations to run"
    )
    num_epochs: Optional[int] = Field(default=10, description="Number of epochs to run")
    grid_type: Optional[SOMGrid] = Field(default=SOMGrid.RECTANGULAR)
    som_type: Optional[SOMType] = Field(default=SOMType.TOROID)
    som_initialization: Optional[SOMInitialization] = Field(
        default=SOMInitialization.RANDOM
    )
    initial_neighborhood_size: Optional[float] = Field(default=0.0)
    final_neighborhood_size: Optional[float] = Field(default=1.0)
    neighborhood_function: Optional[NeighborhoodFunction] = Field(
        default=NeighborhoodFunction.GAUSSIAN
    )
    gaussian_neighborhood_coefficient: Optional[float] = Field(default=0.5)
    learning_rate_decay: Optional[LearningRateDecay] = Field(
        default=LearningRateDecay.LINEAR
    )
    neighborhood_decay: Optional[NeighborhoodDecay] = Field(
        default=NeighborhoodDecay.LINEAR
    )
    initial_learning_rate: Optional[float]
    final_learning_rate: Optional[float]


# class NeuralNetModel(BaseModel):
#     train_config: NeuralNetTrainConfig
#     pass


# class SOMModel(BaseModel):
#     train_config: SOMTrainConfig
#     pass


# class CMAModel(BaseModel):
#     title: str = Field(
#         description="""
#             Title of the CMA.
#         """,
#     )
#     date: str = Field(
#         default="", description="Model creation date"
#     )
#     authors: List[str] = Field(
#         default_factory=list,
#         description="""
#             Creators of the model
#         """,
#     )
#     organization: Optional[str] = Field(
#         ...,
#         description="""
#             Organization that created the model
#         """,
#     )
#     cma_model_type: Union[NeuralNetModel, SOMModel]

#     training_data: StackMetaData
#     cma_template: CMATemplate



