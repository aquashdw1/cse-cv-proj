import numpy as np
import numpy.linalg as nplin


def get_homography(src_points, dst_points):
    x1 = src_points[0][0]
    y1 = src_points[0][1]
    x2 = src_points[1][0]
    y2 = src_points[1][1]
    x3 = src_points[2][0]
    y3 = src_points[2][1]
    x4 = src_points[3][0]
    y4 = src_points[3][1]
    xp1 = dst_points[0][0]
    yp1 = dst_points[0][1]
    xp2 = dst_points[1][0]
    yp2 = dst_points[1][1]
    xp3 = dst_points[2][0]
    yp3 = dst_points[2][1]
    xp4 = dst_points[3][0]
    yp4 = dst_points[3][1]

    matrix_h = np.array([
         [-x1, -y1, -1, 0, 0, 0, x1 * xp1, y1 * xp1, xp1],
         [0, 0, 0, -x1, -y1, -1, x1 * yp1, y1 * yp1, yp1],
         [-x2, -y2, -1, 0, 0, 0, x2 * xp2, y2 * xp2, xp2],
         [0, 0, 0, -x2, -y2, -1, x2 * yp2, y2 * yp2, yp2],
         [-x3, -y3, -1, 0, 0, 0, x3 * xp3, y3 * xp3, xp3],
         [0, 0, 0, -x3, -y3, -1, x3 * yp3, y3 * yp3, yp3],
         [-x4, -y4, -1, 0, 0, 0, x4 * xp4, y4 * xp4, xp4],
         [0, 0, 0, -x4, -y4, -1, x4 * yp4, y4 * yp4, yp4]
    ], np.int32)
    matrix_u, matrix_s, matrix_vt = nplin.svd(matrix_h)

    vt_column = matrix_vt[8] / matrix_vt[8][0]

    return np.array([
        [vt_column[0], vt_column[1], vt_column[2]],
        [vt_column[3], vt_column[4], vt_column[5]],
        [vt_column[6], vt_column[7], vt_column[8]]
    ])


def warp_image(src, dst, transform):
    matrix_h_inv = nplin.inv(transform)
    for height in range(dst.shape[0]):
        for width in range(dst.shape[1]):
            tmp_coor = np.matmul(matrix_h_inv, np.array([width, height, 1]))
            tmp_coor /= tmp_coor[2]
            trans_coor = [tmp_coor[0], tmp_coor[1]]
            tx, ty = round(trans_coor[0]), round(trans_coor[1])
            a, b = trans_coor[0] - tx, trans_coor[1] - ty

            if 0 <= tx < src.shape[1] - 1 and 0 <= ty < src.shape[0] - 1:
                for i in range(3):
                    dst[height, width, i] = round(
                        ((1-a) * (1-b)) * src[ty, tx, i] +
                        (a * (1-b)) * src[ty, tx + 1, i] +
                        ((1-a) * b) * src[ty + 1, tx, i] +
                        (a * b) * src[ty + 1, tx + 1, i])

    return dst
