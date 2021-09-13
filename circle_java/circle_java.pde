int x_size = 400;
int y_size = 400;
int cx = x_size/2;
int cy = y_size/2;
//from colors import colors

int radius = 150;
int diameter = 2*radius;
int points = 360;
int amplitude = 30;
int waves = 10;
float increment = TWO_PI / points;
int frame_rate = 30;

void settings() {
    size(x_size, y_size);
}

void setup() {
    //global x_size, y_size, cx, cy, radius, diameter, points, amplitude, waves, increment, frame_rate
    frameRate(frame_rate);
    base_drawing();
}

void base_drawing() {
    background(240);
    simple_circle();
    manual_circle_wavy();
}

void simple_circle() {
    strokeWeight(5);
    stroke(colors.get("orange"));
    //fill(255, 255, 255, 0);
    noFill();
    circle(cx, cy, diameter);
}

//void circle_waves() {
//    strokeWeight(1);
//    stroke(colors.get("black"));
//    noFill();
//    sections = 1000;
//    increment = TWO_PI / sections;
//    amplitude = 40;
//    waves = 20;
//    for i in range(sections):
//        d = diameter + ( amplitude * sin(i*increment*waves) );
//        arc(cx, cy,
//            d, d,
//            i*increment, (i+1)*increment);
//}

//void manual_circle() {
//    r = 50;
//    points = 60;
//    increment = TWO_PI / points;
//    strokeWeight(2);
//    stroke(colors.get("blue"));
//    for i in range(points):
//        point(cx + r*cos(i*increment),
//              cy + r*sin(i*increment));
//}

void manual_circle_wavy() {
    strokeWeight(2);
    stroke(colors.get("blue"));
    for (int i=0; i<points; i++) { //i in range(points):
        r = radius + ( amplitude * sin(i*increment*waves) );
        point(cx + r*cos(i*increment),
              cy + r*sin(i*increment));
    }
}

int j = -1;
void draw() {
    //global j, cx, cy, radius, diameter, points, amplitude, waves, increment
    j++;
    angle = j * increment;
    
    //mouse_pause();
    mouse_slow(1, frame_rate);
    
    if (j >= points) {
        j = 0;
        base_drawing();
    }
    
    noStroke();
    // stroke(colors.get("green"));
    // strokeWeight(1);
    fill(240);
    rect(cx-40, cy-20, 150, 60);
    fill(colors.get("black"));
    
    //report = '\n'.join(['frameCount: {}',
    //                    'j: {}',
    //                    'angle: {}',
    //                    ]).format(frameCount, j, angle);
    //text(report, cx-40, cy);

    strokeWeight(5);
    stroke(colors.get("fuchsia"));
    r = radius + ( amplitude * sin(angle*waves) );
    point(cx + r*cos(angle),
          cy + r*sin(angle));
}//draw

void mouse_pause() {
    if (mousePressed) {
        noLoop();
        while (mousePressed) {
            delay(100);
        }
        loop();
    }
}

void mouse_slow(int fr_slow, int fr_fast) {
    if (mousePressed) {
        frameRate(fr_slow);
    } else {
        frameRate(fr_fast);
    }
}
