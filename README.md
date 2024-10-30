


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

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    Area_Extraction ..> AreaType
    Area_Extraction ..> GeomType


```

</details>

### Georeference

<details open>
    <summary>georeference</summary>

```mermaid
classDiagram

    class GeoreferenceResults {
        cog_id: str
        georeference_results: list[GeoreferenceResult] = list
        gcps: list[GroundControlPoint] = list
        system: str
        system_version: str
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class GeoreferenceResult {
        likely_CRSs: list[str] = list
        map_area: Area_Extraction | None = None
        projections: list[ProjectionResult] = list
    }

    class Pixel_Point {
        rows_from_top: float | int
        columns_from_left: float | int
        type: GeomType = GeomType.Point
    }

    class ProjectionResult {
        crs: str
        gcp_ids: list[str]
        file_name: str
        validated: bool = False
    }

    class Geom_Point {
        latitude: float | int | None
        longitude: float | int | None
        type: GeomType = GeomType.Point
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

    class GroundControlPoint {
        gcp_id: str
        map_geom: Geom_Point
        px_geom: Pixel_Point
        confidence: float | int | None = None
        model: str
        model_version: str
        crs: str
    }

    Area_Extraction ..> AreaType
    Area_Extraction ..> GeomType
    Geom_Point ..> GeomType
    Pixel_Point ..> GeomType
    GroundControlPoint ..> Pixel_Point
    GroundControlPoint ..> Geom_Point
    GeoreferenceResult ..> Area_Extraction
    GeoreferenceResult ..> ProjectionResult
    GeoreferenceResults ..> GeoreferenceResult
    GeoreferenceResults ..> GroundControlPoint


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

    Area_Extraction ..> AreaType
    Area_Extraction ..> GeomType
    LineLegendAndFeaturesResult ..> LineFeatureCollection
    LineLegendAndFeaturesResult ..> ModelProvenance
    PointLegendAndFeaturesResult ..> ModelProvenance
    PointLegendAndFeaturesResult ..> PointFeatureCollection
    PolygonLegendAndFeaturesResult ..> MapUnit
    PolygonLegendAndFeaturesResult ..> ModelProvenance
    PolygonLegendAndFeaturesResult ..> PolygonFeatureCollection
    CogMetaData ..> MapMetaData
    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> Area_Extraction
    FeatureResults ..> CogMetaData
    FeatureResults ..> PolygonLegendAndFeaturesResult


```

</details>

### Point Feature

<details open>
    <summary>point feature</summary>

```mermaid
classDiagram

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class PointFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Point
        properties: PointProperties
    }

    class Point {
        coordinates: list[float | int]
        type: GeomType = GeomType.Point
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

    class ModelProvenance {
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class PointFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PointFeature] = list
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

    Point ..> GeomType
    PointFeature ..> Point
    PointFeature ..> PointProperties
    PointFeature ..> GeoJsonType
    PointFeatureCollection ..> GeoJsonType
    PointFeatureCollection ..> PointFeature
    PointLegendAndFeaturesResult ..> ModelProvenance
    PointLegendAndFeaturesResult ..> PointFeatureCollection


```

</details>

### Line Feature

<details open>
    <summary>line feature</summary>

```mermaid
classDiagram

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class LineFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[LineFeature] = list
    }

    class DashType {
        <<Enumeration>>
        none: str = ''
        solid: str = 'solid'
        dash: str = 'dash'
        dotted: str = 'dotted'
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

    Line ..> GeomType
    LineProperties ..> DashType
    LineFeature ..> Line
    LineFeature ..> GeoJsonType
    LineFeature ..> LineProperties
    LineFeatureCollection ..> LineFeature
    LineFeatureCollection ..> GeoJsonType
    LineLegendAndFeaturesResult ..> LineFeatureCollection
    LineLegendAndFeaturesResult ..> ModelProvenance


```

</details>

### Polygon Feature

<details open>
    <summary>polygon feature</summary>

```mermaid
classDiagram

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class PolygonProperties {
        model: str
        model_version: str
        reference_id: str = ''
        validated: bool | None = None
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

    class Polygon {
        coordinates: list[list[list[float | int]]]
        type: GeomType = GeomType.Polygon
    }

    class ModelProvenance {
        model: str
        model_version: str
        confidence: float | int | None = None
    }

    class PolygonFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PolygonFeature] = list
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
    PolygonLegendAndFeaturesResult ..> MapUnit
    PolygonLegendAndFeaturesResult ..> ModelProvenance
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

    class UploadDocument {
        title: str
        is_open: bool = True
        provenance: list[DocumentProvenance] = list
        metadata: DocumentMetaData | None = None
        system: str
        system_version: str
    }

    UploadDocument ..> DocumentMetaData
    UploadDocument ..> DocumentProvenance
    Document ..> DocumentMetaData
    Document ..> DocumentProvenance


```

</details>

### Mineral

<details open>
    <summary>mineral</summary>

```mermaid
classDiagram

    class DepositTypeCandidate {
        observed_name: str = ''
        deposit_type_id: str | None = None
        confidence: float | int | None = None
        source: str
    }

    class DocumentReference {
        cdr_id: str
        page: int | None = None
        x_min: float | None = None
        x_max: float | None = None
        y_min: float | None = None
        y_max: float | None = None
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

    class DepositType {
        id: str | None = None
        name: str
        environment: str
        group: str
    }

    class RecordReference {
        record_id: str = ''
        source: str = ''
        uri: str = ''
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

    class GeologyInfo {
        age: str = ''
        unit_name: str = ''
        description: str = ''
        lithology: list[str] = list
        process: list[str] = list
        environment: list[str] = list
        comments: str = ''
    }

    class MappableCriteria {
        criteria: str
        theoretical: str = ''
        potential_dataset: list[EvidenceLayer] = list
        supporting_references: list[DocumentReference]
    }

    class MineralInventoryCategory {
        category: str
        confidence: float | int | None = None
        source: str
    }

    class GeoLocationInfo {
        crs: str
        geom: str
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
    MineralInventory ..> RecordReference
    MineralInventory ..> MineralInventoryCategory
    MineralInventory ..> DocumentReference
    MineralInventory ..> Confidence
    MineralSite ..> DepositTypeCandidate
    MineralSite ..> MineralInventory
    MineralSite ..> GeoLocationInfo
    DedupSite ..> DepositTypeCandidate
    DedupSite ..> DedupSiteRecord


```

</details>

### Map Results

<details open>
    <summary>map results</summary>

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

    class GeoreferenceResults {
        cog_id: str
        georeference_results: list[GeoreferenceResult] = list
        gcps: list[GroundControlPoint] = list
        system: str
        system_version: str
    }

    class MapResults {
        cog_id: str
        georef_results: list[GeoreferenceResults] = list
        extraction_results: list[FeatureResults] = list
    }

    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> Area_Extraction
    FeatureResults ..> CogMetaData
    FeatureResults ..> PolygonLegendAndFeaturesResult
    GeoreferenceResults ..> GeoreferenceResult
    GeoreferenceResults ..> GroundControlPoint
    MapResults ..> FeatureResults
    MapResults ..> GeoreferenceResults


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

    class RawDataType {
        <<Enumeration>>
        MINERAL_SITE: str = 'mineral_site'
        POINT: str = 'point'
        LINE: str = 'line'
        POLYGON: str = 'polygon'
        TIF: str = 'tif'
        VECTOR: str = 'vector'
    }

    class LayerDataType {
        <<Enumeration>>
        CONTINUOUS: str = 'continuous'
        BINARY: str = 'binary'
        CATEGORICAL: str = 'categorical'
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

    class DefineVectorProcessDataLayer {
        label_raster: bool = False
        title: str
        evidence_features: list[DataTypeId] = list
        extra_geometries: list[Point | LineString | Polygon] = list
        transform_methods: list[TransformMethod | Impute | ScalingType] = list
    }

    class SaveProcessedDataLayer {
        cma_id: str
        title: str
        label_raster: bool = False
        raw_data_info: list[DataTypeId] = list
        extra_geometries: list[] = list
        system: str
        system_version: str
        transform_methods: list[TransformMethod | Impute | ScalingType] = list
        event_id: str = ''
    }

    class CreateProcessDataLayers {
        cma_id: str
        system: str
        system_version: str
        evidence_layers: list[DefineProcessDataLayer] = list
        vector_layers: list[DefineVectorProcessDataLayer] = list
    }

    class DataTypeId {
        raw_data_type: RawDataType
        id: str
    }

    class TransformMethod {
        <<Enumeration>>
        LOG: str = 'log'
        ABS: str = 'abs'
        SQRT: str = 'sqrt'
    }

    class LayerCategory {
        <<Enumeration>>
        GEOPHYSICS: str = 'geophysics'
        GEOLOGY: str = 'geology'
        GEOCHEMISTRY: str = 'geochemistry'
    }

    class ImputeMethod {
        <<Enumeration>>
        MEAN: str = 'mean'
        MEDIAN: str = 'median'
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

    class CreateCriticalMineralAssessment {
        crs: str
        extent: MultiPolygon
        resolution: list[float | int]
        mineral: str
        description: str
        creation_date: datetime = now
    }

    class Polygon {
        bbox: tuple[float, float, float, float] | tuple[float, float, float, float, float, float] | None = None
        type: Literal['Polygon']
        coordinates: list[list[Position2D | Position3D]]
    }

    class DataFormat {
        <<Enumeration>>
        TIF: str = 'tif'
        SHP: str = 'shp'
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

    class Point {
        bbox: tuple[float, float, float, float] | tuple[float, float, float, float, float, float] | None = None
        type: Literal['Point']
        coordinates: Position2D | Position3D
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
        evidence_layers: list[str]
    }

    class ScalingType {
        <<Enumeration>>
        MINMAX: str = 'minmax'
        MAXABS: str = 'maxabs'
        STANDARD: str = 'standard'
    }

    class LineString {
        bbox: tuple[float, float, float, float] | tuple[float, float, float, float, float, float] | None = None
        type: Literal['LineString']
        coordinates: list[Position2D | Position3D]
    }

    class MultiPolygon {
        bbox: tuple[float, float, float, float] | tuple[float, float, float, float, float, float] | None = None
        type: Literal['MultiPolygon']
        coordinates: list[list[list[Position2D | Position3D]]]
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

    class Impute {
        impute_method: ImputeMethod
        window_size: list[int] = [3, 3]
    }

    class DefineProcessDataLayer {
        data_source_id: str
        title: str
        transform_methods: list[TransformMethod | Impute | ScalingType] = list
        label_raster: bool = False
    }

    LineString ..> Position3D
    LineString ..> Position2D
    MultiPolygon ..> Position3D
    MultiPolygon ..> Position2D
    Point ..> Position3D
    Point ..> Position2D
    Polygon ..> Position3D
    Polygon ..> Position2D
    SOMTrainConfig ..> SOMType
    SOMTrainConfig ..> NeighborhoodDecay
    SOMTrainConfig ..> SOMGrid
    SOMTrainConfig ..> NeighborhoodFunction
    SOMTrainConfig ..> LearningRateDecay
    SOMTrainConfig ..> SOMInitialization
    Impute ..> ImputeMethod
    CreateDataSource ..> LayerCategory
    CreateDataSource ..> LayerDataType
    CreateDataSource ..> DataFormat
    CreateCriticalMineralAssessment ..> datetime
    CreateCriticalMineralAssessment ..> MultiPolygon
    DefineProcessDataLayer ..> ScalingType
    DefineProcessDataLayer ..> TransformMethod
    DefineProcessDataLayer ..> Impute
    DataTypeId ..> RawDataType
    SaveProcessedDataLayer ..> DataTypeId
    SaveProcessedDataLayer ..> ScalingType
    SaveProcessedDataLayer ..> TransformMethod
    SaveProcessedDataLayer ..> Impute
    DefineVectorProcessDataLayer ..> Point
    DefineVectorProcessDataLayer ..> ScalingType
    DefineVectorProcessDataLayer ..> LineString
    DefineVectorProcessDataLayer ..> Impute
    DefineVectorProcessDataLayer ..> DataTypeId
    DefineVectorProcessDataLayer ..> TransformMethod
    DefineVectorProcessDataLayer ..> Polygon
    CreateProspectModelMetaData ..> SOMTrainConfig
    CreateProspectModelMetaData ..> NeuralNetUserOptions
    CreateProcessDataLayers ..> DefineVectorProcessDataLayer
    CreateProcessDataLayers ..> DefineProcessDataLayer
    DataSource ..> LayerCategory
    DataSource ..> LayerDataType
    DataSource ..> tuple
    DataSource ..> DataFormat


```

</details>

### Prospectivity Models

<details open>
    <summary>prospectivity models</summary>

```mermaid
classDiagram

    class SOMType {
        <<Enumeration>>
        TOROID: str = 'toroid'
        SHEET: str = 'sheet'
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

    class SOMInitialization {
        <<Enumeration>>
        RANDOM: str = 'random'
        PCA: str = 'pca'
    }

    class NeighborhoodDecay {
        <<Enumeration>>
        LINEAR: str = 'linear'
        EXPONENTIAL: str = 'exponential'
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

    class SOMGrid {
        <<Enumeration>>
        HEXAGONAL: str = 'hexagonal'
        RECTANGULAR: str = 'rectangular'
    }

    class RFUserOptions {
        n_estimators: int | None = 100
        n_unlabeled: int | None = 40000
    }

    class NeighborhoodFunction {
        <<Enumeration>>
        GAUSSIAN: str = 'gaussian'
        BUBBLE: str = 'bubble'
    }

    class LearningRateDecay {
        <<Enumeration>>
        LINEAR: str = 'linear'
        EXPONENTIAL: str = 'exponential'
    }

    SOMTrainConfig ..> SOMType
    SOMTrainConfig ..> NeighborhoodDecay
    SOMTrainConfig ..> SOMGrid
    SOMTrainConfig ..> NeighborhoodFunction
    SOMTrainConfig ..> LearningRateDecay
    SOMTrainConfig ..> SOMInitialization


```

</details>
<!--#+END_SCHEMA-->
