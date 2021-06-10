import math

from project1_hog import main as hog_main
from project2_warp import main as warp_main

from utils.point_extension import PointExtractor
from utils.image_reader import ImageReader

TARGET_IMAGE = "utils/results/kershaw_dodgers_1/0.jpg"

if __name__ == '__main__':
    # hog_main.main(image_first="project1_hog/1st.jpg", image_second="project1_hog/2nd.jpg")
    # warp_main.main(image_src="project2_warp/src.png", image_dst="project2_warp/dst.png")
    point_extraction = PointExtractor(
        image_filename=TARGET_IMAGE,
        indicator_radius=10
    )
    point_extraction.set_points(3)
    batter_keypoints = point_extraction.get_current_points()
    batter_keypoint_heights = sorted(batter_keypoints, key=lambda x: x[1], reverse=True)
    print(batter_keypoint_heights)
    # for batter_keypoint in batter_keypoints:
    #     batter_keypoint_heights.append(batter_keypoint[0])
    # min_height = min(batter_keypoint_heights)
    # max_height = max(batter_keypoint_heights)
    # med_height = 0
    # for batter_height in batter_keypoint_heights:
    #     if batter_height != min_height and batter_height != max_height:
    #         med_height = batter_height
    print("in pixels,")
    print("strike low border: {}".format(batter_keypoint_heights[0][1]))
    strike_zone_top_height = (batter_keypoint_heights[2][1] + batter_keypoint_heights[1][1])/2
    print("strike high border: {}".format(strike_zone_top_height))
    print()

    point_extraction.revert()
    point_extraction.set_points(2)
    home_points = point_extraction.get_current_points()
    home_points = sorted(home_points, key=lambda x: x[1])
    print(home_points)
    dx = abs(home_points[0][0] - home_points[1][0])
    dy = abs(home_points[0][1] - home_points[1][1])
    dx_pow = dx * dx
    dy_pow = dy * dy
    pixel_distance = math.sqrt(dx_pow + dy_pow)
    actual_distance = 51.8

    print("pixels per cm: {}".format(pixel_distance / actual_distance))

    print("estimate y for ground height: {}".format(home_points[0][1]))
    knee_point_height = abs(batter_keypoint_heights[0][1] - home_points[0][1])
    print("batter knee point height in pixels: {}".format(abs(batter_keypoint_heights[0][1] - home_points[0][1])))
    print("high right point for strike zone: {}".format((strike_zone_top_height, home_points[0][0])))
    print("low left point for strike zone: {}".format((batter_keypoint_heights[0][1], home_points[1][0])))
    high_right = (int(home_points[0][0]), int(strike_zone_top_height))
    low_left = (home_points[1][0], batter_keypoint_heights[0][1])
    new_points = [high_right, low_left]

    point_extraction.revert()
    point_extraction.destroy_window()

    display_image = ImageReader(
        image_array=point_extraction.image_array,
        name="result"
    )
    display_image.draw_line((high_right[0], high_right[1]), (high_right[0], low_left[1]))
    display_image.draw_line((high_right[0], high_right[1]), (low_left[0], high_right[1]))
    display_image.draw_line((low_left[0], low_left[1]), (low_left[0], high_right[1]))
    display_image.draw_line((low_left[0], low_left[1]), (high_right[0], low_left[1]))
    display_image.imshow()
