


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

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType


```

</details>

### Georeference

<details open>
    <summary>georeference</summary>

```mermaid
classDiagram

    class ProjectionResult {
        crs: str
        gcp_ids: list[str]
        file_name: str
    }

    class Pixel_Point {
        rows_from_top: Union[float, int]
        columns_from_left: Union[float, int]
        type: GeomType = GeomType.Point
    }

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class Geom_Point {
        latitude: Union[float, int, NoneType]
        longitude: Union[float, int, NoneType]
        type: GeomType = GeomType.Point
    }

    class GroundControlPoint {
        gcp_id: str
        map_geom: Geom_Point
        px_geom: Pixel_Point
        confidence: Optional[float]
        model: str
        model_version: str
        crs: Optional[str]
    }

    class GeoreferenceResult {
        likely_CRSs: Optional[list[str]]
        map_area: Optional[Area_Extraction]
        projections: Optional[list[ProjectionResult]]
    }

    class GeoreferenceResults {
        cog_id: str
        georeference_results: Optional[list[GeoreferenceResult]]
        gcps: Optional[list[GroundControlPoint]]
        system: str
        system_version: str
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

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType
    Geom_Point ..> GeomType
    Pixel_Point ..> GeomType
    GroundControlPoint ..> Geom_Point
    GroundControlPoint ..> Pixel_Point
    GeoreferenceResult ..> Area_Extraction
    GeoreferenceResult ..> ProjectionResult
    GeoreferenceResults ..> GroundControlPoint
    GeoreferenceResults ..> GeoreferenceResult


```

</details>

### Metadata

<details open>
    <summary>metadata</summary>

```mermaid
classDiagram

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
        multiple_maps: Optional[bool]
        map_metadata: Optional[list[MapMetaData]]
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

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
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

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType
    LineLegendAndFeaturesResult ..> LineFeatureCollection
    PointLegendAndFeaturesResult ..> PointFeatureCollection
    PolygonLegendAndFeauturesResult ..> MapUnit
    PolygonLegendAndFeauturesResult ..> PolygonFeatureCollection
    CogMetaData ..> MapMetaData
    FeatureResults ..> CogMetaData
    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> PolygonLegendAndFeauturesResult
    FeatureResults ..> LineLegendAndFeaturesResult
    FeatureResults ..> Area_Extraction


```

</details>

### Point Feature

<details open>
    <summary>point feature</summary>

```mermaid
classDiagram

    class Point {
        coordinates: list[Union[float, int]]
        type: GeomType = GeomType.Point
    }

    class GeoJsonType {
        <<Enumeration>>
        Feature: str = 'Feature'
        FeatureCollection: str = 'FeatureCollection'
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

    class PointProperties {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
        bbox: Optional[list[Union[float, int]]]
        dip: Optional[int]
        dip_direction: Optional[int]
    }

    class PointFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: list[PointFeature]
    }

    Point ..> GeomType
    PointFeature ..> Point
    PointFeature ..> GeoJsonType
    PointFeature ..> PointProperties
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

    class LineFeatureCollection {
        type: GeoJsonType = GeoJsonType.FeatureCollection
        features: Optional[list[LineFeature]]
    }

    class Line {
        coordinates: list[list[Union[float, int]]]
        type: GeomType = GeomType.LineString
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

    class LineProperty {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
        dash_pattern: Optional[DashType] = None
        symbol: Optional[str]
    }

    class LineFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Line
        properties: LineProperty
    }

    Line ..> GeomType
    LineProperty ..> DashType
    LineFeature ..> GeoJsonType
    LineFeature ..> Line
    LineFeature ..> LineProperty
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

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
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

    class PolygonProperty {
        model: Optional[str]
        model_version: Optional[str]
        confidence: Optional[float]
    }

    class PolygonFeature {
        type: GeoJsonType = GeoJsonType.Feature
        id: str
        geometry: Polygon
        properties: PolygonProperty
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

    class Polygon {
        coordinates: list[list[list[Union[float, int]]]]
        type: GeomType = GeomType.Polygon
    }

    Polygon ..> GeomType
    PolygonFeature ..> GeoJsonType
    PolygonFeature ..> Polygon
    PolygonFeature ..> PolygonProperty
    PolygonFeatureCollection ..> GeoJsonType
    PolygonFeatureCollection ..> PolygonFeature
    PolygonLegendAndFeauturesResult ..> MapUnit
    PolygonLegendAndFeauturesResult ..> PolygonFeatureCollection


```

</details>

### Cog Metadata

<details open>
    <summary>cog metadata</summary>

```mermaid
classDiagram

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
        multiple_maps: Optional[bool]
        map_metadata: Optional[list[MapMetaData]]
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

    class MapShapeTypes {
        <<Enumeration>>
        rectangular: str = 'rectangular'
        non_rectangular: str = 'non_rectangular'
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

    class Document {
        id: str
        title: str
        is_open: bool
        pages: Optional[int] = None
        provenance: Optional[list[DocumentProvenance]] = None
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

    class DocumentProvenance {
        external_system_name: str
        external_system_id: str = None
        external_system_url: str = None
    }

    Document ..> DocumentProvenance
    DocumentExtraction ..> dict


```

</details>

### Mineral

<details open>
    <summary>mineral</summary>

```mermaid
classDiagram

    class ResourceReserveCategory {
        <<Enumeration>>
        INFERRED: str = 'Inferred Mineral Resource'
        INDICATED: str = 'Indicated Mineral Resource'
        MEASURED: str = 'Measured Mineral Resource'
        PROBABLE: str = 'Probable Mineral Reserve'
        PROVEN: str = 'Proven Mineral Reserve'
    }

    class Reference {
        document: Document
        page_info: list[PageInfo]
    }

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

    class MappableCriteria {
        criteria: str
        theoretical: Optional[str]
        potential_dataset: Optional[list[EvidenceLayer]]
        supporting_references: list[Reference]
    }

    class Ore {
        ore_unit: str
        ore_value: float
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

    class DepositType {
        name: str
        environment: str
        group: str
    }

    class Document {
        id: str
        title: str
        is_open: bool
        pages: Optional[int] = None
        provenance: Optional[list[DocumentProvenance]] = None
        system: str
        system_version: str
    }

    class DepositTypeCandidate {
        observed_name: str
        normalized_uri: DepositType
        confidence: float
        source: str
    }

    class PageInfo {
        page: int
        bounding_box: Optional[BoundingBox]
    }

    class Commodity {
        name: str
    }

    class BoundingBox {
        x_min: float
        x_max: float
        y_min: float
        y_max: float
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

    class EvidenceLayer {
        name: str
        relevance_score: float
    }

    class Grade {
        grade_unit: str
        grade_value: float
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

    class LocationInfo {
        location: Geometry
        crs: str
        country: Optional[str]
        state_or_province: Optional[str]
    }

    Document ..> DocumentProvenance
    DepositTypeCandidate ..> DepositType
    PageInfo ..> BoundingBox
    Reference ..> Document
    Reference ..> PageInfo
    MappableCriteria ..> Reference
    MappableCriteria ..> EvidenceLayer
    MineralSystem ..> MappableCriteria
    MineralSystem ..> DepositType
    MineralInventory ..> datetime
    MineralInventory ..> Grade
    MineralInventory ..> ResourceReserveCategory
    MineralInventory ..> Commodity
    MineralInventory ..> Reference
    MineralInventory ..> Ore
    LocationInfo ..> Geometry
    MineralSite ..> DepositTypeCandidate
    MineralSite ..> MineralInventory
    MineralSite ..> GeologyInfo
    MineralSite ..> LocationInfo


```

</details>

### Map Results

<details open>
    <summary>map results</summary>

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

    class GeoreferenceResults {
        cog_id: str
        georeference_results: Optional[list[GeoreferenceResult]]
        gcps: Optional[list[GroundControlPoint]]
        system: str
        system_version: str
    }

    class MapResults {
        cog_id: str
        georef_results: Optional[list[GeoreferenceResults]]
        extraction_results: Optional[list[FeatureResults]]
    }

    FeatureResults ..> CogMetaData
    FeatureResults ..> PointLegendAndFeaturesResult
    FeatureResults ..> PolygonLegendAndFeauturesResult
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

    class GeomType {
        <<Enumeration>>
        Point: str = 'Point'
        LineString: str = 'LineString'
        Polygon: str = 'Polygon'
    }

    class Map {
        id: str
        provenance: Optional[list[MapProvenance]] = None
        is_open: bool
        system: str
        system_version: str
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

    class MapProvenance {
        system_name: str
        id: str = None
        url: str = None
    }

    Area_Extraction ..> GeomType
    Area_Extraction ..> AreaType
    Map ..> MapProvenance


```

</details>
<!--#+END_SCHEMA-->
