from enum import Enum
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field


class NeuralNetUserOptions(BaseModel):
    # data/model inputs processing args
    likely_negative_range: Optional[Tuple[float, float]] = Field(
        default=(0.1, 1.0),
        description="Defines the range of values that are most likely to represent negative (non-prospective) cases. A value of 0 indicates known deposit locations, while 1 represents the farthest pixels from deposits in embedding space.",
    )
    fraction_train_split: Optional[float] = Field(
        default=0.8,
        description="The percentage of the dataset allocated for training the model (e.g., 80% training, remaining 20% for validation and testing split evenly).",
    )
    upsample_multiplier: Optional[float] = Field(
        default=20.0,
        description="Specifies how much to increase the number of positive samples in the training dataset to balance class distribution.",
    )
    random_seed: Optional[int] = Field(
        default=777,
        description="A fixed seed value for the random number generator to ensure consistent and reproducible results across different runs. It affects train/validation/test data splitting and negative sampling.",
    )

    # model args
    number_encoder_layers: Optional[int] = Field(
        default=6,
        description="The number of self-attention layers in the encoder. Increasing this value allows the model to capture more complex hierarchical representations.",
    )
    number_encoder_heads: Optional[int] = Field(
        default=8,
        description="The number of attention heads in each encoder layer. More heads enable the model to attend to different parts of the input sequence simultaneously, improving feature extraction.",
    )
    encoder_embedding_dim: Optional[int] = Field(
        default=256,
        description="The dimensionality of token embeddings in the encoder. A higher embedding dimension allows the model to represent more detailed feature interactions but increases computational cost.",
    )
    number_decoder_layers: Optional[int] = Field(
        default=2,
        description="The number of self-attention layers in the decoder. A deeper decoder can better refine outputs but may increase inference time.",
    )
    number_decoder_heads: Optional[int] = Field(
        default=4,
        description="The number of attention heads in each decoder layer. More heads allow the decoder to process multiple information streams in parallel, enhancing representation learning.",
    )
    decoder_embedding_dim: Optional[int] = Field(
        default=128,
        description="The dimensionality of token embeddings in the decoder. Lower values reduce memory usage and computation cost, while higher values improve expressiveness.",
    )
    dropout_tuple: Optional[Tuple[float, float, float]] = Field(
        default=(0.0, 0.25, 0.25),
        description="A tuple representing dropout rates for each layer in the classifier. Lower values make predictions more deterministic, while higher values introduce uncertainty for probabilistic outputs.",
    )

    # model training args
    learning_rate: Optional[float] = Field(
        default=1e-3,
        description="Controls how quickly the model updates its weights during training. A higher value speeds up learning but may cause instability, while a lower value ensures more gradual learning.",
    )
    weight_decay: Optional[float] = Field(
        default=1e-2,
        description="A technique to prevent overfitting by adding a small penalty to large weight values, encouraging simpler models.",
    )
    smoothing: Optional[float] = Field(
        default=0.3,
        description="Adjusts how sharply the model differentiates between high and low prospectivity areas. Lower values create stronger contrasts, while higher values result in more gradual transitions.",
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
