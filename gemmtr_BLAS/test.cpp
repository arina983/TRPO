#include <iostream>
#include "gemmtr.h"

int main() {

    int n = 2;

    float A_s[4] = {1,2,3,4};
    float B_s[4] = {5,6,7,8};
    float C_s[4] = {0};

    double A_d[4] = {1,2,3,4};
    double B_d[4] = {5,6,7,8};
    double C_d[4] = {0};

    sgemmtr(n, n, n, 1, A_s, B_s, 0, C_s, true);
    dgemmtr(n, n, n, 1, A_d, B_d, 0, C_d, true);

    std::cout << "sgemmtr: ";
    for(int i = 0; i < 4; i++)
        std::cout << C_s[i] << " ";
    std::cout << std::endl;

    std::cout << "dgemmtr: ";
    for(int i = 0; i < 4; i++)
        std::cout << C_d[i] << " ";
    std::cout << std::endl;

    return 0;

}
 
