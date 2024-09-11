from typing import List, Union
from datetime import datetime
from pydantic import BaseModel, Field

from cdr_schemas.prospectivity_input import (
    CreateCriticalMineralAssessment,
    CreateDataSource,
    TranformMethods,
)
from cdr_schemas.prospectivity_models import NeuralNetUserOptions, SOMTrainConfig


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
        default="", description="Transformation method used"
    )


class ProspectModelMetaData(BaseModel):
    """
    # CDR to TA3: EVENT
    provides a model run id, cma
    """

    model_run_id: str = Field(description="CDR id of the model run")
    cma: CriticalMineralAssessment = Field(description="CMA info")
    model_type: str
    train_config: Union[SOMTrainConfig, NeuralNetUserOptions]
    evidence_layers: List[CreateProcessDataLayer]
