import numpy as np

from utils.image_reader import ImageReader
from utils.point_extension import PointExtractor

from project1_hog.gradient_histogram import get_grad_hist, variance_check


if __name__ == '__main__':
    image_first = PointExtractor(
        image_filename="project1_hog/1st.jpg",
        name="test1"
    )

    image_first.set_points(4)

    image_second = PointExtractor(
        image_filename="project1_hog/2nd.jpg",
        name="test2"
    )

    image_second.set_points(4)

    image_first_hists = []
    for i in range(len(image_first.points)):
        image_first_hists.append(get_grad_hist(image_first.image_array, image_first.points[i]))

    image_second_hists = []
    for i in range(len(image_second.points)):
        image_second_hists.append(get_grad_hist(image_second.image_array, image_second.points[i]))

    pairs = []
    for i in range(4):
        variances = []
        for j in range(4):
            variances.append(variance_check(image_first_hists[i], image_second_hists[j]))
        pairs.append((i, variances.index(min(variances))))

    image_first.save()
    image_second.save()
    result_image = ImageReader(
        image_array=np.concatenate(
            (image_first.image_array, image_second.image_array),
            axis=1),
        name="concatenated"
    )

    offset = image_first.image_array.shape[1]

    for pair in pairs:
        offset_point = image_second.points[pair[1]]
        print(offset_point)
        offset_point = offset_point[0] + offset, offset_point[1]
        result_image.draw_line(image_first.points[pair[0]], offset_point)
    result_image.imshow()
