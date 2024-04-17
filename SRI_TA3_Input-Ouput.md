# SRIExperimentInput

### Properties

- **`preprocess`**: Refer to *[PreprocessConfig](#PreprocessConfig)*.
- **`data`**: Refer to *[DataConfig](#DataConfig)*.
- **`model`**: Refer to *[ModelConfig](#ModelConfig)*.
- **`callbacks`**: Refer to *[CallbacksConfig](#CallbacksConfig)*.
- **`logger`**: Refer to *[LoggerConfig](#LoggerConfig)*.
- **`trainer`**: Refer to *[TrainerConfig](#TrainerConfig)*.
- **`paths`**: Refer to *[PathsConfig](#PathsConfig)*.
- **`extras`**: Refer to *[ExtrasConfig](#ExtrasConfig)*.
- **`experiment`**
  - **Any of**
    - *string*
    - *null*
- **`hparams_search`**
  - **Any of**
    - *string*
    - *null*
- **`debug`**
  - **Any of**
    - *string*
    - *null*
- **`task_name`** *(string)*
- **`tags`** *(array)*
  - **Items** *(string)*
- **`train`** *(boolean)*
- **`test`** *(boolean)*
- **`ckpt_path`**
  - **Any of**
    - *string*
    - *null*
- **`seed`** *(integer)*
- **`hydra`**: Refer to *[HydraConfig](#HydraConfig)*.

## SRIExperimentOuput

### Properties

- **`checkpoint`**
  - **Any of**
    - *string*
    - *null*
- **`logs`**
  - **Any of**
    - *string*
    - *null*
- **`likelihood_raster`**
  - **Any of**
    - *string*
    - *null*
- **`uncertainty_raster`**
  - **Any of**
    - *string*
    - *null*
- **`attribution_rasters`**
  - **Any of**
    - *array*
      - **Items** *(string)*
    - *null*

## CallbacksConfig

### Properties

- **`model_checkpoint`**: Refer to *[ModelCheckpointConfig](#ModelCheckpointConfig)*.
- **`early_stopping`**: Refer to *[EarlyStoppingConfig](#EarlyStoppingConfig)*.
- **`model_summary`**: Refer to *[ModelSummaryConfig](#ModelSummaryConfig)*.
- **`rich_progress_bar`**: Refer to *[RichProgressBarConfig](#RichProgressBarConfig)*.

## DataConfig

### Properties

- **`tif_dir`** *(string)*
- **`window_size`** *(integer)*
- **`multiplier`** *(number)*
- **`downsample`** *(boolean)*
- **`oversample`** *(boolean)*
- **`likely_neg_range`** *(array)*
  - **Items** *(integer)*
- **`frac_train_split`** *(number)*
- **`batch_size`** *(integer)*
- **`num_workers`** *(integer)*
- **`pin_memory`** *(boolean)*
- **`seed`** *(integer)*
- **`log_path`** *(string)*

## EarlyStoppingConfig

### Properties

- **`monitor`** *(string)*
- **`min_delta`** *(number)*
- **`patience`** *(integer)*
- **`verbose`** *(boolean)*
- **`mode`** *(string)*
- **`strict`** *(boolean)*
- **`check_finite`** *(boolean)*
- **`stopping_threshold`** *(number)*
- **`divergence_threshold`** *(number)*
- **`check_on_train_epoch_end`** *(boolean)*

## ExtrasConfig

### Properties

- **`ignore_warnings`** *(boolean)*
- **`enforce_tags`** *(boolean)*
- **`print_config`** *(boolean)*

## HydraConfig

### Properties


## LoggerConfig

### Properties

- **`save_dir`** *(string)*
- **`offline`** *(boolean)*
- **`id`** *(integer)*
- **`anonymous`** *(boolean)*
- **`project`** *(string)*
- **`log_model`** *(boolean)*
- **`prefix`** *(string)*
- **`group`** *(string)*
- **`tags`** *(array)*
  - **Items** *(string)*
- **`job_type`** *(string)*

## MAEClassifierConfig

### Properties

- **`backbone_ckpt`** *(string)*
- **`backbone_net`**: Refer to *[MAEPretrainConfig](#MAEPretrainConfig)*.
- **`freeze_backbone`** *(boolean)*
- **`dropout_rate`** *(number)*

## MAEPretrainConfig

### Properties

- **`image_size`** *(integer)*
- **`patch_size`** *(integer)*
- **`input_dim`** *(integer)*
- **`enc_dim`** *(integer)*
- **`encoder_layer`** *(integer)*
- **`encoder_head`** *(integer)*
- **`dec_dim`** *(integer)*
- **`output_dim`** *(integer)*
- **`decoder_layer`** *(integer)*
- **`decoder_head`** *(integer)*
- **`mask_ratio`** *(number)*

## ModelCheckpointConfig

### Properties

- **`dirpath`** *(string)*
- **`filename`** *(string)*
- **`monitor`** *(string)*
- **`verbose`** *(boolean)*
- **`save_last`** *(boolean)*
- **`save_top_k`** *(integer)*
- **`mode`** *(string)*
- **`auto_insert_metric_name`** *(boolean)*
- **`save_weights_only`** *(boolean)*
- **`every_n_train_steps`** *(integer)*
- **`train_time_interval`** *(number)*
- **`every_n_epochs`** *(integer)*
- **`save_on_train_epoch_end`** *(boolean)*

## ModelConfig

### Properties

- **`optimizer`**: Refer to *[OptimizerConfig](#OptimizerConfig)*.
- **`scheduler`**: Refer to *[SchedulerConfig](#SchedulerConfig)*.
- **`net`**
  - **Any of**
    - : Refer to *[ResNetClassifierConfig](#ResNetClassifierConfig)*.
    - : Refer to *[MAEPretrainConfig](#MAEPretrainConfig)*.
    - : Refer to *[MAEClassifierConfig](#MAEClassifierConfig)*.
- **`compile`** *(boolean)*
- **`gain`** *(number)*
- **`extract_attributions`** *(boolean)*
- **`mc_samples`** *(integer)*
- **`smoothing`** *(number)*
- **`warmup_epoch`** *(integer)*

## ModelSummaryConfig

### Properties

- **`max_depth`** *(integer)*

## OptimizerConfig

### Properties

- **`lr`** *(number)*
- **`weight_decay`** *(number)*

## PathsConfig

### Properties

- **`root_dir`** *(string)*
- **`work_dir`** *(string)*
- **`data_dir`** *(string)*
- **`log_dir`** *(string)*
- **`output_dir`** *(string)*

## PreprocessConfig

### Properties

- **`raster_stacks`** *(array)*
  - **Items**: Refer to *[RasterStack](#RasterStack)*.

## RasterStack

### Properties

- **`raster_stack_path`** *(string)*
- **`raster_files_path`** *(string)*
- **`raster_files`** *(array)*
  - **Items** *(string)*
- **`raster_files_types`** *(array)*
  - **Items** *(string)*

## ResNetClassifierConfig

### Properties

- **`num_input_channels`** *(integer)*
- **`num_output_classes`** *(integer)*
- **`dropout_rate`** *(number)*

## RichProgressBarConfig

### Properties


## SchedulerConfig

### Properties

- **`mode`** *(string)*
- **`factor`** *(number)*
- **`patience`** *(integer)*

## TrainerConfig

### Properties

- **`default_root_dir`** *(string)*
- **`min_epochs`** *(integer)*
- **`max_epochs`** *(integer)*
- **`accelerator`**: Refer to *[Accelerator](#Accelerator)*.
- **`devices`** *(integer)*
- **`precision`** *(integer)*
- **`val_check_interval`** *(number)*
- **`deterministic`** *(boolean)*
- **`benchmark`** *(boolean)*
- **`strategy`**: Refer to *[DDPStrategy](#DDPStrategy)*.
- **`num_nodes`** *(integer)*
- **`sync_batchnorm`** *(boolean)*

