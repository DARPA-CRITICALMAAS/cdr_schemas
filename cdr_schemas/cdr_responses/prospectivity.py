from datetime import datetime
from typing import List, Optional, Union

from geojson_pydantic import LineString, Point, Polygon
from pydantic import BaseModel, ConfigDict, Field

from cdr_schemas.prospectivity_input import (
    CreateCriticalMineralAssessment,
    CreateDataSource,
    DataTypeId,
    TranformMethods,
)
from cdr_schemas.prospectivity_models import (
    NeuralNetUserOptions,
    RFUserOptions,
    SOMTrainConfig,
    fastBNNUserOptions,
)


class CriticalMineralAssessment(CreateCriticalMineralAssessment):
    cma_id: str = Field(description="ID of the cma")
    download_url: str = Field(description="url to view template raster")
    creation_date: datetime = Field()


class DataSource(CreateDataSource):
    data_source_id: str = Field(default="")
    download_url: str


class CreateProcessDataLayer(BaseModel):
    data_source: DataSource = Field(description="Data source to create this layer")
    title: str = Field(description="Title to use for processed layer")
    transform_methods: TranformMethods = Field(
        default_factory=list, description="Transformation method used"
    )
    label_raster: bool = Field(description="A label layer for training")


class DataTypeIdWithGeom(DataTypeId):
    geom: Point | LineString | Polygon = Field(description="Adding feature coords")


class CreateVectorProcessDataLayer(BaseModel):
    label_raster: bool = Field(
        default=False, description="Layer used to train prospectivity models"
    )
    title: str = Field(description="Title to use for processed layer")
    evidence_features: List[DataTypeIdWithGeom] = Field(
        default_factory=list, description="Feature ids from the cdr"
    )
    extra_geometries: List[Point | LineString | Polygon] = Field(
        default_factory=list,
        description="site locations selected by expert. Use EPSG:4326 only",
    )
    transform_methods: TranformMethods = Field(
        default_factory=list, description="Transformation method used"
    )


class ProcessedDataLayer(BaseModel):
    layer_id: str = Field(description="Layer id")
    download_url: str = Field(description="Download url")
    label_raster: Optional[bool] = Field(description="Label raster")
    title: str = Field(description="title of layer")


class ProspectModelMetaData(BaseModel):
    """
    # CDR to TA3: EVENT
    provides a model run id, cma
    """

    model_run_id: str = Field(description="CDR id of the model run")
    cma: CriticalMineralAssessment = Field(description="CMA info")
    model_type: str
    train_config: Union[
        SOMTrainConfig, NeuralNetUserOptions, RFUserOptions, fastBNNUserOptions
    ]
    evidence_layers: List[ProcessedDataLayer] = Field(
        description="Processed data layer info."
    )

    model_config = ConfigDict(protected_namespaces=())


class ProcessDataLayers(BaseModel):
    cma: CriticalMineralAssessment = Field(description="CMA info")

    evidence_layers: List[CreateProcessDataLayer] = Field(
        default_factory=list, description="Datasource and preprocess steps"
    )
    vector_layers: List[CreateVectorProcessDataLayer] = Field(
        default_factory=list,
        description="Vector features and preprocess steps. EPSG:4326",
    )
    previously_processed: List[dict] = Field(
        description="Preprocessed layers that have already been processed in a previous event",
        default_factory=list,
    )

    model_config = ConfigDict(protected_namespaces=())
