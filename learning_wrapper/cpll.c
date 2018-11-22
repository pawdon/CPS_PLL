void test(double *carr2, int carr2_length, double *carr3, int carr3_length, double *synch, int synch_length)
{
    int i;

    for (i = 0; i < carr2_length; i++)
    {
        carr2[i] += 2;
    }

    for (i = 0; i < carr3_length; i++)
    {
        carr3[i] += 3;
    }

    for (i = 0; i < synch_length; i++)
    {
        synch[i] += 1;
    }
}

void test2(double *carr2, int carr2_length, double *carr3, int carr3_length, double *synch, int synch_length)
{
    int i;

    for (i = 0; i < carr2_length; i++)
    {
        carr2[i] *= 2;
    }

    for (i = 0; i < carr3_length; i++)
    {
        carr3[i] *= 3;
    }

    for (i = 0; i < synch_length; i++)
    {
        synch[i] *= 1;
    }
}
