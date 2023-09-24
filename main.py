# from turtle import Turtle
# from random import random

# t = Turtle()
# t.forward(100)
# t.left(90)
# t.backward(100)
# t.right(90)
# t.color("blue")
# t.width(4)
# t.forward(50)
# t.up()
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(150)
# t.down()
# t.right(90)
# t.forward(50)
# # t.home()
# x = t.pos()
# print(x)
# # t.clearscreen()
# t.width(1)
# # for steps in range(100):
# #     for c in ('blue', 'red', 'green'):
# #         t.color(c)
# #         t.forward(steps)
# #         t.right(90)
# t.fillcolor("red")
# t.up()
# # t.begin_fill()
# # t.home()
# # while True:
# #     t.forward(200)
# #     t.left(170)
# #     if abs(t.pos()) < 1:
# #         break
# # t.end_fill()
# t.home()
# # from random import random

# # for i in range(100):
# #     steps = int(random() * 100)
# #     angle = int(random() * 360)
# #     t.right(angle)
# #     t.fd(steps)

# # t = Turtle()
# # for i in range(100):
# #     steps = int(random() * 100)
# #     angle = int(random() * 360)
# #     t.right(angle)
# #     t.fd(steps)

# t.screen.title('Object-oriented turtle demo')
# t.screen.bgcolor("orange")


# t.screen.mainloop()
from turtle import Turtle

def f(nums: list[int]) -> list[int]:
    rel = []
    x = 1
    for i in nums:
        x *= i
        rel.append(x)
    return rel

def hoshiya(x: list):
    t = Turtle()
    t.color("red")
    t.width(2)
    t.up()
    for i, e in enumerate(x):
        y = 200 - 40 * i
        t.setpos(-200, y)
        l = 400 // (e + 1)
        for j in range(e):
            t.forward(l)
            t.down()
            t.circle(20)
            t.up()
    return t


def main():
    w = f([2, 2])
    x = hoshiya(w)
    x.screen.mainloop()

if __name__ == "__main__":
    main()
