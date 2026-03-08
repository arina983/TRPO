#include <iostream>
#include "gemmtr.h"

int main() {

    int n = 2;

    float A[4] = {1,2,3,4};
    float B[4] = {5,6,7,8};
    float C[4] = {0};

    sgemmtr(n, n, n, 1, A, B, 0, C, true);

    for(int i=0;i<4;i++)
    std::cout << C[i] << " ";
    std::cout << std::endl;

}
 
