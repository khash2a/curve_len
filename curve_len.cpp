// Length of the curve pass thru points (x[0],y[0]), (x[1],y[1]), (x[2],y[2]), ... 
// (c) Khashin S.I. http://math.ivanovo.ac.ru/dalgebra/Khashin/index.html
// khash2@gmail.com
// public domain

// main function:
// double curve_len(vector<double>& x, vector<double>& y);

#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>

using namespace std;


// ----------------------------------------------------------------------------
//Length of the cubic curve thru (0,0), (1,0), (x0, y0), (x1,y1)
double curve_len2(double x0, double y0, double x1, double y1) 
{
	double a, b;
	double de = x0 * x1 * (x1 - 1) * (x0 - 1) * (x0 - x1);
	double na = x1 * (x1 - 1) * y0 - x0 * (x0 - 1) * y1;
	double nb = -x1 * x1 * (x1 - 1) * y0 + x0 * x0 * (x0 - 1) * y1;
	a = na / de;
	b = nb / de;
	return  1 + (2 * a * a + 5 * a * b + 5 * b * b) / 30;
}
// ----------------------------------------------------------------------------
// The length of arc [(x0,y0), (x1,y1)] using also (x2,y2), (x3,y3)
double len_P0P1(double x0, double y0, double x1, double y1, double x2, double y2, double x3, double y3 )
{
	x1 -= x0; y1 -= y0;
	x2 -= x0; y2 -= y0;
	x3 -= x0; y3 -= y0;

	double len1 = x1 * x1 + y1 * y1;
	double len2 = 1/len1;

	double xs2 = (x2 * x1 + y2 * y1)*len2;
	double ys2 = (-x2 * y1 + y2 * x1)* len2;
	
	double xs3 = (x3 * x1 + y3 * y1)* len2;
	double ys3 = (-x3 * y1 + y3 * x1)* len2;

	return curve_len2(xs2, ys2, xs3, ys3)*sqrt(len1);
}
// ----------------------------------------------------------------------------
// Length of the curve pass thru (x[0],y[0]), (x[1],y[1]), (x[2],y[2]), ...
double curve_len(vector<double>& x, vector<double>& y) {
	int N = (int)x.size();

	double s = len_P0P1(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3]); // First arc
	s += len_P0P1(x[N-1], y[N-1], x[N-2], y[N-2], x[N-3], y[N-3], x[N-4], y[N-4]); // Last arc

	for(int i=0; i<N-3; i++) // Middle arcs
		s += len_P0P1(x[i+1], y[i+1], x[i+2], y[i+2], x[i], y[i], x[i+3], y[i+3]);
	return s;
}
// ----------------------------------------------------------------------------

int main()
{
	// Quarter of the circle :
	double Pi2 = 3.141592653589793 / 2;
	printf("Half of circle, Pi/2=%9.7f\n", Pi2);
	for (int N = 4; N <= 20; N++) {
		vector<double>x(N);
		vector<double>y(N);
		double al = Pi2 / (N - 1);
		for (int i = 0; i < N; i++) {
			x[i] = cos(i * al);
			y[i] = sin(i * al);
		}
		double res = curve_len(x, y);
		printf(" N=%3d, acc=%8.1e\n", N, res - Pi2);
	}
	// A quarter of the astroid  (x**(2/3) + y**(2/3) = 1), length = 1.5
	printf("\nAstroida: len=1.5\n");
	for (int N = 4; N <= 20; N++) {
		vector<double>x(N);
		vector<double>y(N);
		for (int i = 0; i < N; i++) {
			x[i] = i / (N - 1.);
			y[i] = pow(1 - pow(x[i], 2. / 3), 3. / 2);
		}
		double res = curve_len(x, y);
		printf(" N=%3d, acc=%8.1e\n", N, res - 1.5);
	}
	getchar();
}

