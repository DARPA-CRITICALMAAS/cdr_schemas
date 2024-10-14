from typing import List, Optional, Union
from pydantic import BaseModel
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