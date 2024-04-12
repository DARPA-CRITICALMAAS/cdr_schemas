


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
   [Georeference](#Georeference)<br/>
   [Metadata](#Metadata)<br/>
   [Feature Results](#Feature-Results)<br/>
   [Point Feature](#Point-Feature)<br/>
   [Line Feature](#Line-Feature)<br/>
   [Polygon Feature](#Polygon-Feature)<br/>
   [Cog Metadata](#Cog-Metadata)<br/>
   [Document](#Document)<br/>
   [Mineral](#Mineral)<br/>
   [Map Results](#Map-Results)<br/>
   [Map](#Map)<br/>



### Area Extraction

<details open>
    <summary>area extraction</summary>

```mermaid
classDiagram

    class AreaType {
        <<Enumeration>>
        Map_Area: str = 'Map_Area'
        Legend_Area: str = 'Legend_Area'
        CrossSection: str = 'CrossSection'
        OCR: str = 'OCR'
        Polygon_Legend_Area: str = 'Polygon_Legend_Area'
        Line_Point_Legend_Area: str = 'Line_Point_Legend_Area'
        Line_Legend_Area: str = 'Line_Legend_Area'
        Point_Legend_Area: str = 'Point_Legend_Area'
        Correlation_Diagram: str = 'Correlation_Diagram'
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[Union[float, int]]]]
        bbox: Optional[list[Union[float, int]]]
        category: AreaType
        text: Optional[str]
        confidence: Optional[float]
        model: Optional[str]
        model_version: Optional[str]
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

    class GroundControlPoint {
        gcp_id: str
        map_geom: Geom_Point
        px_geom: Pixel_Point
        confidence: Optional[float]
        model: str
        model_version: str
        crs: Optional[str]
    }

    class ProjectionResult {
        crs: str
        gcp_ids: list[str]
        file_name: str
    }

    class GeoreferenceResult {
        likely_CRSs: Optional[list[str]]
        map_area: Optional[Area_Extraction]
        projections: Optional[list[ProjectionResult]]
    }

    class Pixel_Point {
        rows_from_top: Union[float, int]
        columns_from_left: Union[float, int]
        type: GeomType = GeomType.Point
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[Union[float, int]]]]
        bbox: Optional[list[Union[float, int]]]
        category: AreaType
        text: Optional[str]
        confidence: Optional[float]
        model: Optional[str]
        model_version: Optional[str]
    }

    class Geom_Point {
        latitude: Union[float, int, NoneType]
        longitude: Union[float, int, NoneType]
        type: GeomType = GeomType.Point
    }

    class GeoreferenceResults {
        cog_id: str
        georeference_results: Optional[list[GeoreferenceResult]]
        gcps: Optional[list[GroundControlPoint]]
        system: str
        system_version: str
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    Area_Extraction ..> AreaType
    Area_Extraction ..> GeomType
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

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: Optional[bool]
        map_metadata: Optional[list[MapMetaData]]
    }

    class MapColorSchemeTypes {
        <<Enumeration>>
        full_color: str = 'full_color'
        monochrome: str = 'monochrome'
        grayscale: str = 'grayscale'
    }

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
    }

    class MapMetaData {
        title: Optional[str]
        year: Optional[int]
        crs: Optional[str]
        authors: Optional[list[str]]
        organization: Optional[str]
        scale: Optional[int]
        quadrangle_name: Optional[str]
        map_shape: Optional[MapShapeTypes]
        map_color_scheme: Optional[MapColorSchemeTypes]
        publisher: Optional[str]
        state: Optional[str]
        model: str
        model_version: str
    }

    MapMetaData ..> MapColorSchemeTypes
    MapMetaData ..> MapShapeTypes
    CogMetaData ..> MapMetaData


```

</details>

### Feature Results

<details open>
    <summary>feature results</summary>

```mermaid
classDiagram

    class FeatureResults {
        cog_id: str
        line_feature_results: Optional[list[LineLegendAndFeaturesResult]]
        point_feature_results: Optional[list[PointLegendAndFeaturesResult]]
        polygon_feature_results: Optional[list[PolygonLegendAndFeauturesResult]]
        cog_area_extractions: Optional[list[Area_Extraction]]
        cog_metadata_extractions: Optional[list[CogMetaData]]
        system: str
        system_version: str
    }

    class PolygonLegendAndFeauturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        map_unit: Optional[MapUnit]
        abbreviation: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        category: Optional[str]
        color: Optional[str]
        description: Optional[str]
        pattern: Optional[str]
        polygon_features: Optional[PolygonFeatureCollection]
    }

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: Optional[bool]
        map_metadata: Optional[list[MapMetaData]]
    }

    class PointLegendAndFeaturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        name: Optional[str]
        description: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        point_features: Optional[list[PointFeatureCollection]]
    }

    class LineLegendAndFeaturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        name: Optional[str]
        description: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        line_features: Optional[LineFeatureCollection]
    }

    class Area_Extraction {
        type: GeomType = GeomType.Polygon
        coordinates: list[list[list[Union[float, int]]]]
        bbox: Optional[list[Union[float, int]]]
        category: AreaType
        text: Optional[str]
        confidence: Optional[float]
        model: Optional[str]
        model_version: Optional[str]
    }

    Area_Extraction ..> AreaType
    Area_Extraction ..> GeomType
    LineLegendAndFeaturesResult ..> LineFeatureCollection
    PointLegendAndFeaturesResult ..> PointFeatureCollection
    PolygonLegendAndFeauturesResult ..> PolygonFeatureCollection
    PolygonLegendAndFeauturesResult ..> MapUnit
    CogMetaData ..> MapMetaData
    FeatureResults ..> PolygonLegendAndFeauturesResult
    FeatureResults ..> CogMetaData
    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> Area_Extraction


```

</details>

### Point Feature

<details open>
    <summary>point feature</summary>

```mermaid
classDiagram

    class PointLegendAndFeaturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        name: Optional[str]
        description: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        point_features: Optional[list[PointFeatureCollection]]
    }

    class Point {
        coordinates: list[Union[float, int]]
        type: GeomType = GeomType.Point
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class PointProperties {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
        bbox: Optional[list[Union[float, int]]]
        dip: Optional[int]
        dip_direction: Optional[int]
    }

    class PointFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Point
        properties: PointProperties
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class PointFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PointFeature]
    }

    Point ..> GeomType
    PointFeature ..> PointProperties
    PointFeature ..> Point
    PointFeature ..> GeoJsonType
    PointFeatureCollection ..> PointFeature
    PointFeatureCollection ..> GeoJsonType
    PointLegendAndFeaturesResult ..> PointFeatureCollection


```

</details>

### Line Feature

<details open>
    <summary>line feature</summary>

```mermaid
classDiagram

    class LineFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Line
        properties: LineProperty
    }

    class DashType {
        <<Enumeration>>
        solid: str = 'solid'
        dash: str = 'dash'
        dotted: str = 'dotted'
    }

    class LineLegendAndFeaturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        name: Optional[str]
        description: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        line_features: Optional[LineFeatureCollection]
    }

    class LineProperty {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
        dash_pattern: Optional[DashType] = None
        symbol: Optional[str]
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class LineFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: Optional[list[LineFeature]]
    }

    class Line {
        coordinates: list[list[Union[float, int]]]
        type: GeomType = GeomType.LineString
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    Line ..> GeomType
    LineProperty ..> DashType
    LineFeature ..> LineProperty
    LineFeature ..> Line
    LineFeature ..> GeoJsonType
    LineFeatureCollection ..> LineFeature
    LineFeatureCollection ..> GeoJsonType
    LineLegendAndFeaturesResult ..> LineFeatureCollection


```

</details>

### Polygon Feature

<details open>
    <summary>polygon feature</summary>

```mermaid
classDiagram

    class PolygonLegendAndFeauturesResult {
        id: str
        crs: str
        cdr_projection_id: Optional[str]
        map_unit: Optional[MapUnit]
        abbreviation: Optional[str]
        legend_bbox: Optional[list[Union[float, int]]]
        category: Optional[str]
        color: Optional[str]
        description: Optional[str]
        pattern: Optional[str]
        polygon_features: Optional[PolygonFeatureCollection]
    }

    class PolygonProperty {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
    }

    class Polygon {
        coordinates: list[list[list[Union[float, int]]]]
        type: GeomType = GeomType.Polygon
    }

    class PolygonFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Polygon
        properties: PolygonProperty
    }

    class MapUnit {
        age_text: Optional[str]
        b_age: Optional[float]
        b_interval: Optional[str]
        lithology: Optional[str]
        name: Optional[str]
        t_age: Optional[float]
        t_interval: Optional[str]
        comments: Optional[str]
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
    }

    class PolygonFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: Optional[list[PolygonFeature]]
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    Polygon ..> GeomType
    PolygonFeature ..> Polygon
    PolygonFeature ..> PolygonProperty
    PolygonFeature ..> GeoJsonType
    PolygonFeatureCollection ..> PolygonFeature
    PolygonFeatureCollection ..> GeoJsonType
    PolygonLegendAndFeauturesResult ..> PolygonFeatureCollection
    PolygonLegendAndFeauturesResult ..> MapUnit


```

</details>

### Cog Metadata

<details open>
    <summary>cog metadata</summary>

```mermaid
classDiagram

    class CogMetaData {
        cog_id: str
        system: str
        system_version: str
        multiple_maps: Optional[bool]
        map_metadata: Optional[list[MapMetaData]]
    }

    class MapColorSchemeTypes {
        <<Enumeration>>
        full_color: str = 'full_color'
        monochrome: str = 'monochrome'
        grayscale: str = 'grayscale'
    }

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
    }

    class MapMetaData {
        title: Optional[str]
        year: Optional[int]
        crs: Optional[str]
        authors: Optional[list[str]]
        organization: Optional[str]
        scale: Optional[int]
        quadrangle_name: Optional[str]
        map_shape: Optional[MapShapeTypes]
        map_color_scheme: Optional[MapColorSchemeTypes]
        publisher: Optional[str]
        state: Optional[str]
        model: str
        model_version: str
    }

    MapMetaData ..> MapColorSchemeTypes
    MapMetaData ..> MapShapeTypes
    CogMetaData ..> MapMetaData


```

</details>

### Document

<details open>
    <summary>document</summary>

```mermaid
classDiagram

    class DocumentMetaData {
        doi: str = ''
        authors: list[str] = list
        journal: str = ''
        year: Optional[int] = None
        month: Optional[int] = None
        volume: Optional[int] = None
        issue: Optional[int] = None
        description: str = ''
    }

    class UploadDocument {
        title: str
        is_open: bool = True
        provenance: Optional[DocumentProvenance] = None
        metadata: Optional[DocumentMetaData] = None
        system: str
        system_version: str
    }

    class DocumentProvenance {
        external_system_name: str
        external_system_id: Optional[str] = ''
        external_system_url: Optional[str] = ''
    }

    class Document {
        id: str
        title: str
        is_open: bool
        pages: int
        size: int
        provenance: list[DocumentProvenance] = list
        metadata: Optional[DocumentMetaData] = None
        system: str
        system_version: str
    }

    class DocumentExtraction {
        id: UnionType[str, NoneType] = None
        document_id: str = None
        extraction_type: str
        extraction_label: str
        score: UnionType[float, NoneType] = None
        bbox: UnionType[tuple[float, float, float, float], NoneType] = None
        page_num: UnionType[int, NoneType] = None
        external_link: UnionType[str, NoneType] = None
        data: UnionType[dict, NoneType] = None
        system: str
        system_version: str
    }

    UploadDocument ..> DocumentMetaData
    UploadDocument ..> DocumentProvenance
    Document ..> DocumentMetaData
    Document ..> DocumentProvenance
    DocumentExtraction ..> dict


```

</details>

### Mineral

<details open>
    <summary>mineral</summary>

```mermaid
classDiagram

    class MineralInventory {
        commodity: Commodity
        observed_commodity: Optional[str]
        category: Optional[ResourceReserveCategory]
        ore: Optional[Ore]
        grade: Optional[Grade]
        cutoff_grade: Optional[Grade]
        contained_metal: Optional[float]
        reference: Reference
        date: Optional[datetime]
        zone: Optional[str]
    }

    class Grade {
        grade_unit: str
        grade_value: float
    }

    class PageInfo {
        page: int
        bounding_box: Optional[BoundingBox]
    }

    class Reference {
        document: Document
        page_info: list[PageInfo]
    }

    class LocationInfo {
        location: Geometry
        crs: str
        country: Optional[str]
        state_or_province: Optional[str]
    }

    class MineralSite {
        source_id: str
        record_id: str
        name: Optional[str]
        mineral_inventory: list[MineralInventory]
        location_info: LocationInfo
        geology_info: Optional[GeologyInfo]
        deposit_type_candidate: list[DepositTypeCandidate]
    }

    class EvidenceLayer {
        name: str
        relevance_score: float
    }

    class Ore {
        ore_unit: str
        ore_value: float
    }

    class DepositType {
        name: str
        environment: str
        group: str
    }

    class Geometry {
        <<Enumeration>>
        Point: str = 'Point'
        Polygon: str = 'Polygon'
    }

    class MappableCriteria {
        criteria: str
        theoretical: Optional[str]
        potential_dataset: Optional[list[EvidenceLayer]]
        supporting_references: list[Reference]
    }

    class MineralSystem {
        deposit_type: list[DepositType]
        source: list[MappableCriteria]
        pathway: list[MappableCriteria]
        trap: Optional[list[MappableCriteria]]
        preservation: Optional[list[MappableCriteria]]
        energy: Optional[list[MappableCriteria]]
        outflow: Optional[list[MappableCriteria]]
    }

    class Commodity {
        name: str
    }

    class DepositTypeCandidate {
        observed_name: str
        normalized_uri: DepositType
        confidence: float
        source: str
    }

    class Document {
        id: str
        title: str
        is_open: bool
        pages: int
        size: int
        provenance: list[DocumentProvenance] = list
        metadata: Optional[DocumentMetaData] = None
        system: str
        system_version: str
    }

    class ResourceReserveCategory {
        <<Enumeration>>
        INFERRED: str = 'Inferred Mineral Resource'
        INDICATED: str = 'Indicated Mineral Resource'
        MEASURED: str = 'Measured Mineral Resource'
        PROBABLE: str = 'Probable Mineral Reserve'
        PROVEN: str = 'Proven Mineral Reserve'
    }

    class GeologyInfo {
        age: Optional[str]
        unit_name: Optional[str]
        description: Optional[str]
        lithology: Optional[list[str]]
        process: Optional[list[str]]
        environment: Optional[list[str]]
        comments: Optional[str]
    }

    class BoundingBox {
        x_min: float
        x_max: float
        y_min: float
        y_max: float
    }

    Document ..> DocumentMetaData
    Document ..> DocumentProvenance
    DepositTypeCandidate ..> DepositType
    PageInfo ..> BoundingBox
    Reference ..> Document
    Reference ..> PageInfo
    MappableCriteria ..> Reference
    MappableCriteria ..> EvidenceLayer
    MineralSystem ..> MappableCriteria
    MineralSystem ..> DepositType
    MineralInventory ..> Commodity
    MineralInventory ..> datetime
    MineralInventory ..> Reference
    MineralInventory ..> ResourceReserveCategory
    MineralInventory ..> Ore
    MineralInventory ..> Grade
    LocationInfo ..> Geometry
    MineralSite ..> DepositTypeCandidate
    MineralSite ..> LocationInfo
    MineralSite ..> MineralInventory
    MineralSite ..> GeologyInfo


```

</details>

### Map Results

<details open>
    <summary>map results</summary>

```mermaid
classDiagram

    class MapResults {
        cog_id: str
        georef_results: Optional[list[GeoreferenceResults]]
        extraction_results: Optional[list[FeatureResults]]
    }

    class FeatureResults {
        cog_id: str
        line_feature_results: Optional[list[LineLegendAndFeaturesResult]]
        point_feature_results: Optional[list[PointLegendAndFeaturesResult]]
        polygon_feature_results: Optional[list[PolygonLegendAndFeauturesResult]]
        cog_area_extractions: Optional[list[Area_Extraction]]
        cog_metadata_extractions: Optional[list[CogMetaData]]
        system: str
        system_version: str
    }

    class GeoreferenceResults {
        cog_id: str
        georeference_results: Optional[list[GeoreferenceResult]]
        gcps: Optional[list[GroundControlPoint]]
        system: str
        system_version: str
    }

    FeatureResults ..> PolygonLegendAndFeauturesResult
    FeatureResults ..> CogMetaData
    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> Area_Extraction
    GeoreferenceResults ..> GroundControlPoint
    GeoreferenceResults ..> GeoreferenceResult
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
        provenance: Optional[list[MapProvenance]] = None
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
<!--#+END_SCHEMA-->
