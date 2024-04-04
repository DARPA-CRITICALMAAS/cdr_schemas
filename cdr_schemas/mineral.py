from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from cdr_schemas.document import Document


class Geometry(Enum):
    Point = "Point"
    Polygon = "Polygon"


class ResourceReserveCategory(Enum):
    INFERRED = "Inferred Mineral Resource"
    INDICATED = "Indicated Mineral Resource"
    MEASURED = "Measured Mineral Resource"
    PROBABLE = "Probable Mineral Reserve"
    PROVEN = "Proven Mineral Reserve"


class GeologyInfo(BaseModel):
    age: Optional[str] = Field(description="Age of the geologic unit or event")
    unit_name: Optional[str] = Field(description="Name of the geologic unit")
    description: Optional[str]
    lithology: Optional[list[str]]
    process: Optional[list[str]]
    environment: Optional[list[str]]
    comments: Optional[str]


class Ore(BaseModel):
    ore_unit: str = Field(
        description="The unit in which ore quantity is measured, eg, metric tonnes"
    )
    ore_value: float = Field(description="The value of ore quantity")


class DepositType(BaseModel):
    name: str = Field(description="Deposit type name")
    environment: str = Field(description="Deposit type environment")
    group: str = Field(description="Deposit type group")


class DepositTypeCandidate(BaseModel):
    observed_name: str = Field(
        description="Source dataset that the site info is retrieved from. e.g., MRDS"
    )
    normalized_uri: DepositType = Field(
        description="The deposit type of an inventory item"
    )
    confidence: float = Field(description="Score deposit type of an inventory item")
    source: str = Field(
        description="Source of the classification (automated model version / SME / etc...)"
    )


class BoundingBox(BaseModel):
    x_min: float
    x_max: float
    y_min: float
    y_max: float


class PageInfo(BaseModel):
    page: int
    bounding_box: Optional[BoundingBox] = Field(
        description="Coordinates of the document where reference is found"
    )


class Reference(BaseModel):
    document: Document
    page_info: List[PageInfo] = Field(
        description="List of pages and their respective bounding boxes where the reference is found"
    )


class EvidenceLayer(BaseModel):
    name: str
    relevance_score: float


class MappableCriteria(BaseModel):
    criteria: str
    theoretical: Optional[str]
    potential_dataset: Optional[list[EvidenceLayer]]
    supporting_references: list[Reference]


class MineralSystem(BaseModel):
    deposit_type: list[DepositType]
    source: list[MappableCriteria]
    pathway: list[MappableCriteria]
    trap: Optional[list[MappableCriteria]]
    preservation: Optional[list[MappableCriteria]]
    energy: Optional[list[MappableCriteria]]
    outflow: Optional[list[MappableCriteria]]


class Commodity(BaseModel):
    name: str


class Grade(BaseModel):
    grade_unit: str = Field(
        description="The unit in which grade is measured, eg, percent"
    )
    grade_value: float = Field(description="The value of grade")


class MineralInventory(BaseModel):
    commodity: Commodity = Field(description="The commodity of an inventory item")
    observed_commodity: Optional[str] = Field(
        description="The observed commodity in the source data (textual format)"
    )
    category: Optional[ResourceReserveCategory] = Field(
        description="The category of an inventory item"
    )
    ore: Optional[Ore] = Field(description="The ore of an inventory item")
    grade: Optional[Grade] = Field(description="The grade of an inventory item")
    cutoff_grade: Optional[Grade] = Field(
        description="The cutoff grade of the observed inventory item"
    )
    contained_metal: Optional[float] = Field(
        description="The quantity of a contained metal in an inventory item"
    )
    reference: Reference = Field(description="The reference of an inventory item")
    date: Optional[datetime] = Field(
        description="When in the point of time mineral inventory valid"
    )
    zone: Optional[str] = Field(
        description="zone of mineral site where inventory item was discovered"
    )


class LocationInfo(BaseModel):
    location: Geometry = Field(
        description="Type: Polygon or Point, value indicates the geolocation of the site"
    )
    crs: str = Field(
        description="The Coordinate Reference System (CRS) of the location"
    )
    country: Optional[str] = Field(description="Country that the mine site resides in")
    state_or_province: Optional[str] = Field(
        description="State or province that the mine site resides in"
    )


class MineralSite(BaseModel):
    source_id: str = Field(
        description="Source dataset that the site info is retrieved from. e.g., MRDS"
    )
    record_id: str = Field(
        description="Unique ID of the record that the info is retrieved from e.g., 10022920"
    )
    name: Optional[str] = Field(description="Name of the mine, e.g., Tungsten Jim")
    mineral_inventory: list[MineralInventory]
    location_info: LocationInfo
    geology_info: Optional[GeologyInfo]
    deposit_type_candidate: list[DepositTypeCandidate]
