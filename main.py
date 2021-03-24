import numpy as np

from utils.image_reader import ImageReader
from utils.point_extension import PointExtractor

from project1_hog.gradient_histogram import get_grad_hist, variance_check


if __name__ == '__main__':
    print("hello world")
    image_first = PointExtractor(
        image_filename="project1_hog/1st.jpg",
        name="test1"
    )

    image_first.set_points(4)
    image_first_hists = []
    for i in range(len(image_first.points)):
        image_first_hists.append(get_grad_hist(image_first.image_array, image_first.points[i]))

    image_second = PointExtractor(
        image_filename="project1_hog/2nd.jpg",
        name="test2"
    )

    image_second.set_points(4)
    image_second_hists = []
    for i in range(len(image_second.points)):
        image_second_hists.append(get_grad_hist(image_second.image_array, image_second.points[i]))

    pairs = []
    for i in range(4):
        variances = []
        for j in range(4):
            variances.append(variance_check(image_first_hists[i], image_second_hists[j]))
        pairs.append((i, variances.index(min(variances))))

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
