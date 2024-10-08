


# CDR Schemas


## Development

Formatting Code
```
poetry run format
```


Verify Changes
```
# verify types (mypy)
poetry run types

# lint
poetry run lint
```

Build local package

```
poetry build -f sdist
```


Update Schema Diagrams

To generate schemas you will need to run `poetry install --with docs` to install the proper dependencies

```
poetry run docs
```

<!--#+BEGIN_SCHEMA-->
<!-- this sections is autogenerated -->



## Schemas

   [Area Extraction](#Area-Extraction)<br/>
   [Cog Metadata](#Cog-Metadata)<br/>
   [Document](#Document)<br/>
   [Feature Results](#Feature-Results)<br/>
   [Georeference](#Georeference)<br/>
   [Line Feature](#Line-Feature)<br/>
   [Map](#Map)<br/>
   [Map Results](#Map-Results)<br/>
   [Metadata](#Metadata)<br/>
   [Mineral](#Mineral)<br/>
   [Point Feature](#Point-Feature)<br/>
   [Polygon Feature](#Polygon-Feature)<br/>
   [Prospectivity Input](#Prospectivity-Input)<br/>
   [Prospectivity Models](#Prospectivity-Models)<br/>



### Area Extraction

<details open>
    <summary>area extraction</summary>

```mermaid
classDiagram

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class AreaType {
        <<Enumeration>>
        Map_Area: str = 'map_area'
        Legend_Area: str = 'legend_area'
        CrossSection: str = 'cross_section'
        OCR: str = 'ocr'
        Polygon_Legend_Area: str = 'polygon_legend_area'
        Line_Point_Legend_Area: str = 'line_point_legend_area'
        Line_Legend_Area: str = 'line_legend_area'
        Point_Legend_Area: str = 'point_legend_area'
        Correlation_Diagram: str = 'correlation_diagram'
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[float | int]]]
        bbox: list[float | int] = list
        category: AreaType
        text: str = ''
        reference_id: str = ''
        validated: bool = False
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType


```

</details>

### Georeference

<details open>
    <summary>georeference</summary>

```mermaid
classDiagram

    class Geom_Point {
        latitude: float | int | None
        longitude: float | int | None
        type: GeomType = GeomType.Point
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class Pixel_Point {
        rows_from_top: float | int
        columns_from_left: float | int
        type: GeomType = GeomType.Point
    }

    class GeoreferenceResults {
        cog_id: str
        georeference_results: list[GeoreferenceResult] = list
        gcps: list[GroundControlPoint] = list
        system: str
        system_version: str
    }

    class GroundControlPoint {
        gcp_id: str
        map_geom: Geom_Point
        px_geom: Pixel_Point
        confidence: float | int | None = None
        model: str
        model_version: str
        crs: str
    }

    class GeoreferenceResult {
        likely_CRSs: list[str] = list
        map_area: Area_Extraction | None = None
        projections: list[ProjectionResult] = list
    }

    class ProjectionResult {
        crs: str
        gcp_ids: list[str]
        file_name: str
        validated: bool = False
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[float | int]]]
        bbox: list[float | int] = list
        category: AreaType
        text: str = ''
        reference_id: str = ''
        validated: bool = False
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType
    Geom_Point ..> GeomType
    Pixel_Point ..> GeomType
    GroundControlPoint ..> Geom_Point
    GroundControlPoint ..> Pixel_Point
    GeoreferenceResult ..> ProjectionResult
    GeoreferenceResult ..> Area_Extraction
    GeoreferenceResults ..> GroundControlPoint
    GeoreferenceResults ..> GeoreferenceResult


```

</details>

### Metadata

<details open>
    <summary>metadata</summary>

```mermaid
classDiagram

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
    }

    class MapMetaData {
        title: str = ''
        year: int | None = None
        crs: str = ''
        authors: list[str] = list
        organization: str = ''
        scale: int | None = None
        quadrangle_name: str = ''
        map_shape: MapShapeTypes | None = None
        map_color_scheme: MapColorSchemeTypes | None = None
        publisher: str = ''
        state: str = ''
        model: str
        model_version: str
    }

    class MapColorSchemeTypes {
        <<Enumeration>>
        full_color: str = 'full_color'
        monochrome: str = 'monochrome'
        grayscale: str = 'grayscale'
    }

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: bool | None = None
        map_metadata: list[MapMetaData] = list
    }

    MapMetaData ..> MapShapeTypes
    MapMetaData ..> MapColorSchemeTypes
    CogMetaData ..> MapMetaData


```

</details>

### Feature Results

<details open>
    <summary>feature results</summary>

```mermaid
classDiagram

    class FeatureResults {
        system: str
        system_version: str
        cog_id: str
        line_feature_results: list[LineLegendAndFeaturesResult] = list
        point_feature_results: list[PointLegendAndFeaturesResult] = list
        polygon_feature_results: list[PolygonLegendAndFeaturesResult] = list
        cog_area_extractions: list[Area_Extraction] = list
        cog_metadata_extractions: list[CogMetaData] = list
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[float | int]]]
        bbox: list[float | int] = list
        category: AreaType
        text: str = ''
        reference_id: str = ''
        validated: bool = False
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: bool | None = None
        map_metadata: list[MapMetaData] = list
    }

    class LineLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        name: str = ''
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        line_features: LineFeatureCollection | None = None
    }

    class PolygonLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        label: str
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        color: str = ''
        pattern: str = ''
        category: str = ''
        map_unit: list[MapUnit] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        polygon_features: PolygonFeatureCollection | None = None
    }

    class PointLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        name: str
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        point_features: PointFeatureCollection | None = None
    }

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType
    LineLegendAndFeaturesResult ..> ModelProvenance
    LineLegendAndFeaturesResult ..> LineFeatureCollection
    PointLegendAndFeaturesResult ..> ModelProvenance
    PointLegendAndFeaturesResult ..> PointFeatureCollection
    PolygonLegendAndFeaturesResult ..> ModelProvenance
    PolygonLegendAndFeaturesResult ..> MapUnit
    PolygonLegendAndFeaturesResult ..> PolygonFeatureCollection
    CogMetaData ..> MapMetaData
    FeatureResults ..> Area_Extraction
    FeatureResults ..> CogMetaData
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> PolygonLegendAndFeaturesResult
    FeatureResults ..> PointLegendAndFeaturesResult


```

</details>

### Point Feature

<details open>
    <summary>point feature</summary>

```mermaid
classDiagram

    class PointFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PointFeature] = list
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class Point {
        coordinates: list[float | int]
        type: GeomType = GeomType.Point
    }

    class ModelProvenance {
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class PointFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Point
        properties: PointProperties
    }

    class PointProperties {
        model: str
        model_version: str
        confidence: float | int | None = None
        bbox: list[float | int] = list
        dip: int | None = None
        dip_direction: int | None = None
        reference_id: str = ''
        validated: bool | None = None
    }

    class PointLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        name: str
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        point_features: PointFeatureCollection | None = None
    }

    Point ..> GeomType
    PointFeature ..> Point
    PointFeature ..> PointProperties
    PointFeature ..> GeoJsonType
    PointFeatureCollection ..> PointFeature
    PointFeatureCollection ..> GeoJsonType
    PointLegendAndFeaturesResult ..> ModelProvenance
    PointLegendAndFeaturesResult ..> PointFeatureCollection


```

</details>

### Line Feature

<details open>
    <summary>line feature</summary>

```mermaid
classDiagram

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class DashType {
        <<Enumeration>>
        none: str = ''
        solid: str = 'solid'
        dash: str = 'dash'
        dotted: str = 'dotted'
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class LineLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        name: str = ''
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        line_features: LineFeatureCollection | None = None
    }

    class ModelProvenance {
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class LineFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[LineFeature] = list
    }

    class LineProperties {
        model: str
        model_version: str
        confidence: float | int | None = None
        dash_pattern: DashType = DashType.none
        symbol: str = ''
        reference_id: str = ''
        validated: bool | None = None
    }

    class LineFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Line
        properties: LineProperties
    }

    class Line {
        coordinates: list[list[float | int]]
        type: GeomType = GeomType.LineString
    }

    Line ..> GeomType
    LineProperties ..> DashType
    LineFeature ..> Line
    LineFeature ..> LineProperties
    LineFeature ..> GeoJsonType
    LineFeatureCollection ..> LineFeature
    LineFeatureCollection ..> GeoJsonType
    LineLegendAndFeaturesResult ..> ModelProvenance
    LineLegendAndFeaturesResult ..> LineFeatureCollection


```

</details>

### Polygon Feature

<details open>
    <summary>polygon feature</summary>

```mermaid
classDiagram

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class PolygonFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PolygonFeature] = list
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class PolygonProperties {
        model: str
        model_version: str
        reference_id: str = ''
        validated: bool | None = None
        confidence: float | int | None = None
    }

    class Polygon {
        coordinates: list[list[list[float | int]]]
        type: GeomType = GeomType.Polygon
    }

    class ModelProvenance {
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class PolygonFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Polygon
        properties: PolygonProperties
    }

    class MapUnit {
        age_text: str = ''
        b_age: float | None = None
        b_interval: str = ''
        lithology: str = ''
        name: str = ''
        t_age: float | None = None
        t_interval: str = ''
        comments: str = ''
    }

    class PolygonLegendAndFeaturesResult {
        id: str
        legend_provenance: ModelProvenance | None = None
        label: str
        abbreviation: str = ''
        description: str = ''
        legend_bbox: list[float | int] = list
        legend_contour: list[list[float | int]] = list
        color: str = ''
        pattern: str = ''
        category: str = ''
        map_unit: list[MapUnit] = list
        reference_id: str = ''
        validated: bool | None = None
        crs: str = 'pixel'
        cdr_projection_id: str = ''
        polygon_features: PolygonFeatureCollection | None = None
    }

    Polygon ..> GeomType
    PolygonFeature ..> PolygonProperties
    PolygonFeature ..> Polygon
    PolygonFeature ..> GeoJsonType
    PolygonFeatureCollection ..> PolygonFeature
    PolygonFeatureCollection ..> GeoJsonType
    PolygonLegendAndFeaturesResult ..> ModelProvenance
    PolygonLegendAndFeaturesResult ..> MapUnit
    PolygonLegendAndFeaturesResult ..> PolygonFeatureCollection


```

</details>

### Cog Metadata

<details open>
    <summary>cog metadata</summary>

```mermaid
classDiagram

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
    }

    class MapMetaData {
        title: str = ''
        year: int | None = None
        crs: str = ''
        authors: list[str] = list
        organization: str = ''
        scale: int | None = None
        quadrangle_name: str = ''
        map_shape: MapShapeTypes | None = None
        map_color_scheme: MapColorSchemeTypes | None = None
        publisher: str = ''
        state: str = ''
        model: str
        model_version: str
    }

    class MapColorSchemeTypes {
        <<Enumeration>>
        full_color: str = 'full_color'
        monochrome: str = 'monochrome'
        grayscale: str = 'grayscale'
    }

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: bool | None = None
        map_metadata: list[MapMetaData] = list
    }

    MapMetaData ..> MapShapeTypes
    MapMetaData ..> MapColorSchemeTypes
    CogMetaData ..> MapMetaData


```

</details>

### Document

<details open>
    <summary>document</summary>

```mermaid
classDiagram

    class UploadDocument {
        title: str
        is_open: bool = True
        provenance: list[DocumentProvenance] = list
        metadata: DocumentMetaData | None = None
        system: str
        system_version: str
    }

    class DocumentMetaData {
        doi: str = ''
        authors: list[str] = list
        journal: str = ''
        year: int | None = None
        month: int | None = None
        volume: int | None = None
        issue: str = ''
        description: str = ''
        publisher: str = ''
    }

    class DocumentProvenance {
        external_system_name: str
        external_system_id: str = ''
        external_system_url: str = ''
    }

    class DocumentExtraction {
        id: str | None = None
        document_id: str = None
        extraction_type: str
        extraction_label: str
        score: float | None = None
        bbox: tuple[float, float, float, float] | None = None
        page_num: int | None = None
        external_link: str | None = None
        data: dict[] | None = None
        system: str
        system_version: str
    }

    class Document {
        id: str
        title: str
        is_open: bool
        pages: int
        size: int
        provenance: list[DocumentProvenance] = list
        metadata: DocumentMetaData | None = None
        system: str
        system_version: str
    }

    UploadDocument ..> DocumentProvenance
    UploadDocument ..> DocumentMetaData
    Document ..> DocumentProvenance
    Document ..> DocumentMetaData


```

</details>

### Mineral

<details open>
    <summary>mineral</summary>

```mermaid
classDiagram

    class RecordReference {
        record_id: str = ''
        source: str = ''
        uri: str = ''
    }

    class MineralSite {
        id: str
        source_id: str = ''
        record_id: str = ''
        name: str = ''
        site_rank: str = ''
        site_type: str = ''
        country: list[str] = list
        province: list[str] = list
        location: GeoLocationInfo | None = None
        mineral_inventory: list[MineralInventory] = list
        deposit_type_candidate: list[DepositTypeCandidate] = list
        validated: bool = False
        system: str
        system_version: str
    }

    class DedupSite {
        id: str | None = None
        sites: list[DedupSiteRecord] = list
        commodity: str
        contained_metal: float | None = None
        contained_metal_units: str = ''
        tonnage: float | None = None
        tonnage_units: str = ''
        grade: float | None = None
        grade_units: str = ''
        crs: str = ''
        centroid: str | None = ''
        geom: str | None = ''
        deposit_type_candidate: list[DepositTypeCandidate] = list
        system: str
        system_version: str
        data_snapshot: str
        data_snapshot_date: str
    }

    class MappableCriteria {
        criteria: str
        theoretical: str = ''
        potential_dataset: list[EvidenceLayer] = list
        supporting_references: list[DocumentReference]
    }

    class GeologyInfo {
        age: str = ''
        unit_name: str = ''
        description: str = ''
        lithology: list[str] = list
        process: list[str] = list
        environment: list[str] = list
        comments: str = ''
    }

    class DedupSiteRecord {
        id: str | None = None
        mineral_site_id: str
        name: str = ''
        country: str = ''
        province: str = ''
        site_rank: str = ''
        site_type: str = ''
    }

    class Confidence {
        confidence: float | int | None = None
        source: str
    }

    class MineralInventoryCategory {
        category: str
        confidence: float | int | None = None
        source: str
    }

    class MineralInventory {
        contained_metal: float | None = None
        commodity: str = ''
        commodity_observed_name: str = ''
        ore_unit: str = ''
        ore_value: float | None = None
        grade_unit: str = ''
        grade_value: float | None = None
        cutoff_grade_unit: str = ''
        cutoff_grade_value: float | None = None
        material_form: float | None = None
        material_form_unit: str = ''
        material_form_conversion: float | None = None
        confidence: Confidence | None = None
        categories: list[MineralInventoryCategory] = list
        documents: list[DocumentReference] = list
        records: list[RecordReference] = list
        date: str = ''
        zone: str = ''
    }

    class GeoLocationInfo {
        crs: str
        geom: str
    }

    class DocumentReference {
        cdr_id: str
        page: int | None = None
        x_min: float | None = None
        x_max: float | None = None
        y_min: float | None = None
        y_max: float | None = None
    }

    class DepositTypeCandidate {
        observed_name: str = ''
        deposit_type_id: str | None = None
        confidence: float | int | None = None
        source: str
    }

    class DepositType {
        id: str | None = None
        name: str
        environment: str
        group: str
    }

    class MineralSystem {
        deposit_type: list[str] = list
        source: list[MappableCriteria] = list
        pathway: list[MappableCriteria] = list
        trap: list[MappableCriteria] = list
        preservation: list[MappableCriteria] = list
        energy: list[MappableCriteria] = list
        outflow: list[MappableCriteria] = list
    }

    class EvidenceLayer {
        name: str = ''
        relevance_score: float
    }

    MappableCriteria ..> DocumentReference
    MappableCriteria ..> EvidenceLayer
    MineralSystem ..> MappableCriteria
    MineralInventory ..> Confidence
    MineralInventory ..> MineralInventoryCategory
    MineralInventory ..> DocumentReference
    MineralInventory ..> RecordReference
    MineralSite ..> MineralInventory
    MineralSite ..> GeoLocationInfo
    MineralSite ..> DepositTypeCandidate
    DedupSite ..> DedupSiteRecord
    DedupSite ..> DepositTypeCandidate


```

</details>

### Map Results

<details open>
    <summary>map results</summary>

```mermaid
classDiagram

    class MapResults {
        cog_id: str
        georef_results: list[GeoreferenceResults] = list
        extraction_results: list[FeatureResults] = list
    }

    class GeoreferenceResults {
        cog_id: str
        georeference_results: list[GeoreferenceResult] = list
        gcps: list[GroundControlPoint] = list
        system: str
        system_version: str
    }

    class FeatureResults {
        system: str
        system_version: str
        cog_id: str
        line_feature_results: list[LineLegendAndFeaturesResult] = list
        point_feature_results: list[PointLegendAndFeaturesResult] = list
        polygon_feature_results: list[PolygonLegendAndFeaturesResult] = list
        cog_area_extractions: list[Area_Extraction] = list
        cog_metadata_extractions: list[CogMetaData] = list
    }

    FeatureResults ..> Area_Extraction
    FeatureResults ..> CogMetaData
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> PolygonLegendAndFeaturesResult
    FeatureResults ..> PointLegendAndFeaturesResult
    GeoreferenceResults ..> GroundControlPoint
    GeoreferenceResults ..> GeoreferenceResult
    MapResults ..> GeoreferenceResults
    MapResults ..> FeatureResults


```

</details>

### Map

<details open>
    <summary>map</summary>

```mermaid
classDiagram

    class Map {
        id: str
        provenance: list[MapProvenance] = list
        is_open: bool
        system: str
        system_version: str
    }

    class MapProvenance {
        system_name: str
        id: str = None
        url: str = None
    }

    Map ..> MapProvenance


```

</details>

### Prospectivity Input

<details open>
    <summary>prospectivity input</summary>

```mermaid
classDiagram

    class LayerCategory {
        <<Enumeration>>
        GEOPHYSICS: str = 'geophysics'
        GEOLOGY: str = 'geology'
        GEOCHEMISTRY: str = 'geochemistry'
    }

    class LayerDataType {
        <<Enumeration>>
        CONTINUOUS: str = 'continuous'
        BINARY: str = 'binary'
        CATEGORICAL: str = 'categorical'
    }

    class Impute {
        impute_method: ImputeMethod
        window_size: list[int] = [3, 3]
    }

    class CreateCriticalMineralAssessment {
        crs: str
        extent: MultiPolygon
        resolution: list[float | int]
        mineral: str
        description: str
        creation_date: datetime = now
    }

    class SaveProcessedDataLayer {
        model_run_id: str
        data_source_id: str
        cma_id: str
        title: str
        system: str
        system_version: str
        transform_methods: list[TransformMethod | Impute | ScalingType] = ''
    }

    class DataSource {
        DOI: str | None
        authors: list[str] | None
        publication_date: str | None
        category: LayerCategory | str | None
        subcategory: str | None
        description: str | None
        derivative_ops: str | None
        type: LayerDataType
        resolution: tuple | None
        format: DataFormat
        download_url: str | None
    }

    class NeuralNetUserOptions {
        likely_negative_range: tuple[float, float] | None = (0.1, 1.0)
        fraction_train_split: float | None = 0.8
        upsample_multiplier: float | None = 20.0
        dropout_tuple: tuple[float, float, float] | None = (0.0, 0.25, 0.25)
        learning_rate: float | None = 0.001
        weight_decay: float | None = 0.01
        smoothing: float | None = 0.3
    }

    class TransformMethod {
        <<Enumeration>>
        LOG: str = 'log'
        ABS: str = 'abs'
        SQRT: str = 'sqrt'
    }

    class CreateProspectModelMetaData {
        cma_id: str
        system: str
        system_version: str
        author: str = ''
        date: str = ''
        organization: str = ''
        model_type: str
        train_config: SOMTrainConfig | NeuralNetUserOptions
        evidence_layers: list[DefineProcessDataLayer]
    }

    class ScalingType {
        <<Enumeration>>
        MINMAX: str = 'minmax'
        MAXABS: str = 'maxabs'
        STANDARD: str = 'standard'
    }

    class SOMTrainConfig {
        size: int = 20
        dimensions_x: int | None = 20
        dimensions_y: int | None = 20
        num_initializations: int | None = 5
        num_epochs: int = 10
        grid_type: SOMGrid | None = 'rectangular'
        som_type: SOMType | None = 'toroid'
        som_initialization: SOMInitialization | None = 'random'
        initial_neighborhood_size: float | None = 0.0
        final_neighborhood_size: float | None = 1.0
        neighborhood_function: NeighborhoodFunction | None = 'gaussian'
        gaussian_neighborhood_coefficient: float | None = 0.5
        learning_rate_decay: LearningRateDecay | None = 'linear'
        neighborhood_decay: NeighborhoodDecay | None = 'linear'
        initial_learning_rate: float | None
        final_learning_rate: float | None
    }

    class MultiPolygon {
        bbox: tuple[float, float, float, float] | tuple[float, float, float, float, float, float] | None = None
        type: Literal['MultiPolygon']
        coordinates: list[list[list[Position2D | Position3D]]]
    }

    class DefineProcessDataLayer {
        cma_id: str
        data_source_id: str
        title: str
        transform_methods: list[TransformMethod | Impute | ScalingType] = list
    }

    class CreateDataSource {
        DOI: str = ''
        authors: list[str] = list
        publication_date: str = ''
        category: LayerCategory
        subcategory: str = ''
        description: str = ''
        derivative_ops: str = ''
        type: LayerDataType
        resolution: list[float | int] = list
        format: DataFormat
        reference_url: str = ''
        evidence_layer_raster_prefix: str = ''
    }

    class ImputeMethod {
        <<Enumeration>>
        MEAN: str = 'mean'
        MEDIAN: str = 'median'
    }

    class ProspectivityOutputLayer {
        system: str
        system_version: str
        model: str = ''
        model_version: str = ''
        model_run_id: str
        output_type: str
        cma_id: str
        title: str
    }

    class DataFormat {
        <<Enumeration>>
        TIF: str = 'tif'
        SHP: str = 'shp'
    }

    MultiPolygon ..> Position2D
    MultiPolygon ..> Position3D
    SOMTrainConfig ..> SOMType
    SOMTrainConfig ..> LearningRateDecay
    SOMTrainConfig ..> SOMInitialization
    SOMTrainConfig ..> NeighborhoodFunction
    SOMTrainConfig ..> SOMGrid
    SOMTrainConfig ..> NeighborhoodDecay
    Impute ..> ImputeMethod
    CreateDataSource ..> LayerDataType
    CreateDataSource ..> LayerCategory
    CreateDataSource ..> DataFormat
    CreateCriticalMineralAssessment ..> datetime
    CreateCriticalMineralAssessment ..> MultiPolygon
    DefineProcessDataLayer ..> TransformMethod
    DefineProcessDataLayer ..> ScalingType
    DefineProcessDataLayer ..> Impute
    SaveProcessedDataLayer ..> TransformMethod
    SaveProcessedDataLayer ..> ScalingType
    SaveProcessedDataLayer ..> Impute
    CreateProspectModelMetaData ..> NeuralNetUserOptions
    CreateProspectModelMetaData ..> SOMTrainConfig
    CreateProspectModelMetaData ..> DefineProcessDataLayer
    DataSource ..> LayerDataType
    DataSource ..> LayerCategory
    DataSource ..> tuple
    DataSource ..> DataFormat


```

</details>

### Prospectivity Models

<details open>
    <summary>prospectivity models</summary>

```mermaid
classDiagram

    class NeuralNetUserOptions {
        likely_negative_range: tuple[float, float] | None = (0.1, 1.0)
        fraction_train_split: float | None = 0.8
        upsample_multiplier: float | None = 20.0
        dropout_tuple: tuple[float, float, float] | None = (0.0, 0.25, 0.25)
        learning_rate: float | None = 0.001
        weight_decay: float | None = 0.01
        smoothing: float | None = 0.3
    }

    class SOMInitialization {
        <<Enumeration>>
        RANDOM: str = 'random'
        PCA: str = 'pca'
    }

    class SOMTrainConfig {
        size: int = 20
        dimensions_x: int | None = 20
        dimensions_y: int | None = 20
        num_initializations: int | None = 5
        num_epochs: int = 10
        grid_type: SOMGrid | None = 'rectangular'
        som_type: SOMType | None = 'toroid'
        som_initialization: SOMInitialization | None = 'random'
        initial_neighborhood_size: float | None = 0.0
        final_neighborhood_size: float | None = 1.0
        neighborhood_function: NeighborhoodFunction | None = 'gaussian'
        gaussian_neighborhood_coefficient: float | None = 0.5
        learning_rate_decay: LearningRateDecay | None = 'linear'
        neighborhood_decay: NeighborhoodDecay | None = 'linear'
        initial_learning_rate: float | None
        final_learning_rate: float | None
    }

    class NeighborhoodDecay {
        <<Enumeration>>
        LINEAR: str = 'linear'
        EXPONENTIAL: str = 'exponential'
    }

    class SOMType {
        <<Enumeration>>
        TOROID: str = 'toroid'
        SHEET: str = 'sheet'
    }

    class LearningRateDecay {
        <<Enumeration>>
        LINEAR: str = 'linear'
        EXPONENTIAL: str = 'exponential'
    }

    class NeighborhoodFunction {
        <<Enumeration>>
        GAUSSIAN: str = 'gaussian'
        BUBBLE: str = 'bubble'
    }

    class SOMGrid {
        <<Enumeration>>
        HEXAGONAL: str = 'hexagonal'
        RECTANGULAR: str = 'rectangular'
    }

    SOMTrainConfig ..> SOMType
    SOMTrainConfig ..> LearningRateDecay
    SOMTrainConfig ..> SOMInitialization
    SOMTrainConfig ..> NeighborhoodFunction
    SOMTrainConfig ..> SOMGrid
    SOMTrainConfig ..> NeighborhoodDecay


```

</details>
<!--#+END_SCHEMA-->
