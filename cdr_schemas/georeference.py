from typing import List, Union, Optional

from pydantic import BaseModel, Field, ConfigDict
from common import GeomType
from cdr_schemas.area_extraction import Area_Extraction


class Geom_Point(BaseModel):
    """
    Geometry Point:
    Point geometry in world coordinates (longitude, latitude).
    """

    latitude: Optional[Union[float, int]]
    longitude: Optional[Union[float, int]]
    type: GeomType = GeomType.Point


class Pixel_Point(BaseModel):
    """
    Pixel point.
    Point geometry in pixel coordinates (columns from left, row from bottom).
    """

    rows_from_top: Union[float, int]
    columns_from_left: Union[float, int]
    type: GeomType = GeomType.Point


class GroundControlPoint(BaseModel):
    """
    Ground Control Point
    """

    gcp_id: str = Field(
        ...,
        description="""
            Your internal generated gcp id that helps connect to a 
            raster projection if one is created.
        """,
    )
    map_geom: Geom_Point = Field(
        ...,
        description="""
            Point geometry, in world coordinates. [longitude, latitude].
        """,
    )
    px_geom: Pixel_Point = Field(
        ...,
        description="""
            Point geometry, in pixel coordinates. [columns from left, row from bottom].
        """,
    )
    confidence: Optional[float] = Field(
        ...,
        description="""
            Confidence associated with this extraction.
        """,
    )
    model: str = Field(
        ...,
        description="""
            The name of the model used.
        """,
    )
    model_version: str = Field(
        ...,
        description="""
            The version of the model.
        """,
    )
    crs: Optional[str] = Field(
        ...,
        description="""
            Coordinate reference system. i.e. "EPSG:4267"
        """,
    )

    model_config = ConfigDict(protected_namespaces=())


class ProjectionResult(BaseModel):
    """
    Projection Result
    """

    crs: str = Field(
        ...,
        description="""
            Coordinate reference system used for projection. i.e. "EPSG:32612"
        """,
    )
    gcp_ids: List[str] = Field(
        ...,
        description="""
            List of gcp ids used in transform. i.e. ["1","2"]
        """,
    )
    file_name: str = Field(
        ...,
        description="""
            Name of file uploaded for this projection.
        """,
    )


class GeoreferenceResult(BaseModel):
    """
    Georeference Result.
    """

    likely_CRSs: Optional[List[str]] = Field(
        ...,
        description="""
            List of potential Coordinate Reference System specifically 
            Projection Coordinate System for the map. ie ["EPSG:32612", "EPSG:32613"]
        """,
    )
    map_area: Optional[Area_Extraction] = Field(
        ...,
        description="""
            Polygon bordering the map area for this georeference result. There can 
            be many map areas on a cog so this would be the pixel polygon of one of those
            areas that has been found. 
            The optional projections attached to this GeoreferenceResult should be referring to this area.
        """,
    )
    projections: Optional[List[ProjectionResult]] = Field(
        ...,
        description="""
            For each projection raster produced return crs 
            and gcp ids used in the transform
        """,
    )


class GeoreferenceResults(BaseModel):
    """
    Georeference Results.
    """

    cog_id: str = Field(
        ...,
        description="""
            Cog id.
        """,
    )
    georeference_results: Optional[List[GeoreferenceResult]] = Field(
        ...,
        description="""
            A list of georeferencing results, which include projections, gcps, and crs info. 
        """,
    )
    gcps: Optional[List[GroundControlPoint]] = Field(
        ...,
        description="""
            List of all gcps extracted for the cog image.
        """,
    )
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
