from project1_hog import main as hog_main
from project2_warp import main as warp_main

if __name__ == '__main__':
    # hog_main.main(image_first="project1_hog/1st.jpg", image_second="project1_hog/2nd.jpg")
    warp_main.main(image_src="project2_warp/src.png", image_dst="project2_warp/dst.png")
