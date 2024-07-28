"""Kovh fractal"""

import numpy as np
import matplotlib.pyplot as plt

START_X = 0
START_Y = 0
START_ANGLE = 180
START_STEP = 100


def koch_branch_build(step, angle, points: list, level):
    """Calculate points of Koch fractal"""

    if level == 0:
        old_point = points[-1]
        radians = np.radians(angle)

        new_point = [
            float(old_point[0] + step * np.cos(radians)),
            float(old_point[1] + step * np.sin(radians)),
        ]

        points.append(new_point)
    else:
        for angle_rotate in [0, 60, -120, 60]:
            angle += angle_rotate
            points = koch_branch_build(step / 3, angle, points, level - 1)

    return points


def koch_build(x, y, angle, step, levels) -> list:
    """Calculate points of Koch snowflake"""
    result = [[x, y]]
    for angle_change in [0, -120, -240]:
        result = koch_branch_build(step, angle + angle_change, result, levels)
    return result


def koch_draw(points, level):
    """Draw Koch fractal"""
    title = f"Koch fractal of the level {level}"
    plt.figure(facecolor="black", num=title)
    ax = plt.axes()
    ax.set_facecolor("black")
    ax.set_aspect("equal", "box")
    plt.plot(*zip(*points), color="deepskyblue")
    plt.scatter(*zip(*points), color="deepskyblue", s=10)
    plt.show()


if __name__ == "__main__":
    print("\nEnter the number of levels of the Koch fractal >> ...")
    levels = int(input())
    koch_draw(koch_build(START_X, START_Y, START_ANGLE, START_STEP, levels), levels)
