import numpy as np

from utils.point_extension import PointExtractor

from project1_hog.gradient_histogram import get_grad_hist


if __name__ == '__main__':
    print("hello world")
    image_first = PointExtractor(
        image_filename="project1_hog/1st.jpg",
        name="test1"
    )

    # image_first.set_points(4)
    # image_first.imshow()

    image_second = PointExtractor(
        image_filename="project1_hog/2nd.jpg",
        name="test2"
    )

    image_second.set_points(1)
    get_grad_hist(image_second.image_array, image_second.points[0])

    # image_third = ImageReader(
    #     image_array=np.concatenate(
    #         (image_first.image_array, image_second.image_array),
    #         axis=1),
    #     name="concatenated"
    # )
    # image_third.imshow()
    #
    # merge_fs = ImageMerge(
    #     image_arrays=[image_first.image_array, image_second.image_array]
    # )
    # merge_fs.preprocess()
