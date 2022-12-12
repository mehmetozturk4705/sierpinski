import numpy as np
import cv2


def sapinski_animation():
    image = np.zeros((500, 500, 3), dtype=np.uint8)
    image += 255

    # Initial points
    initial_points = [
        (80, 250), # top
        (392, 250 - int(250/np.sqrt(2))), # left down
        (392, 250 + int(250/np.sqrt(2))), # right down
    ]

    for p in initial_points:
        image[p[0]][p[1]] = (0, 0, 0)

    pt1, pt2, pt3 = initial_points
    x, y = np.random.random(), np.random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    last_point = (
        int(s * pt1[0] + t * pt2[0] + u * pt3[0]),
        int(s * pt1[1] + t * pt2[1] + u * pt3[1]),
    ) # a random point within triangle
    image[last_point[0]][last_point[1]] = (0, 0, 0)

    num_of_points = 4
    while True:
        # Select one of initial points
        selected_element = initial_points[np.random.randint(0, 3)]

        last_point = int((selected_element[0] + last_point[0])/2), int((selected_element[1] + last_point[1])/2)
        # Add point
        image[last_point[0]][last_point[1]] = (0, 0, 0)
        num_of_points += 1

        # Print the number of points
        image_copy = np.copy(image)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        font_scale = 0.5
        color = (0, 0, 0)
        thickness = 1
        image_copy = cv2.putText(image_copy, f'{num_of_points} points', org, font,
                            font_scale, color, thickness, cv2.LINE_AA)

        # show
        cv2.imshow('Image', image_copy)

        if cv2.waitKey(1) == ord('e'):
            return


if __name__=='__main__':
    sapinski_animation()