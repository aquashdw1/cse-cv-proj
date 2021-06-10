import os
import cv2
import numpy as np
from utils.image_reader import ImageReader


class EdgeExtractor(ImageReader):
    def __init__(
            self,
            image_filename: str = None,
            image_file: bytes = None,
            image_array=None,
            name: str = "no_name",
            thresh_min: int = 100,
            thresh_max: int = 200,
            kernel_gaussian: int = 5
    ):
        super().__init__(
            image_filename=image_filename,
            image_file=image_file,
            image_array=image_array,
            name=name
        )
        self.thresh_min = thresh_min
        self.thresh_max = thresh_max
        self.process_frame = self.image_array
        self.kernel_gaussian = kernel_gaussian

    def resize(self, width: int = 384, height: int = 216):
        self.process_frame = cv2.resize(self.process_frame, (width, height))

    def gaussian_process(self, kernel_size: int = None):
        if not kernel_size:
            kernel_size = self.kernel_gaussian
        self.process_frame = cv2.cvtColor(self.process_frame, cv2.COLOR_BGR2GRAY)
        _, self.process_frame = cv2.threshold(self.process_frame, 200, 255, cv2.THRESH_BINARY)
        self.process_frame = cv2.GaussianBlur(self.process_frame, (kernel_size, kernel_size), 0)

    def canny_process(self, thresh_min: int = None, thresh_max: int = None):
        if not thresh_min:
            thresh_min = self.thresh_min
        if not thresh_max:
            thresh_max = self.thresh_max
        self.process_frame = cv2.Canny(self.process_frame, thresh_min, thresh_max)

    def hough_process(self):
        rho = 1  # distance resolution in pixels of the Hough grid
        theta = np.pi / 180  # angular resolution in radians of the Hough grid
        threshold = 15  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 50  # minimum number of pixels making up a line
        max_line_gap = 15  # maximum gap in pixels between connectable line segments
        line_image = np.copy(self.process_frame) * 0  # creating a blank to draw lines on

        lines = cv2.HoughLinesP(self.process_frame, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), 2)
        self.process_frame = line_image

    def preview(self):
        cv2.imshow(self.name, self.process_frame)
        cv2.waitKey(0)
        cv2.destroyWindow(self.name)

    def save(self):
        self.image_array = self.process_frame

    def reset(self):
        self.process_frame = self.image_array

    def imwrite_preview(self):
        cv2.imwrite("./{}_{}_{}_{}.jpg".format(self.name, self.thresh_min, self.thresh_max, self.kernel_gaussian), self.process_frame)


TARGET_DIR = "results/jamsil_front"


if __name__ == '__main__':
    # for i in range(len(os.listdir(TARGET_DIR))):
    #     image_test = EdgeExtractor(
    #         image_filename="./{}/{}.jpg".format(TARGET_DIR, i),
    #         name="{}".format(i)
    #     )
    #
    #     # image_test.resize(192, 108)
    #     image_test.gaussian_process(kernel_size=3)
    #     image_test.canny_process()
    #     # image_test.hough_process()
    #     image_test.save()
    #     image_test.imshow()

    image_test = EdgeExtractor(
        image_filename="./{}/{}.jpg".format(TARGET_DIR, 0),
        name="jamsil_front",
        thresh_min=100,
        thresh_max=200,
        kernel_gaussian=3,
    )

    # image_test.gaussian_process()
    image_test.canny_process()
    image_test.preview()
    image_test.imwrite_preview()
    image_test.reset()

    # image_test.kernel_gaussian = 5
    # image_test.gaussian_process()
    # image_test.canny_process()
    # image_test.preview()
    # image_test.imwrite_preview()
    # image_test.reset()
    #
    # image_test.kernel_gaussian = 7
    # image_test.gaussian_process()
    # image_test.canny_process()
    # image_test.preview()
    # image_test.imwrite_preview()
    # image_test.reset()
    #
    # image_test.thresh_max = 250
    # image_test.thresh_min = 50
    #
    # image_test.kernel_gaussian = 3
    # image_test.gaussian_process()
    # image_test.canny_process()
    # image_test.preview()
    # image_test.imwrite_preview()
    # image_test.reset()
    #
    # image_test.kernel_gaussian = 5
    # image_test.gaussian_process()
    # image_test.canny_process()
    # image_test.preview()
    # image_test.imwrite_preview()
    # image_test.reset()
    #
    # image_test.kernel_gaussian = 7
    # image_test.gaussian_process()
    # image_test.canny_process()
    # image_test.preview()
    # image_test.imwrite_preview()
    # image_test.reset()
