from typing import List, Optional, Union

from pydantic import BaseModel, Field


class DocumentReference(BaseModel):
    cdr_id: str
    page: Optional[int] = Field(default=None)
    x_min: Optional[float] = Field(default=None)
    x_max: Optional[float] = Field(default=None)
    y_min: Optional[float] = Field(default=None)
    y_max: Optional[float] = Field(default=None)


class EvidenceLayer(BaseModel):
    name: str = Field(default="")
    relevance_score: float


class MappableCriteria(BaseModel):
    criteria: str
    theoretical: str = Field(default="")
    potential_dataset: list[EvidenceLayer] = Field(
        default_factory=list, description="List of evidence layers"
    )
    supporting_references: list[DocumentReference]


class MineralSystem(BaseModel):
    deposit_type: list[str] = Field(default_factory=list)
    source: list[MappableCriteria] = Field(default_factory=list)
    pathway: list[MappableCriteria] = Field(default_factory=list)
    trap: list[MappableCriteria] = Field(
        default_factory=list, description="Mappable Criteria: trap"
    )
    preservation: list[MappableCriteria] = Field(
        default_factory=list, description="Mappable Criteria: Preservation"
    )
    energy: list[MappableCriteria] = Field(
        default_factory=list, description="Mappable Criteria: Energy"
    )
    outflow: list[MappableCriteria] = Field(
        default_factory=list, description="Mappable Criteria: outflow"
    )


class GeologyInfo(BaseModel):
    age: str = Field(default="", description="Age of the geologic unit or event")
    unit_name: str = Field(default="", description="Name of the geologic unit")
    description: str = Field(default="")
    lithology: List[str] = Field(default_factory=list, description="Lithology")
    process: List[str] = Field(default_factory=list, description="Process")
    environment: List[str] = Field(default_factory=list, description="environment")
    comments: str = Field(default="")


class DepositType(BaseModel):
    id: Optional[str] = Field(default=None, description="Deposit type id")
    name: str = Field(description="Deposit type name")
    environment: str = Field(description="Deposit type environment")
    group: str = Field(description="Deposit type group")


class DepositTypeCandidate(BaseModel):
    observed_name: str = Field(
        default="",
        description="Source dataset that the site info is retrieved from. e.g., MRDS",
    )

    deposit_type_id: Optional[str] = Field(default=None, description="Deposit type id")

    confidence: Optional[Union[float, int]] = Field(
        default=None, description="Score deposit type of an inventory item"
    )
    source: str = Field(
        description="Source of the classification (automated model version / SME / etc...)"
    )


class RecordReference(BaseModel):
    record_id: str = Field(default="", description="id in source")
    source: str = Field(default="", description="Source information")
    uri: str = Field(default="", description="uri of source")


class MineralInventoryCategory(BaseModel):
    category: str = Field(description="category name")
    confidence: Optional[Union[float, int]] = Field(
        default=None,
    )
    source: str = Field(
        description="Source of the classification (automated model version / SME / etc...)"
    )


class GeoLocationInfo(BaseModel):
    crs: str = Field(
        description="The Coordinate Reference System (CRS) of the location"
    )

    geom: str = Field(
        description="Type: Polygon or Point, value indicates the geolocation of the site"
    )


class Confidence(BaseModel):
    confidence: Optional[Union[float, int]] = Field(default=None)
    source: str = Field(
        description="Source of the classification (automated model version / SME / etc...)"
    )


class MineralInventory(BaseModel):
    contained_metal: Optional[float] = Field(
        default=None,
        description="The quantity of a contained metal in an inventory item",
    )
    commodity: str = Field(default="", description="The commodity of an inventory item")
    commodity_observed_name: str = Field(
        default="",
        description="The observed commodity in the source data (textual format)",
    )

    ore_unit: str = Field(
        default="",
        description="The unit in which ore quantity is measured, eg, metric tonnes",
    )
    ore_value: Optional[float] = Field(
        default=None, description="The value of ore quantity"
    )

    grade_unit: str = Field(
        default="", description="The unit in which grade is measured, eg, percent"
    )
    grade_value: Optional[float] = Field(default=None, description="The value of grade")

    cutoff_grade_unit: str = Field(
        default="", description="The unit in which grade is measured, eg, percent"
    )
    cutoff_grade_value: Optional[float] = Field(default=None)

    material_form: Optional[float] = Field(default=None)
    material_form_unit: str = Field(default="")
    material_form_conversion: Optional[float] = Field(default=None)

    confidence: Optional[Confidence] = Field(default=None)

    categories: List[MineralInventoryCategory] = Field(
        default_factory=list,
        description="""
            A list of categories
        """,
    )

    documents: List[DocumentReference] = Field(
        default_factory=list,
        description="""
            A list of document references
        """,
    )

    records: List[RecordReference] = Field(
        default_factory=list,
        description="""
            A list of records references from databases or other sources
        """,
    )

    date: str = Field(
        default="", description="When in the point of time mineral inventory valid"
    )
    zone: str = Field(
        default="",
        description="zone of mineral site where inventory item was discovered",
    )


class MineralSite(BaseModel):
    id: str = Field(description="Mineral Site Id")
    source_id: str = Field(
        default="",
        description="Source dataset that the site info is retrieved from. e.g., MRDS",
    )
    record_id: str = Field(
        default="",
        description="Unique ID of the record that the info is retrieved from e.g., 10022920",
    )
    name: str = Field(default="", description="Name of the mine, e.g., Tungsten Jim")

    site_rank: str = Field(default="")
    site_type: str = Field(default="")
    country: List[str] = Field(default_factory=list)
    province: List[str] = Field(default_factory=list)
    location: Optional[GeoLocationInfo] = Field(default=None)
    mineral_inventory: List[MineralInventory] = Field(
        default_factory=list,
        description="""
            A list of mineral inventories
        """,
    )

    deposit_type_candidate: List[DepositTypeCandidate] = Field(
        default_factory=list,
        description="""
            A list of deposit types candidates
        """,
    )

    validated: bool = Field(False, description="Validated by human")

    system: str = Field(
        ...,
        description="""
            The name of the system used.
        """,
    )
    system_version: str = Field(
        ...,
        description="""
            The version of the system used.
        """,
    )


class Reference(BaseModel):
    document_uri: str = Field(description="URL of the document")
    comment: str = Field(description="Comment")


class DedupSiteRecord(BaseModel):
    mineral_site_id: str = Field(description="original mineral site id")
    score: float = Field(description="score of the site")
    reference: List[Reference] = Field(description="Provenance of the site")


class DedupSiteLocation(BaseModel):
    latitude: Optional[float] = Field(
        default=None, description="Latitude (decimal, EPSG:4326)"
    )
    longitude: Optional[float] = Field(
        default=None, description="Longitude (decimal, EPSG:4326)"
    )
    country: List[str] = Field(
        default_factory=list, description="The country that the site is located in"
    )
    state_or_province: List[str] = Field(
        default_factory=list,
        description="The state or province that the site is located in",
    )


class SiteGradeTonnage(BaseModel):
    commodity_id: str = Field(description="Commodity ID")
    contained_metal: Optional[float] = Field(
        default=None, description="Total contained metal"
    )
    tonnage: Optional[float] = Field(default=None, description="Total tonnage")
    grade: Optional[float] = Field(default=None, description="Total grade")
    tonnage_unit_id: Optional[str] = Field(default=None, description="Tonnage unit ID")
    grade_unit_id: Optional[str] = Field(default=None, description="Grade unit ID")


class DedupSite(BaseModel):
    id: Optional[str] = Field(default=None, description="dedup mineral site id")
    sites: List[DedupSiteRecord] = Field(
        default_factory=list, description="Mineral Sites"
    )
    name: str = Field(description="Dedup site name")
    type: str = Field(description="Dedup site type")
    rank: str = Field(description="Dedup site rank")
    location: DedupSiteLocation = Field(description="Dedup site location")
    deposit_types: List[DepositTypeCandidate] = Field(
        default_factory=list, description="Deposit Types"
    )
    grade_tonnage: List[SiteGradeTonnage] = Field(
        default_factory=list, description="Grade Tonnage"
    )

    system: str = Field(..., description="The name of the system used.")
    system_version: str = Field(..., description="The version of the system used.")
    data_snapshot: str = Field(..., description="version of data")
    data_snapshot_date: str = Field(..., description="date of data")
