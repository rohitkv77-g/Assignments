import math


def trans(X, Y):
    #initial matrix final edit
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def new_pointt(X, Y):
    result = [0, 0, 0]
    for i in range(len(X)):
        for j in range(len(Y)):
            result[i] += X[i][j] * Y[j]
    return result


def change():
    coord = list(map(int, input("Enter the point in x y z coordinates: ").strip().split(),))[:3]
    theta = list(map(int, input("The angles of rotation about the x y z coordinates: ").strip().split(),))[:3]

    rotation_X = [[1, 0, 0],[0, math.cos(math.radians(theta[0])), -math.sin(math.radians(theta[0]))], [0, math.sin(math.radians(theta[0])), math.cos(math.radians(theta[0]))],]

    rotation_Y = [[math.cos(math.radians(theta[1])), 0, math.sin(math.radians(theta[1]))], [0, 1, 0], [-math.sin(math.radians(theta[1])), 0, math.cos(math.radians(theta[1]))],]

    rotation_Z = [[math.cos(math.radians(theta[2])), -math.sin(math.radians(theta[2])), 0], [math.sin(math.radians(theta[2])), math.cos(math.radians(theta[2])), 0], [0, 0, 1],]

    transformation = trans(rotation_X, rotation_Y)
    transformation = trans(transformation, rotation_Z)
    final_result = new_pointt(transformation, coord)

    print(f"Coordinates of Point {coord[0], coord[1], coord[2]} with respect to original frame is {round(final_result[0], 3), round(final_result[1], 3), round(final_result[2], 3)}")
    input("Press Enter to exit...")


change()
