#import math
x_size = 400
y_size = 400
cx = x_size//2
cy = y_size//2
from colors import colors

radius = 150
diameter = 2*radius
points = 360
amplitude = 30
waves = 10
increment = TWO_PI / points
frame_rate = 30

def setup():
    global x_size, y_size, cx, cy, radius, diameter, points, amplitude, waves, increment, frame_rate
    size(x_size, y_size)
    frameRate(frame_rate)
    base_drawing()
    
def base_drawing():
    background(240)
    simple_circle()
    manual_circle_wavy()

def simple_circle():
    strokeWeight(5)
    stroke(colors['orange'])
    #fill(255, 255, 255, 0)
    noFill()
    circle(cx, cy, diameter)
    
def circle_waves():
    strokeWeight(1)
    stroke(colors['black'])
    noFill()
    sections = 1000
    increment = TWO_PI / sections
    amplitude = 40
    waves = 20
    for i in range(sections):
        d = diameter + ( amplitude * sin(i*increment*waves) )
        arc(cx, cy,
            d, d,
            i*increment, (i+1)*increment)
    
def manual_circle():
    r = 50
    points = 60
    increment = TWO_PI / points
    strokeWeight(2)
    stroke(colors['blue'])
    for i in range(points):
        point(cx + r*cos(i*increment),
              cy + r*sin(i*increment))
    
def manual_circle_wavy():
    strokeWeight(2)
    stroke(colors['blue'])
    for i in range(points):
        r = radius + ( amplitude * sin(i*increment*waves) )
        point(cx + r*cos(i*increment),
              cy + r*sin(i*increment))

j = -1
def draw():
    global j, cx, cy, radius, diameter, points, amplitude, waves, increment
    j += 1
    angle = j * increment
    
    mouse_pause()
    
    if (j >= points):
        j = 0
        base_drawing()
    
    noStroke()
    # stroke(colors['green'])
    # strokeWeight(1)
    fill(240)
    rect(cx-40, cy-20, 150, 60)
    fill(colors['black'])
    
    report = '\n'.join(['frameCount: {}',
                        'j: {}',
                        'angle: {}',
                        ]).format(frameCount, j, angle)
    text(report, cx-40, cy)

    strokeWeight(5)
    stroke(colors['fuchsia'])
    r = radius + ( amplitude * sin(angle*waves) )
    point(cx + r*cos(angle),
          cy + r*sin(angle))
#draw

def mouse_pause(fr_slow=1, fr_fast=frame_rate):
    if (mousePressed and mouseButton==LEFT):
        noLoop()
        while mousePressed:
            delay(100)
        else:
            loop()
    elif (mousePressed and mouseButton==RIGHT):
        frameRate(fr_slow)
    else:
        frameRate(fr_fast)
