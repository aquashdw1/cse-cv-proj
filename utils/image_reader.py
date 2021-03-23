import cv2
import numpy as np


class ImageReader:
    def __init__(
            self,
            image_filename: str = None,
            image_file: bytes = None,
            image_array=None,
            name: str = "no_name"
    ):
        if image_filename:
            self.image_array = cv2.imread(image_filename)
        elif image_file:
            self.image_array = cv2.imdecode(image_file)
        elif image_array.any():
            self.image_array = image_array
        else:
            raise ValueError("no valid arguments given")
        self.name = name

    def imshow(self):
        cv2.imshow(self.name, self.image_array)
        cv2.waitKey(0)
        cv2.destroyWindow(self.name)

    def imshow_focus_point(self, x, y):
        temp_image = np.copy(self.image_array)
        cv2.circle(temp_image, (x, y), 50, (255, 0, 0), 10)
        cv2.circle(temp_image, (x, y), 5, (255, 255, 255), -1)
        cv2.imshow("{}_focus".format(self.name), temp_image)
        cv2.waitKey(0)
        cv2.destroyWindow(self.name)
