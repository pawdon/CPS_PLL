%module cpll

%{
    #define SWIG_FILE_WITH_INIT
    #include "cpll.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double *carr2, int carr2_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *carr3, int carr3_length)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *synch, int synch_length)}

%include "cpll.h"
