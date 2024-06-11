from cdr_schemas.ta3_input import StackMetaData
from cdr_schemas.ta3_model import CMAModel
import erdantic as erd

from PIL import Image


def test_visualization():

    diagram_name = "ta3_output.png"
    erd.draw(CMAModel, out=diagram_name)

    with Image.open(diagram_name) as im:
        im.show()


if __name__ == "__main__":
    test_visualization()