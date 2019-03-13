from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    prev_x = r * math.cos(t) + cx
    prev_y = r * math.sin(t) + cy
    s = (math.pi*2)/step
    t+= s
    while (t <= (math.pi * 2)):
        x = r * math.cos(t) + cx
        y = r * math.sin(t) + cy
        add_edge(points,prev_x,prev_y,cz,x,y,cz)
        prev_x = x
        prev_y = y
        t += s
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    if curve_type == 'hermite':
        make_hermite(points,x0,y0,x1,y1,x2,y2,x3,x3,step)
    pass


def make_hermite(points,x0,y0,x1,y1,rx0,ry0,rx1,ry1,step):
    step_size = 1.0/(step)
    t = 0
    prevx = herm_help(x0,x1,rx0,rx1)
    prevy = herm_help(y0,y1,ry0,ry1)
    t+=step_size
    while (t <= 1):
        x = herm_help(x0,x1,rx0,rx1)
        y = herm_help(y0,y1,ry0,ry1)
        add_edge(points,prevx,prevy,0,x,y,0)
        prevx = x
        prevy = y
        t+=step_size
    pass

def herm_help(p0,p1,r0,r1,i):
    (2*i**3 - 3*i**2 + 1)*p0 + (-2*i**3 + 3*i**2)*p1 + (i**3 - 2*i**2 + i)*r0 + (i**3 -  i**2 )*r1

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
