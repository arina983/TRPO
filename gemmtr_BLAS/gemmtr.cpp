#include "gemmtr.h"
void sgemmtr(int n, int m, int k, float alpha, const float* A, const float* B, float beta, float* C, bool upper) {
    for (int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if (upper && j < i) continue;
            if (!upper && j > i) continue;

            float sum = 0;

            for (int p = 0;p < k; p++)
            sum += A[i*k+p] * B[p*m+j];

            C[i*m+j] = alpha * sum + beta * C[i*m+j];

        }
    }
}

void dgemmtr(int n, int m, int k, double alpha, const double* A, const double* B, double beta, double* C, bool upper) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (upper && j < i) continue;
            if (!upper && j > i) continue;

            double sum=0;

            for (int p = 0; p < k; p++)
            sum += A[i*k+p]*B[p*m+j];

            C[i*m+j] = alpha * sum + beta * C[i*m+j];

        }
    }
} 
