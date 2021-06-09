import os
import cv2


class VideoHandler:
    def __init__(
            self,
            filename: str = None,
            extract_frame_rate: int = 30,  # standard fps for videos
            check_delay: int = 1000,
            save_path: str = "./results"
    ):
        self.filename = filename
        self.extract_frame_rate = extract_frame_rate
        self.frames = []
        self.check_delay = check_delay
        self.save_path = save_path

    def extract_frame_arrays(self):
        capture = cv2.VideoCapture(self.filename)
        i = 0
        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break
            if i % self.extract_frame_rate == 0:
                self.frames.append(frame)
            i += 1
        print("extracted total {} frames".format(len(self.frames)))
        capture.release()

    def check_frames(self):

        for frame in self.frames:
            cv2.imshow("extracted frame", frame)
            key_input = cv2.waitKey(self.check_delay)
            if key_input == ord("q"):
                break
            if key_input == ord("n"):
                continue
        cv2.destroyWindow("extracted frame")

    def save_to(self, path: str = None):
        save_path = path
        if not save_path:
            save_path = self.save_path
        if not os.path.exists(save_path) or not os.path.isdir(save_path):
            print("target directory invalid")

        save_img_basename = os.path.splitext(
            os.path.basename(self.filename)
        )[0]
        try:
            os.mkdir(os.path.join(save_path, save_img_basename))
        except FileExistsError:
            print("warn: result subsequent directory already exists")
            pass

        for index, frame in enumerate(self.frames):
            cv2.imwrite(
                os.path.join(save_path, save_img_basename, "{}.jpg".format(index)),
                frame
            )


if __name__ == '__main__':
    video_handler = VideoHandler("/Users/aquashdw/Movies/baseball_videos/2021-05-25 09-57-15.mkv")
    video_handler.extract_frame_arrays()
    # video_handler.check_frames()
    video_handler.save_to()
