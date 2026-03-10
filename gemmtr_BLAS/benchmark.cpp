#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>
#include "gemmtr.h"

extern "C" {
    #include <cblas.h>
    #include <openblas_config.h>
}

double run_my(int n,std::vector<double>&A,std::vector<double>&B,std::vector<double>&C) {
    auto start=std::chrono::high_resolution_clock::now();
    dgemmtr(n,n,n,1,A.data(),B.data(),0,C.data(),true);
    auto end=std::chrono::high_resolution_clock::now();
    return std::chrono::duration<double>(end-start).count();
}

double run_openblas(int n,std::vector<double>&A,std::vector<double>&B,std::vector<double>&C) {
    auto start=std::chrono::high_resolution_clock::now();
    cblas_dgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,n,n,n,1,A.data(),n,B.data(),n,0,C.data(),n);
    auto end=std::chrono::high_resolution_clock::now();
    return std::chrono::duration<double>(end-start).count();
}

int main() {

    int n=500;

    std::vector<double>A(n*n);
    std::vector<double>B(n*n);
    std::vector<double>C(n*n);

    for(auto &x:A) x=1;
    for(auto &x:B) x=1;
    for(auto &x:C) x=0;

    int threads[5]={1,2,4,8,16};

    for(int t:threads) {

    openblas_set_num_threads(t);

    std::cout<<"Threads "<<t<<std::endl;

    double geom=1;

    for(int i=0;i<10;i++) {
        double t1=run_my(n,A,B,C);
        double t2=run_openblas(n,A,B,C);

        double perf=(t2/t1)*100;
        geom*=perf;

        std::cout<<"Run "<<i+1<<" "<<perf<<"%"<<std::endl;
    }
    geom=pow(geom,1.0/10.0);
    std::cout<<"Geometric mean "<<geom<<"%"<<std::endl;
    }
}
