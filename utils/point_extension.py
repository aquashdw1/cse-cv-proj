import cv2
import numpy as np

from utils.image_reader import ImageReader


class PointExtractor(ImageReader):
    def __init__(
            self,
            image_filename: str = None,
            image_file: bytes = None,
            image_array=None,
            indicator_radius=50,
            name: str = "no_name"
    ):
        super().__init__(
            image_filename=image_filename,
            image_file=image_file,
            image_array=image_array,
            name=name
        )
        self.points = []
        self.indicator_radius=indicator_radius
        self.image_with_points = np.copy(self.image_array)

    def set_points(self, point_count: int):
        self.points = []

        def point_click(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(self.image_with_points, (x, y), self.indicator_radius, (255, 0, 0), int(self.indicator_radius / 5))
                cv2.circle(self.image_with_points, (x, y), int(self.indicator_radius / 10), (255, 255, 255), -1)
                self.points.append((x, y))
                cv2.imshow(self.name, self.image_with_points)

        cv2.namedWindow(self.name)
        cv2.setMouseCallback(self.name, point_click)

        cv2.imshow(self.name, self.image_with_points)
        while len(self.points) < point_count:
            key = cv2.waitKey(20) & 0xFF
            if key == ord("q"):
                cv2.destroyAllWindows()
                exit(-1)
        cv2.destroyWindow(self.name)

    def save(self):
        self.image_array = self.image_with_points

    def revert(self):
        self.points = []
        self.image_with_points = self.image_array

    def get_current_points(self):
        return self.points

    def destroy_window(self):
        cv2.destroyWindow(self.name)
