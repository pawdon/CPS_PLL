typedef struct
{
	double freq;
	double latest_theta;
	double alpha;
	double beta;
	unsigned int N;
} CPllState;

CPllState process1(double *pilot, int pilot_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState synch);
CPllState process2(double *pilot, int pilot_length, double *carr2, int carr2_length, double *carr3, int carr3_length, CPllState synch,
	double *lut_cos, int lut_cos_length, double *lut_sin, int lut_sin_length);
