from enum import Enum
from typing import Type
from pydantic import BaseModel


class GeomType(str, Enum):
    Point = "Point"
    LineString = "LineString"
    Polygon = "Polygon"


class GeoJsonType(str, Enum):
    Feature = "Feature"
    FeatureCollection = "FeatureCollection"


def add_class_name_property(cls: Type[BaseModel]) -> Type[BaseModel]:
    class_name_property = property(lambda self: self.__class__.__name__)
    setattr(cls, "class_name", class_name_property)

    def to_dict_with_class_name(self):
        return {"class_name": self.__class__.__name__, **self.dict()}

    setattr(cls, "to_dict_with_class_name", to_dict_with_class_name)

    return cls
