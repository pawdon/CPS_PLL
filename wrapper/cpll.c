#include "cpll.h"
#include <math.h>

CPllState process1(double *pilot, int pilot_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState synch)
{
	int i;

	for (i = 0; i < synch.N; i++)
	{
		carr2[i] += 2 * pilot[i];
		carr3[i] += 3 * pilot[i];
	}

	synch.freq += 1;
	synch.latest_theta = sin(3.14 / 2);
	synch.alpha = 2 * acos(0.0);
	return synch;
}

CPllState process2(double *pilot, int pilot_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState synch, 
	double *lut_cos, int lut_cos_length, double *lut_sin, int lut_sin_length)
{
	int i;

	for (i = 0; i < synch.N; i++)
	{
		carr2[i] = lut_cos[i];
		carr3[i] = lut_sin[i];
	}

	synch.freq += 1;
	synch.latest_theta = sin(3.14 / 2);
	return synch;
}