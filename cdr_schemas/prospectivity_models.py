from enum import Enum
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field


class NeuralNetUserOptions(BaseModel):
    # data/model inputs processing args
    likely_negative_range: Optional[Tuple[float, float]] = Field(
        default=(0.1, 1.0),
        description="The range of values to consider as likely negatives.",
    )
    fraction_train_split: Optional[float] = Field(
        default=0.8, description="The fraction of the data to use for training."
    )
    upsample_multiplier: Optional[float] = Field(
        default=20.0,
        description="The multiplier for upsampling positives in the training data split.",
    )

    # model args
    dropout_tuple: Optional[Tuple[float, float, float]] = Field(
        default=(0.0, 0.25, 0.25),
        description="Dropout influences variance of network outputs. Low dropout results in deterministic prospectivity map. High dropout results in probabilistic prospectivity map.",
    )

    # model training args
    learning_rate: Optional[float] = Field(
        default=1e-3,
        description="Model learning rate. In machine learning referring to the step size at each iteration while moving toward a minimum of a loss function.",
    )
    weight_decay: Optional[float] = Field(
        default=1e-2,
        description="Model weight decay. A regularization technique that prevents the model weights from growing too large by adding a penalty term to the loss function.",
    )
    smoothing: Optional[float] = Field(
        default=0.3,
        description="Controls certainty of data labels. Low smoothing results in large gradients between low vs high prospectivity areas. High smoothing results in incremental gradients between low vs high prospectivity areas.",
    )


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
    num_initializations: Optional[int] = Field(
        default=5, description="Number of initializations to run"
    )
    num_epochs: int = Field(default=10, description="Number of epochs to run")
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
    kmeans: Optional[bool] = Field(
        default=True, description="Whether to apply KMeans after SOM run"
    )
    kmeans_min: Optional[int] = Field(
        default=1, description="Minimum number of clusters for KMeans"
    )
    kmeans_max: Optional[int] = Field(
        default=10, description="Maximum number of clusters for KMeans"
    )


class RFUserOptions(BaseModel):
    n_estimators: Optional[int] = Field(
        default=100,
        description="Controls number of trees used in sklearn RandomForestClassifier. More trees means higher accuracy but longer runtimes.  This should be interpreted as a 'compute budget' more than a hyperparameter.",
    )

    n_unlabeled: Optional[int] = Field(
        default=40_000,
        description="Number of unlabeled points to use to train the model.",
    )


class fastBNNUserOptions(BaseModel):
    train_size: Optional[float] = Field(
        default=1.0,
        description="Fraction of data to use for training/testing. Value of 1 refers to all data used for training and disables separate testing.",
    )
    init_negatives_multiplier: Optional[int] = Field(
        default=20,
        description="Higher value means more negative values are sampled from the unknowns. Reduce if the result contains large flat areas with low values. Recommended: 5 - 20.",
    )
    upsample_positives_multiplier: Optional[float] = Field(
        default=0.0,
        description="Oversample positive labels to a fraction of negatives. Value of 0.25 oversamples positives to 25% the number of negatives. Higher value may lead to overfitting. Recommended: 0.0 - 0.25.",
    )
    learning_rate: Optional[float] = Field(
        default=1e-3,
        description="Learning rate for the neural network. Step size during loss calculation towards the minimum loss.",
    )
    training_epochs: Optional[int] = Field(
        default=100,
        description="Number of iterations to train the neural network. Higher value may lead to overfitting. Recommended: 75 - 125.",
    )
    network_arch_depth: Optional[int] = Field(
        default=2,
        description="Number of layers. Higher value increases complexity and may lead to overfitting. Recommended: 2 - 3.",
    )
    network_arch_width: Optional[int] = Field(
        default=1,
        description="Number of neurons. Higher value enhances feature learning capacity but may also lead to overfitting. Recommended: 1 - 3.",
    )
    network_arch_core_units: Optional[List[int]] = Field(
        default=None,
        description="Custom architecture for the core layers of the neural network. If provided, overwrites depth and width parameters.",
    )
    network_arch_head_units: Optional[List[int]] = Field(
        default=None,
        description="Custom architecture for the head layers the neural network. If provided, overwrites depth and width parameters.",
    )
