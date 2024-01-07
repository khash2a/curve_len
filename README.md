# curve_len
Length of the curve pass thru points (x[0],y[0]), (x[1],y[1]), (x[2],y[2]), ... 

\section{Introduction}

The length of a smooth plane curve given parametrically x=x(t), y=y(t) 
for a <= t <= b can be found using the integral
\[
 s = \int_a^b \sqrt{x'(t)^2 + y'(t)^2}\, dt.
\]
If the integral cannot be found analytically, it can be found
numerically. But for this, the functions x(t), y(t) must be
specified.

In practice, the curve is sometimes defined using some set of points
$(P_1, \dots, P_n)$ belonging to the curve. In this case, the length
of the curve can be estimated in terms of the length of the polyline
with the same vertices.

In fact, the length of the curve passing through the given points
can be approximated more accurately. This is what this work is
dedicated to.

\section{Main formula}

Consider a cubic curve of the form

 y(x) = x(x-1)(ax+b).

It passes through the points P1(0,0) and P2(1,0). We will
consider the parameters a and b are small. Let's find
approximate formulas for the length of its arc between the points
P1 and P2.

 L = \int_0^1 \sqrt{1+y'(x)}dx


The result of decomposing into a Taylor series:

          2a^2 + 5ab + 5b^2
 L = 1 + ------------------  + O^4(a,b).     (1)
                30 
 
If we have 4 consecutive points on the curve (P0, P1, P2, P3,
we will replace the coordinates on the plane, translating the point
P1 to (0,0), the point P_2 to (0,1). In this case, the
point P0 will move to the point with coordinates (x0, y0),
the point P2 to the point with coordinates (x2, y3).

Then we find a cubic curve passing through the points (x0, y0),
(0,0), (1,0), (x2, y2) and using the  formula (1) we
find the length of the arc from the point (0,0) to (1,0).

If the number of points is more than 4, then we split the
consecutive fours $(P_i, P_{i+1}, P_{i+2}, P_{i+3})$ and find the
length of each of the central arcs $(P_{i+1}, P_{i+2})$.

The lengths of the edge arcs $(P_1, P_2)$ and $(P_{n-1}, P_n)$ we
will find by a similar method.

\section{Results}

To check, consider two examples: the arc length of a quarter of a
circle and the astroids $x^{2/3} + y^{2/3}=1$.

The points on the circle were taken at equal angular intervals, the
points on the astroid thru an equal intervals on the ordinate axis.

Colunms in table:
N: the number of points,
acc_1: the accuracy of the length of the polyline arc for a quarter of a circle,
acc_2: the accuracy of our approximation,
acc_3: the accuracy of the length of the polyline arc for a quarter of astroid,
acc_4: the accuracy of our approximation.

   N     acc_1       acc_2      acc_3       acc_4
   4     1.8e-2     8.3e-3     1.6e-2      9.5e-3
   5     1.0e-2     1.5e-3     1.1e-2      3.5e-3
   6     6.5e-3     2.3e-4     7.7e-3      2.1e-3
   8     3.3e-3     3.2e-5     4.7e-3      1.1e-3
  10     2.0e-3     2.7e-5     3.3e-3      7.6e-4
  15     8.2e-4     8.0e-6     1.7e-3      3.9e-4
  20     4.5e-4     2.5e-6     1.1e-3      2.5e-4

