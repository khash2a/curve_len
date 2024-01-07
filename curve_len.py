# Length of the cureve
import numpy as np
np.set_printoptions(precision=4, linewidth = 100, suppress=True)

def curve_len2(x0, y0, x1, y1): # Length of the cubic curve thru (0,0), (1,0), (x0, y0), (x1,y1)
    de = x0 * x1 * (x1 - 1) * (x0 - 1) * (x0 - x1)
    na = x1 * (x1 - 1) * y0 - x0 * (x0 - 1) * y1
    nb = -x1 * x1 * (x1 - 1) * y0 + x0 * x0 * (x0 - 1) * y1
    a = na / de
    b = nb / de
    return 1 + (2*a*a + 5*a*b + 5*b*b)/30

# The length of arc [(x0,y0), (x1,y1)] using also (x2,y2), (x3,y3)
def len_P0P1(x0, y0, x1, y1, x2, y2, x3, y3):
    x1 -= x0
    y1 -= y0
    x2 -= x0
    y2 -= y0
    x3 -= x0
    y3 -= y0

    len1 = x1 * x1 + y1 * y1
    len2 = 1 / len1

    xs2 = (x2 * x1 + y2 * y1) * len2
    ys2 = (-x2 * y1 + y2 * x1) * len2
    xs3 = (x3 * x1 + y3 * y1) * len2
    ys3 = (-x3 * y1 + y3 * x1) * len2

    return curve_len2(xs2, ys2, xs3, ys3) * np.sqrt(len1)

def curve_len_simple(x,y):
    result = 0
    for i in range(1, len(x)):
        dx = x[i]-x[i-1]
        dy = y[i]-y[i-1]
        result += np.sqrt(dx*dx + dy*dy)
    return result

# Length of the curve pass thru (x[0],y[0]), (x[1],y[1]), (x[2],y[2]), ...
def curve_len(x, y):
    s = len_P0P1(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3]) # First arc
    s += len_P0P1(x[-1],y[-1], x[-2],y[-2], x[-3],y[-3], x[-4],y[-4]) # Last arc

    for i in range(len(x)-3): # Middle arcs
        s += len_P0P1(x[i+1], y[i+1], x[i+2], y[i+2], x[i], y[i], x[i+3], y[i+3])
    return s


if __name__ == '__main__':
    # quarter of circle:
    Pi2 = np.pi/2
    print(f'quarter of circle, Pi/2={np.pi/2:9.7f}')
    for N in range(4,21):
        x = np.zeros(N)
        y = np.zeros(N)
        al = np.pi/(2*(N-1))
        for i in range(N):
            x[i] = np.cos(i*al)
            y[i] = np.sin(i*al)
        res = curve_len(x,y)
        ress = curve_len_simple(x,y)
        print(f' N={N:3d}, simpl:{Pi2-ress:8.1e}, len:{Pi2-res:8.1e}')

    # A quarter of astroid (x**(2/3) + y**(2/3)=1), length = 1.5
    print(f'Astroida: len=1.5')
    for N in range(4,21):
        x = np.zeros(N)
        y = np.zeros(N)
        for i in range(N):
            x1 = i/(N-1)
            x[i] = x1
            y[i] = (1-x1**(2/3))**(3/2)
        res = curve_len(x,y)
        ress = curve_len_simple(x,y)
        print(f' N={N:3d}, simpl:{1.5-ress:8.1e}, len:{1.5-res:8.1e}')

'''
quarter of circle, Pi/2=1.5707963
 N=  4, simpl: 1.8e-02, len: 8.3e-03
 N=  5, simpl: 1.0e-02, len: 1.5e-03
 N=  6, simpl: 6.5e-03, len: 2.3e-04
 N=  7, simpl: 4.5e-03, len: 6.2e-06
 N=  8, simpl: 3.3e-03, len:-3.1e-05
 N=  9, simpl: 2.5e-03, len:-3.2e-05
 N= 10, simpl: 2.0e-03, len:-2.6e-05
 N= 11, simpl: 1.6e-03, len:-2.0e-05
 N= 12, simpl: 1.3e-03, len:-1.6e-05
 N= 13, simpl: 1.1e-03, len:-1.2e-05
 N= 14, simpl: 9.6e-04, len:-9.3e-06
 N= 15, simpl: 8.2e-04, len:-7.3e-06
 N= 16, simpl: 7.2e-04, len:-5.8e-06
 N= 17, simpl: 6.3e-04, len:-4.6e-06
 N= 18, simpl: 5.6e-04, len:-3.7e-06
 N= 19, simpl: 5.0e-04, len:-3.0e-06
 N= 20, simpl: 4.5e-04, len:-2.5e-06

Astroida: len=1.5
 N=  4, simpl: 1.6e-02, len: 9.5e-03
 N=  5, simpl: 1.1e-02, len: 3.5e-03
 N=  6, simpl: 7.7e-03, len: 2.1e-03
 N=  7, simpl: 5.9e-03, len: 1.5e-03
 N=  8, simpl: 4.7e-03, len: 1.1e-03
 N=  9, simpl: 3.9e-03, len: 9.1e-04
 N= 10, simpl: 3.3e-03, len: 7.6e-04
 N= 11, simpl: 2.8e-03, len: 6.5e-04
 N= 12, simpl: 2.5e-03, len: 5.6e-04
 N= 13, simpl: 2.2e-03, len: 4.9e-04
 N= 14, simpl: 1.9e-03, len: 4.4e-04
 N= 15, simpl: 1.7e-03, len: 3.9e-04
 N= 16, simpl: 1.6e-03, len: 3.6e-04
 N= 17, simpl: 1.4e-03, len: 3.2e-04
 N= 18, simpl: 1.3e-03, len: 3.0e-04
 N= 19, simpl: 1.2e-03, len: 2.7e-04
 N= 20, simpl: 1.1e-03, len: 2.5e-04

'''