from math import sin, cos, radians
import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

std_angle = 40

def line(p0, length, angle, text=None):
    angle = radians(angle)
    x = p0[0] + length * cos(angle)
    y = p0[1] + length * sin(angle)
    ax.plot([p0[0], x], [p0[1], y], color="black")
    if text:
        ax.text(x + 0.4*length * cos(angle),
                y + 0.4*length * sin(angle),
                text,
                horizontalalignment="center",
                verticalalignment="center", backgroundcolor="white",
                fontsize="x-large")


def alkane(n, d=[], t=[], *g):
    ax.set_xlim([-3, 6])
    ax.set_ylim([-4.5, 4.5])
    op_main_angle = std_angle
    op_main_point = (0, 0)
    for i in range(n):
        if i+1 not in t and i not in t:
            line(op_main_point, 1, op_main_angle)
        else:
            op_main_angle *= -1
            line(op_main_point, 1, op_main_angle)
        if i+1 in d:
            op_double_point = (op_main_point[0], op_main_point[1] + (-1)**i * 0.2)
            line(op_double_point, 0.9, op_main_angle)
        elif i+1 in t:
            op_upper_t_point = (op_main_point[0] - (-1)**i * cos(op_main_angle) * 0.1,
                                op_main_point[1] + 0.1)
            op_down_t_point = (op_main_point[0] + (-1)**i * cos(op_main_angle) * 0.1,
                               op_main_point[1] - 0.1)
            line(op_upper_t_point, 0.9, op_main_angle)
            line(op_down_t_point, 0.9, op_main_angle)
        op_main_point = (op_main_point[0] + cos(radians(op_main_angle)),
                         op_main_point[1] + sin(radians(op_main_angle)))
        op_main_angle *= -1
    for ele in g:
        if ele[0] % 2:
            for i in range(ele[1]):
                if i == 0:
                    p = (ele[0] * cos(radians(std_angle)), sin(radians(std_angle)))
                    angle = 90
                elif i == 1:
                    p = (p[0], p[1]+1)
                    angle = 180 - std_angle
                else:
                    x = p[0] - cos(radians(std_angle))
                    p = (x, p[1] + (-1)**i * sin(radians(std_angle)))
                    angle = 180 - (-1)**i * std_angle
                text = f"$CH_3$" if i == (ele[1]-1) else None
                line(p, 1, angle, text)
        else:
            for i in range(ele[1]):
                if i == 0:
                    p = (ele[0] * cos(radians(std_angle)), 0)
                    angle = -90
                elif i == 1:
                    p = (p[0], p[1]-1)
                    angle = 180 + std_angle
                else:
                    x = p[0] - cos(radians(std_angle))
                    p = (x, p[1] - (-1)**i * sin(radians(std_angle)))
                    angle = 180 - (-1)**i * std_angle
                text = f"$CH_3$" if i == (ele[1] - 1) else None
                line(p, 1, angle, text)


alkane(6, [2], [5], (2, 4), (3, 2))

plt.axis("off")


plt.savefig("export.svg")