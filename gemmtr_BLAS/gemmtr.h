#pragma once

void sgemmtr(
    int n,
    int m,
    int k,
    float alpha,
    const float* A,
    const float* B,
    float beta,
    float* C,
    bool upper
);

void dgemmtr(
    int n,
    int m,
    int k,
    double alpha,
    const double* A,
    const double* B,
    double beta,
    double* C,
    bool upper
);