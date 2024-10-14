from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

class BestBounds(BaseModel):
    type: str
    coordinates: List[List[List[Union[float, int]]]]

class CMA(BaseModel):
    cma_id: str
    crs: str
    mineral: str
    download_url: str
    extent: Optional[BestBounds]
    resolution: List[int]
    description: Optional[str]=""
    creation_date: Optional[datetime]

class CogMeta(BaseModel):
    cog_id: str
    scale: Optional[int] = None
    has_part_names: List[str] = []
    cog_url: str
    best_bounds: Optional[BestBounds] = None
    publisher: str = ""
    cog_size: Optional[int] = None
    authors: List[str] = []
    provider_name: str= ""
    display_links_str: str= ""
    no_map: bool = False
    provider_url: str = ""
    original_download_url: str = ""
    cog_name: str = ""
    thumbnail_url: str = ""
    state: str = ""
    alternate_name: str = ""
    publish_year: Optional[int] = None
    quadrangle: str = ""
    citation: str = ""
    keywords: List[str] = []
    ngmdb_prod: Optional[str] = ""
    ngmdb_item: Optional[int] = None
    cmas: List[CMA] = []
    georeferenced_count: int = 0
    validated_count: int = 0
