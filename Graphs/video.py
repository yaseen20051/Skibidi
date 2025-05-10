import cv2
import numpy as np


def stitch_images_side_by_side(image1_path, image2_path):
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    im3 = cv2.imread("img2.png")

    if img1.shape[0] != img2.shape[0]:

        height1 = img1.shape[0]
        width2 = int(img2.shape[1] * (height1 / img2.shape[0]))  # maintain aspect ratio
        img2 = cv2.resize(img2, (width2, height1))

    stitched_image = np.hstack((img1,im3, img2))

    size = (int(stitched_image.shape[1]/3), int(stitched_image.shape[0]/3))
    stitched_image = cv2.resize(stitched_image, size)
    return stitched_image


def create_video(ii):

    image1_path = 'Graphs/graph1.png'
    image2_path = 'Graphs/graph-1.png'
    frame = stitch_images_side_by_side(image1_path, image2_path)

    vid = cv2.VideoWriter("final.avi", cv2.VideoWriter_fourcc(*'MJPG'), 1, (frame.shape[1], frame.shape[0]))
    vid.write(frame)
    vid.write(frame)
    for i in range(2, ii+1):
        print(i)
        image1_path = f'Graphs/graph{i}.png'
        image2_path = f'Graphs/graph-{i}.png'
        frame = stitch_images_side_by_side(image1_path, image2_path)
        vid.write(frame)
    vid.release()

