from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from .ta3_input import StackMetaData


from pydantic import BaseModel, StrictStr

# Pytorch Lightning Datamodule Config
class DataConfig(BaseModel):
    _target_: str
    # dataset params
    tif_dir: str
    window_size: int
    multiplier: float
    downsample: bool
    oversample: bool
    likely_neg_range: List[int]
    frac_train_split: float
    # training params
    batch_size: int
    num_workers: int
    pin_memory: bool
    # experiment tracking
    seed: int
    log_path: str

# Optimizer Algorithm Config
class OptimizerConfig(BaseModel):
    _target_: str
    _partial_: bool
    lr: float
    weight_decay: float

# Learning Rate Scheduler Config
class SchedulerConfig(BaseModel):
    _target_: str
    _partial_: bool
    mode: str
    factor: float
    patience: int

# ResNet Classifier Config
class ResNetClassifierConfig(BaseModel):
    _target_: str
    num_input_channels: int
    num_output_classes: int
    dropout_rate: float

# MAE ViT Pretrain Config
class MAEPretrainConfig(BaseModel):
    _target_: str
    image_size: int
    patch_size: int
    input_dim: int
    enc_dim: int
    encoder_layer: int
    encoder_head: int
    dec_dim: int
    output_dim: int
    decoder_layer: int
    decoder_head: int
    mask_ratio: float

# MAE ViT Classifier Config
class MAEClassifierConfig(BaseModel):
    _target_: str
    backbone_ckpt: str
    backbone_net: MAEPretrainConfig
    freeze_backbone: bool
    dropout_rate: float

# General Model Config for various DNNs
class ModelConfig(BaseModel):
    _target_: str
    optimizer: OptimizerConfig
    scheduler: SchedulerConfig
    net: Union[ResNetClassifierConfig, MAEPretrainConfig, MAEClassifierConfig]
    # compile model for faster training with pytorch 2.0
    compile: bool
    gain: float
    extract_attributions: bool
    mc_samples: int
    smoothing: float
    warmup_epoch: int

# Early Stopping Config to end training
class EarlyStoppingConfig(BaseModel):
    _target_: str
    monitor: str
    min_delta: float
    patience: int
    verbose: bool
    mode: str
    strict: bool
    check_finite: bool
    stopping_threshold: float
    divergence_threshold: float
    check_on_train_epoch_end: bool

# Model Checkpointing config to save models
class ModelCheckpointConfig(BaseModel):
    _target_: str
    dirpath: str
    filename: str
    monitor: str
    verbose: bool
    save_last: bool
    save_top_k: int
    mode: str
    auto_insert_metric_name: bool
    save_weights_only: bool
    every_n_train_steps: int
    train_time_interval: float
    every_n_epochs: int
    save_on_train_epoch_end: bool

# Model Summary config to print model summary
class ModelSummaryConfig(BaseModel):
    _target_: str
    max_depth: int

# Rich Progress Bar config when running
class RichProgressBarConfig(BaseModel):
    _target_: str

# Various Callback configs
class CallbacksConfig(BaseModel):
    model_checkpoint: ModelCheckpointConfig
    early_stopping: EarlyStoppingConfig
    model_summary: ModelSummaryConfig
    rich_progress_bar: RichProgressBarConfig

# Pytorch Lightning Logger config
class LoggerConfig(BaseModel):
  _target_: str
  save_dir: str
  offline: bool
  id: int
  anonymous: bool
  project: str
  log_model: bool
  prefix: str
  group: str
  tags: List[str]
  job_type: str


class Accelerator(str, Enum):
    CPU = "cpu"
    GPU = "gpu"


class DDPStrategy(str, Enum):
    DDP = "ddp"
    DDP_NOTEBOOK = "dpp_notebook"
    DDP_SIM = "ddp_spawn"

# Pytorch Lightning Trainer config
class TrainerConfig(BaseModel):
    _target_: str
    default_root_dir: str
    min_epochs: int
    max_epochs: int
    accelerator: Accelerator
    devices: int
    precision: int
    val_check_interval: float
    deterministic: bool
    benchmark: bool
    strategy: DDPStrategy
    num_nodes: int
    sync_batchnorm: bool

# Paths config for data, logs, etc
class PathsConfig(BaseModel):
    root_dir: str
    work_dir: str
    data_dir: str
    log_dir: str
    output_dir: str

# Extras config
class ExtrasConfig(BaseModel):
    ignore_warnings: bool
    enforce_tags: bool
    print_config: bool

# Hydra config
class HydraConfig(BaseModel):
    pass

# datastrcuture to build a raster stack
class RasterStack(BaseModel):
    raster_stack_path: str
    raster_files_path: str
    raster_files: List[str]
    raster_files_types: List[str]

# Preprocessing config to generate raster stack
class PreprocessConfig(BaseModel):
    _target_: str
    raster_stacks: List[RasterStack]

# SRI Experiment config for all run parameters
class SRIExperimentConfig(BaseModel):
    preprocess: PreprocessConfig
    data: DataConfig
    model: ModelConfig
    callbacks: CallbacksConfig
    logger: LoggerConfig
    trainer: TrainerConfig
    paths: PathsConfig
    extras: ExtrasConfig
    experiment: Optional[str]
    hparams_search: Optional[str]
    debug: Optional[str]
    task_name: str
    tags: List[str]
    train: bool
    test: bool
    ckpt_path: Optional[str]
    seed: int
    hydra: HydraConfig


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
    train_config: SRIExperimentConfig
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
