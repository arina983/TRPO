/* 
  программа неправильно 
  считает сумму элементов матрицы.
  
  логика программы:
  1. функция init() создает единичную квадратную матрицу N*N
  2. функция inc увеличивает все элементы на 1
  3. функция m_sum - считает сумму всеx элементов (должно быть 2*N*N)  
    
*/

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void init(int ***, int);
void destroy(int **, int);
void inc(int **, int);
long long int m_sum(int **, int);

static unsigned long long N = 10000;

int main(int argc, char **argv) {

    int num_ths;
    long long int res, t_res;

    printf("program start\n");

    if (argc != 2) {
        printf("usage: ./a.out num_threads\n");
        exit(1);
    }
    num_ths = atoi(argv[1]);

    if (num_ths < 1 || num_ths > 24) num_ths = 6;

    omp_set_num_threads(num_ths);

    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        printf("thread %d: Hello\n", tid);
    }

    int **matrix = NULL;
    init(&matrix, N);
    inc(matrix, N);

    res = m_sum(matrix, N);
    t_res = 2LL * N * N;

    printf("program's sum of elements of matrix  = %lld\n", res);
    printf("theoretical(right) sum of elements of matrix  = %lld\n", t_res);

    destroy(matrix, N);

    return 0;
}

/**************/

void init(int ***m, int n) {
    *m = (int **)malloc(sizeof(int *) * n);
    if (!(*m)) { perror("malloc"); exit(1); }

    for (int i = 0; i < n; i++) {
        (*m)[i] = (int *)malloc(sizeof(int) * n);
        if (!(*m)[i]) { perror("malloc"); exit(1); }
    }

    #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            (*m)[i][j] = 1;
}

/**************/

void destroy(int **m, int n) {
    for (int i = 0; i < n; i++) free(m[i]);
    free(m);
}

/**************/

void inc(int **m, int n) {
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            m[i][j]++;
}

/**************/

long long int m_sum(int **m, int n) {
    long long int res = 0;

    #pragma omp parallel for reduction(+:res) collapse(2)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            res += m[i][j];

    return res;
}