from colors import colors
x_size = 400
y_size = 400
cx = x_size//2
cy = y_size//2
s1_x = 0
s1_y = 0
s2_x = x_size
s2_y = 0

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
    
    report(frameCount, j, angle)
    px, py = circle_sine_point(angle)
    draw_point(px, py)
    suspend(px, py)
    distances(px, py)
#draw

def report(frameCount, j, angle):
    noStroke()
    # stroke(colors['green'])
    # strokeWeight(1)
    fill(240)
    rect(cx-40, cy-20, 140, 60)
    fill(colors['black'])
    
    report = '\n'.join(['frameCount: {}',
                        'j: {}',
                        'angle: {}',
                        ]).format(frameCount, j, angle)
    text(report, cx-40, cy)

def circle_sine_point(angle):
    r = radius + ( amplitude * sin(angle*waves) )
    x = cx + r*cos(angle)
    y = cy + r*sin(angle)
    return x, y

def draw_point(x, y):
    strokeWeight(5)
    stroke(colors['fuchsia'])
    point(x, y)

def suspend(x, y):
    strokeWeight(1)
    stroke(colors['lightblue'])
    line(s1_x, s1_y, x, y)
    line(s2_x, s2_y, x, y)

def distances(x, y):
    l1 = dist(s1_x, s1_y, x, y)
    l2 = dist(s2_x, s2_y, x, y)
    fill(240)
    noStroke()
    #stroke(colors['green'])
    #strokeWeight(1)
    rect(20, 5, 50, 20)
    rect(x_size-60, 5, 50, 20)
    fill(colors['black'])
    text(l1, 20, 20)
    text(l2, x_size-60, 20)

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
