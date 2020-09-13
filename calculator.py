import math

def getDegree(angel):
    angel = angel/180*math.pi
    return angel


angel = 20.5
v0 = 8
dis = 2
g=9.8
h0 =0.1


angel = getDegree(angel)

vx = 8*math.cos(angel)
vy = 8*math.sin(angel)

t = dis/vx
h = vy*t - 0.5*g*t**2

print(h+h0)
