import turtle as te
import time
WriteStep = 15  # 贝塞尔函数的取样次数
Speed = 5
Width = 600  # 界面宽度
Height = 500  # 界面高度
Xh = 0  # 记录前一个贝塞尔函数的手柄
Yh = 0


def Bezier(p1, p2, t):  # 一阶贝塞尔函数
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4  # 坐标变换
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Moveto(x, y):  # 移动到svg坐标下（x，y）
    te.penup()
    te.goto(-Width / 2 + x, Height / 2 - y)


def line(x1, y1, x2, y2):  # 连接svg坐标下两点
    te.penup()
    te.goto(-Width / 2 + x1, Height / 2 - y1)
    te.pendown()
    te.goto(-Width / 2 + x2, Height / 2 - y2)
    te.penup()


def lineto(dx, dy):  # 连接当前点和相对坐标（dx，dy）的点
    te.pendown()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.penup()


def Lineto(x, y):  # 连接当前点和svg坐标下（x，y）
    te.pendown()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.penup()


def Horizontal(x):  # 做到svg坐标下横坐标为x的水平线
    te.pendown()
    te.setx(x - Width / 2)
    te.penup()


def horizontal(dx):  # 做到相对横坐标为dx的水平线
    te.seth(0)
    te.pendown()
    te.fd(dx)
    te.penup()


def vertical(dy):  # 做到相对纵坐标为dy的垂直线
    te.seth(-90)
    te.pendown()
    te.fd(dy)
    te.penup()
    te.seth(0)


def polyline(x1, y1, x2, y2, x3, y3):  # 做svg坐标下的折线
    te.penup()
    te.goto(-Width / 2 + x1, Height / 2 - y1)
    te.pendown()
    te.goto(-Width / 2 + x2, Height / 2 - y2)
    te.goto(-Width / 2 + x3, Height / 2 - y3)
    te.penup()


def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def Smooth(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到（x，y）
    global Xh
    global Yh
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh, x2, y2, x, y)
    Xh = x - x2
    Yh = y - y2


def smooth_r(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到相对坐标（x，y）
    global Xh
    global Yh
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    Xh = x - x2
    Yh = y - y2

te.tracer(10)
te.setup(Width, Height, 0, 0)
te.pensize(1)
te.speed(Speed)
te.penup()

# 图层_2
time.sleep(20)
te.color("black", "#F2F2F2")  # 外套
Moveto(61, 462)
te.begin_fill()
smooth_r(12, -41, 27, -58)
curveto_r(-6, -36, 6, -118, 9, -132)
curveto_r(-15, -27, -23, -51, -26, -74)
curveto_r(4, -66, 38, -105, 65, -149)
Horizontal(486)
curveto_r(12, 24, 40, 99, 33, 114)
curveto_r(39, 82, 55, 129, 39, 144)
smooth_r(-31, 23, -39, 28)
smooth_r(-12, 37, -12, 37)
lineto(50, 92)
Horizontal(445)
smooth_r(-29, -38, -31, -46)
smooth_r(78, -107, 72, -119)
Smooth(355, 178, 340, 176)
Smooth(272, 63, 264, 64)
smooth_r(-29, 67, -27, 73)
Curveto(99, 292, 174, 428, 173, 439)
smooth_r(-8, 23, -8, 23)
Lineto(61, 462)
te.end_fill()

Moveto(60.5, 461.5)  # 阴影
te.color("black", "#D3DFF0")
te.begin_fill()
curveto_r(0, 0, 17, -42, 27, -59)
curveto_r(-6, -33, 6, -128, 10, -133)
curveto_r(-15, -10, -27, -66, -27.285, -75)
te.pencolor("#D3DFF0")
curveto_r(12.285, 11, 82.963, 156, 82.963, 156)
te.pencolor("black")
smooth_r(12.322, 75, 19.322, 86)
curveto_r(-1, 11, -8, 25, -8, 25)
Horizontal(60.5)
te.end_fill()

Moveto(444.5, 464)
te.begin_fill()
curveto_r(0, 0, -29, -36, -31, -46)
smooth_r(53.59, -82.337, 53.59, -82.337)
te.pencolor("#D3DFF0")
smooth_r(86.41, -47.663, 96.072, -54.85)
Curveto(563.5, 297.5, 570.5, 299.5, 518.5, 334)
te.pencolor("black")
curveto_r(-2, 16, -12, 33, -12, 37)
smooth_r(50, 92, 50, 93)
Horizontal(444.5)
te.end_fill()

Moveto(195, 49)
te.begin_fill()
te.pencolor("#D3DFF0")
polyline(195, 49, 175.5, 106.5, 202.522, 49)
te.pencolor("black")
Horizontal(195)
te.pencolor("#D3DFF0")
te.end_fill()

Moveto(327.997, 49)
te.begin_fill()
te.pencolor("#D3DFF0")
curveto_r(0, 0, 11.503, 121.087, 13.503, 128.087)
curveto_r(11, 2, 54, 37, 54, 37)
lineto(-40, -165.087)
te.pencolor("black")
Horizontal(327.997)
te.pencolor("#D3DFF0")
te.end_fill()

te.pencolor("black")
line(94.5, 397.5, 107.5, 373.5)  # 皱纹
line(122.5, 317.5, 95.875, 274.699)
line(122.5, 341.5, 141.5, 402.5)
line(141.5, 409.5, 153.5, 431.5)
# line(328,47.712,344,175.977)
line(340.023, 49, 360.5, 144)
# line(353.5,47.5,395.5,208.5)
line(478.5, 95.5, 518.5, 161.5)
line(518.5, 332.5, 460.5, 359.5)
polyline(506.5, 369.5, 493.5, 402.5, 502.5, 443.5)
Moveto(530, 429)
curveto_r(4, 16, -5, 33, -5, 33)

# 图层_3
te.color("black", "#2b1d2a")  # 外套内侧
Moveto(225, 462)
te.begin_fill()
Horizontal(165)
smooth_r(9, -15, 8, -25)
curveto_r(-47, -126, 6, -212, 12, -225)
Curveto(185, 305, 202, 428, 225, 462)
Lineto(225, 462)
te.end_fill()

Moveto(390, 462)
te.begin_fill()
curveto_r(10, -23, 34, -180, 35, -222)  # !!!227
curveto_r(7, 4, 54, 45, 61, 61)  # 61
smooth_r(-73, 101, -72, 118)
curveto_r(5, 15, 31, 46, 31, 45)
Lineto(390, 462)
te.end_fill()
# 图层_4
te.color("black", "#2b1d29")  # 外套内侧
Moveto(225, 462)
te.begin_fill()
curveto_r(-28, -50, -40, -166, -40, -250)
curveto_r(6, 51, -6, 87, 45, 106)
smooth_r(64, 27, 89, 24)
smooth_r(49, -18, 56, -20)
smooth_r(50, -10, 51, -85)
curveto_r(0, 29, -25, 201, -36, 225)
Lineto(225, 462)
te.end_fill()
# 图层_5
te.color("black", "#3D3D3D")  # 衣服
Moveto(225, 462)
te.begin_fill()
curveto_r(-5, -5, -22, -53, -23, -70)
lineto(32, -13)
curveto_r(3, -25, 6, -28, 12, -36)
smooth_r(13, -12, 16, -12)
vertical(-2)
curveto_r(45, 20, 64, 14, 94, 1)
vertical(2)
curveto_r(8, -2, 15, 2, 17, 4)
smooth_r(0, 6, -2, 9)
curveto_r(10, 10, 10, 29, 11, 33)
smooth_r(23, 4, 25, 6)
smooth_r(-17, 83, -17, 78)
Lineto(225, 462)
te.end_fill()
# 图层_6
te.color("black", "#968281")  # 脖子
Moveto(262, 329)
te.begin_fill()
vertical(17)
curveto_r(1, 2, 44, 14, 45, 15)
smooth_r(3, 12, 3, 12)
horizontal(3)
vertical(-5)
curveto_r(1, -3, 4, -6, 5, -7)
lineto(36, -14)
curveto_r(1, -1, 3, -16, 2, -17)
Curveto(318, 348, 296, 344, 262, 329)
te.end_fill()
# 图层_8
te.color("black", "#E7F1FF")  # 白色褶皱
Moveto(225, 462)
te.begin_fill()
lineto(-3, -5)  # -3,-3,-3,-5
curveto_r(0, -2, 4, -4, 5, -6)
smooth_r(16, 3, 19, -8)
smooth_r(0, -7, 0, -11)
smooth_r(5, -8, 9, -5)
smooth_r(19, -8, 19, -11)
smooth_r(6, -7, 6, -7)
smooth_r(7, -2, 9, -4)
lineto(41, -2)
lineto(12, 9)
smooth_r(3, 15, 7, 18)
smooth_r(15, 4, 17, 4)
smooth_r(4, -4, 6, -4)
smooth_r(6, 4, 5, 9)
smooth_r(0, 9, 0, 9)
smooth_r(1, 7, 7, 6)
smooth_r(8, 0, 8, 0)
lineto(-2, 8)
Lineto(225, 462)
te.end_fill()

te.pensize(2)
Moveto(240, 450)
smooth_r(0, 9, 3, 12)
Moveto(372, 462)
curveto_r(-2, -4, -5, -29, -7, -28)
te.pensize(1)
# 图层_7
te.color("black", "#A2B8D6")  # 衣领
Moveto(262, 331)
te.begin_fill()
curveto_r(0, 8, -1, 13, 0, 15)
smooth_r(43, 14, 45, 15)
lineto(3, 12)
horizontal(3)
smooth_r(-1, -3, 0, -5)
lineto(5, -7)
lineto(36, -14)
curveto_r(1, -1, 2, -12, 2, -15)
smooth_r(25, -2, 15, 13)
curveto_r(-2, 4, -7, 29, -7, 32)
smooth_r(-35, 19, -41, 22)
smooth_r(-9, 14, -12, 14)
smooth_r(-7, -12, -14, -15)
curveto_r(-19, -2, -41, -25, -41, -25)
smooth_r(-10, -26, -10, -30)
Smooth(255, 332, 262, 331)
te.end_fill()

Moveto(262, 346)
lineto(-12, -6)
Moveto(369, 333)
curveto_r(2, 4, -6, 10, -15, 14)
# 图层_9
te.color("black", "#151515")  # 领结
Moveto(247, 358)
te.begin_fill()
curveto_r(-5, 3, -8, 20, -6, 23)
curveto_r(25, 21, 50, 17, 50, 17)
lineto(-23, 64)
horizontal(22)
smooth_r(1, -13, 2, -16)
lineto(13, -50)
curveto_r(2, 2, 7, 3, 10, 1)
smooth_r(18, 65, 18, 65)
horizontal(19)
lineto(-24, -65)
curveto_r(21, 5, 39, -10, 44, -13)
curveto_r(5, -20, 1, -21, 0, -24)
curveto_r(-18, -2, -49, 15, -52, 17)
smooth_r(-11, -3, -15, -1)
Smooth(252, 356, 247, 358)
te.end_fill()
# 图层_10
te.color("black", "#A2B8D6")  # 衣领（透过领结）
Moveto(297, 387)
te.begin_fill()
lineto(-11, 6)
curveto_r(-1, 0, -20, -7, -30, -19)
Curveto(259, 373, 297, 385, 297, 387)
te.end_fill()

Moveto(323, 384)
te.begin_fill()
lineto(8, 7)
lineto(30, -14)
curveto_r(1, -1, 5, -6, 4, -7)
Smooth(329, 379, 323, 384)
te.end_fill()
# 图层_11
te.color("black", "#F3EEEB")  # 脸
Moveto(185, 212)
te.begin_fill()
curveto_r(4, -9, 46, -77, 52, -75)
curveto_r(-2, -17, 19, -68, 27, -73)
curveto_r(16, 15, 71, 108, 76, 112)
smooth_r(76, 53, 86, 60)
curveto_r(0, 65, -27, 75, -31, 76)
curveto_r(-50, 28, -70, 30, -85, 30)
smooth_r(-77, -22, -86, -26)
Curveto(180, 302, 186, 228, 185, 212)
te.end_fill()
# 图层_12
te.color("black", "#2B1D29")  # 头发
Moveto(189, 202)
te.begin_fill()
curveto_r(-1, 22, 19, 51, 19, 51)
smooth_r(-10, -42, 7, -92)
Curveto(212, 168, 196, 189, 189, 202)
te.end_fill()

Moveto(221, 155)
te.begin_fill()
curveto_r(-2, 6, 5, 48, 5, 48)
smooth_r(18, -28, 20, -48)
curveto_r(-5, 24, 4, 43, 7, 50)
curveto_r(-10, -49, 3, -72, 13, -106)
curveto_r(-2, -7, -3, -32, -3, -35)
curveto_r(-17, 18, -27, 71, -27, 71)
Lineto(221, 155)
te.end_fill()

Moveto(264, 64)
te.begin_fill()
curveto_r(-4, 5, 14, 100, 14, 100)
smooth_r(-6, -79, -5, -85)
curveto_r(0, 98, 49, 139, 49, 139)
smooth_r(8, -50, 3, -65)
Smooth(272, 64, 264, 64)
te.end_fill()

Moveto(342, 176)
te.begin_fill()
curveto_r(-1, 27, -10, 57, -10, 57)
smooth_r(20, -33, 17, -54)
Lineto(342, 176)
te.end_fill()

te.penup()
te.begin_fill()
polyline(349, 180, 353, 203, 361, 203)
polyline(361, 203, 362, 188, 349, 180)
te.end_fill()
# 图层_13
te.pensize(2)
Moveto(210, 180)  # 眉毛
curveto_r(5, -4, 63, 9, 63, 14)
Moveto(338, 193)
curveto_r(0, -3, 18, -6, 18, -6)
te.pensize(1)
# 图层_14
te.color("black", "#D1D1D1")  # 眼睛1
te.pensize(2)
Moveto(206, 212)
te.begin_fill()
lineto(15, -7)
curveto_r(4, -1, 26, -2, 30, 0)
smooth_r(10, 3, 12, 7)
te.pencolor("#D1D1D1")
te.pensize(1)
smooth_r(2, 27, -1, 30)
smooth_r(-39, 5, -44, 1)
Smooth(206, 212, 206, 212)
te.end_fill()

Moveto(384, 204)
te.begin_fill()
te.pencolor("black")
te.pensize(2)
curveto_r(-3, -1, -18, -1, -28, 1)
smooth_r(-9, 6, -10, 9)
te.pencolor("#D1D1D1")
te.pensize(1)
smooth_r(3, 18, 6, 23)
smooth_r(38, 6, 40, 4)
smooth_r(10, -9, 13, -22)
te.pencolor("black")
te.pensize(2)
Lineto(384, 204)
te.end_fill()
# 图层_15
te.color("#0C1631", "#0C1631")  # 眼睛2
te.pensize(1)
Moveto(216, 206)
te.begin_fill()
curveto_r(-1, 5, 0, 26, 7, 35)
smooth_r(30, 2, 33, 0)
smooth_r(5, -31, 2, -34)
Smooth(219, 203, 216, 206)
te.end_fill()

Moveto(354, 207)
te.begin_fill()
curveto_r(-2, 1, 2, 29, 4, 31)
smooth_r(30, 3, 33, 1)
smooth_r(6, -24, 4, -27)
lineto(-11, -8)
Curveto(382, 204, 357, 206, 354, 207)
te.end_fill()

# 图层_17
te.color("#F5F5F5", "#F5F5F5")  # 眼睛3
Moveto(253, 211)
te.begin_fill()
curveto_r(-3, 0, -8, 8, 1, 10)
Smooth(258, 210, 253, 211)
te.end_fill()

Moveto(392, 209)
te.begin_fill()
lineto(4, 3)
vertical(4)
lineto(-4, 2)
Curveto(386, 214, 392, 209, 392, 209)
te.end_fill()
# 图层_18
te.color("#352F53", "#352F53")  # 眼睛4
Moveto(219, 229)
te.begin_fill()
smooth_r(2, -5, 6, -4)
smooth_r(18, 13, 27, 1)
curveto_r(3, 0, 5, 3, 5, 3)
vertical(13)
Horizontal(224)
Lineto(219, 229)
te.end_fill()

Moveto(357, 227)
te.begin_fill()
smooth_r(4, -6, 10, -2)
smooth_r(10, 13, 19, 1)
curveto_r(6, 0, 8, 6, 8, 6)
lineto(-2, 9)
curveto_r(-12, 3, -29, 0, -32, -2)
Smooth(357, 227, 357, 227)
te.end_fill()

# 图层_19
te.color("#9A90CB", "#9A90CB")  # 眼睛5
Moveto(227, 231)
te.begin_fill()
curveto_r(-6, 0, -5, 5, -3, 8)
smooth_r(24, 2, 27, 0)
smooth_r(0, -8, -1, -8)
Smooth(234, 231, 227, 231)
te.end_fill()

Moveto(361, 227)
te.begin_fill()
curveto_r(2, 18, 26, 14, 30, 6)
smooth_r(-1, -3, -2, -4)
smooth_r(-15, 9, -24, -4)
Curveto(363, 224, 361, 225, 361, 227)
te.end_fill()

# 图层_16
te.pencolor("black")  # 眼睛(线条)
te.pensize(3)
# Moveto(206,213)
# lineto(14,-8)
# curveto_r(3,-1,30,0,33,1)
# lineto(10,6)
Moveto(225, 215)
curveto_r(10, 28, 22, 16, 24, 6)
Moveto(365, 219)
curveto_r(4, 14, 18, 24, 22, -3)
te.pensize(2)
line(240.5, 207.5, 227.5, 211.5)
line(245.5, 209.5, 227.5, 214.5)
line(247.5, 211.5, 227.5, 217.5)
line(247.5, 214.5, 229.5, 220.5)
line(247.5, 218.5, 230.5, 223.5)
line(246.5, 222.5, 232.5, 226.5)
line(244.5, 225.5, 234.5, 228.5)

line(377.5, 207.5, 367.5, 210.5)
line(384.5, 207.5, 366.5, 212.5)
line(385.5, 210.5, 366.5, 215.5)
line(384.5, 213.5, 366.5, 218.5)
line(384.5, 215.5, 367.5, 220.5)
line(384.5, 218.5, 368.5, 223.5)
# line(383.5,220.5,368.5,225.5)
line(382.5, 223.5, 370.5, 227.5)
# line(381.5,226.5,373.5,229.5)
# 图层_20
te.pencolor("black")
Moveto(309, 270)  # 鼻子、嘴
curveto_r(0, 0, 4, 7, 1, 9)
line(296.5, 307.5, 303.5, 307.5)
Moveto(315, 307)
smooth_r(10, -1, 10, 2)

te.penup()
te.hideturtle()
te.update()
te.done()
