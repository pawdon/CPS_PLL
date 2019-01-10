#include "cpll.h"
#include <math.h>


double get_lut(double x, double *lut_array, int lut_length)
{
	const double pi = 3.141592653589793;
	double norm = fmod(x, (2 * pi));
	unsigned int ind = (int)(lut_length * norm / (2 * pi));
	return lut_array[ind];
}


CPllState process1(double *pilot, int pilot_length, double *carr1, int carr1_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState state)
{
	int n;
	double perr;

	for (n = 0; n < state.N; n++)
	{
		carr1[n] = cos(state.latest_theta);
		carr2[n] = cos(2 * state.latest_theta);
		carr3[n] = cos(3 * state.latest_theta);
		perr = -pilot[n] * sin(state.latest_theta);
		state.latest_theta += state.freq + state.alpha * perr;
		state.freq += state.beta * perr;
	}
	return state;
}

CPllState process2(double *pilot, int pilot_length, double *carr1, int carr1_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState state)
{
	int n;
	double perr;

	double *pilot_ptr = pilot;
	double *carr1_ptr = carr1;
	double *carr2_ptr = carr2;
	double *carr3_ptr = carr3;

	for (n = 0; n < state.N; n++)
	{
		*carr1_ptr = cos(state.latest_theta);
		*carr2_ptr = cos(2 * state.latest_theta);
		*carr3_ptr = cos(3 * state.latest_theta);
		perr = -(*pilot_ptr) * sin(state.latest_theta);
		state.latest_theta += state.freq + state.alpha * perr;
		state.freq += state.beta * perr;

		++pilot_ptr;
		++carr1_ptr;
		++carr2_ptr;
		++carr3_ptr;
	}
	return state;
}

CPllState process3(double *pilot, int pilot_length, double *carr1, int carr1_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState state,
	double *lut_cos, int lut_cos_length, double *lut_sin, int lut_sin_length)
{
	int n;
	double perr;

	double *pilot_ptr = pilot;
	double *carr1_ptr = carr1;
	double *carr2_ptr = carr2;
	double *carr3_ptr = carr3;

	for (n = 0; n < state.N; n++)
	{
		*carr1_ptr = get_lut(state.latest_theta, lut_cos, lut_cos_length);
		*carr2_ptr = get_lut(2 * state.latest_theta, lut_cos, lut_cos_length);
		*carr3_ptr = get_lut(3 * state.latest_theta, lut_cos, lut_cos_length);
		perr = -(*pilot_ptr) * get_lut(state.latest_theta, lut_sin, lut_sin_length);
		state.latest_theta += state.freq + state.alpha * perr;
		state.freq += state.beta * perr;

		++pilot_ptr;
		++carr1_ptr;
		++carr2_ptr;
		++carr3_ptr;
	}
	return state;
}