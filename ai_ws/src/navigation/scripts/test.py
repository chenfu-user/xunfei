import math


def get_delta_yaw(now_point, specified_point):
    delta_x = specified_point[0] - now_point[0]
    delta_y = specified_point[1] - now_point[1]
    goal_yaw = abs(math.atan(delta_y / delta_x))
    tf_yaw = 0
    if delta_x > 0 and delta_y >0:
        tf_yaw = -(math.radians(90)-goal_yaw)
    elif delta_x < 0 and delta_y >0:
        tf_yaw = (math.radians(90)-goal_yaw)
    elif delta_x < 0 and delta_y < 0:
        tf_yaw = math.radians(90)+goal_yaw
    elif delta_x > 0 and delta_y >0:
        tf_yaw = - math.radians(90)-goal_yaw
    return tf_yaw

x0 = 4.79
y0 = -1.22
x1 = 4.37
y1 = -1.36
if __name__ == '__main__':
    try:
        print(math.degrees(get_delta_yaw((x0, y0), (x1, y1))))
    except KeyboardInterrupt:
        exit(0)
