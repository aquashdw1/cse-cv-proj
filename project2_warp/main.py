import numpy as np

from utils.image_reader import ImageReader
from utils.point_extension import PointExtractor


def main(image_src="src.png", image_dst="dst.png"):
    image_src = PointExtractor(
        image_filename=image_src,
        name="src",
        indicator_radius=10
    )
    image_src.set_points(4)

    image_dst = PointExtractor(
        image_filename=image_dst,
        name="dst",
        indicator_radius=10
    )
    image_dst.set_points(4)


if __name__ == '__main__':
    main()
