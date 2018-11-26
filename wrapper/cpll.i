%module cpll

%{
    #define SWIG_FILE_WITH_INIT
    #include "cpll.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double *pilot, int pilot_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *carr2, int carr2_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *carr3, int carr3_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *lut_cos, int lut_cos_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *lut_sin, int lut_sin_length)}

%include "cpll.h"
