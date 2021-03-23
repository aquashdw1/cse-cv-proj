import numpy as np
import cv2


class ImageReader:
    def __init__(
            self,
            image_filename: str = None,
            image_file: bytes = None,
            image_array: np.array = None,
            name: str = "no_name"
    ):
        if image_filename:
            self.image_array = cv2.imread(image_filename)
        elif image_file:
            self.image_array = cv2.imdecode(image_file)
        elif image_array:
            self.image_array = image_array
        else:
            raise ValueError("no valid arguments given")
        self.name = name

    def imshow(self):
        cv2.imshow(self.name, self.image_array)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def set_points(self, point_count: int):
        points = []

        def point_click(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(self.image_array, (x, y), 50, (255, 0, 0), 3)
                points.append((x, y))
                cv2.imshow(self.name, self.image_array)

        cv2.namedWindow(self.name)
        cv2.setMouseCallback(self.name, point_click)

        cv2.imshow(self.name, self.image_array)
        while len(points) < point_count:
            key = cv2.waitKey(20) & 0xFF
            if key == ord("q"):
                cv2.destroyAllWindows()
                exit(-1)
        print(points)
