import numpy as np

from utils.image_reader import ImageReader
from utils.point_extension import PointExtractor

from project2_warp.image_warp import get_homography


def main(image_src="src.png", image_dst="dst.png"):
    image_src = PointExtractor(
        image_filename=image_src,
        name="src",
        indicator_radius=10
    )
    image_src.set_points(4)
    src_points = image_src.get_current_points()

    image_dst = PointExtractor(
        image_filename=image_dst,
        name="dst",
        indicator_radius=10
    )
    image_dst.set_points(4)
    dst_points = image_dst.get_current_points()

    print(src_points)
    print(dst_points)
    get_homography(src_points, dst_points)


if __name__ == '__main__':
    main()
