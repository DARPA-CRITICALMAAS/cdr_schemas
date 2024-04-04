from enum import Enum


class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"


class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"


class AreaType(str, Enum):
    Map_Area = "Map_Area"
    Legend_Area = "Legend_Area"
    CrossSection = "CrossSection"
    OCR = "OCR"
    Polygon_Legend_Area = "Polygon_Legend_Area"
    Line_Point_Legend_Area = "Line_Point_Legend_Area"
    Line_Legend_Area = "Line_Legend_Area"
    Point_Legend_Area = "Point_Legend_Area"
    Correlation_Diagram = "Correlation_Diagram"
