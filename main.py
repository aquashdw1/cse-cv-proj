from utils.image_reader import ImageReader


if __name__ == '__main__':
    print("hello world")
    test_image = ImageReader(
        image_filename="project1_hog/1st.jpg",
        name="test"
    )

    # test_image.imshow()
    test_image.set_points(4)
