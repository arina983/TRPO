# test_level2_cblas.py
# Простые тесты на Level 2 BLAS (matrix-vector) с OpenBLAS через ctypes

import ctypes
import numpy as np

# Комплексные типы
class c_float_complex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_float), ("imag", ctypes.c_float)]

class c_double_complex(ctypes.Structure):
    _fields_ = [("real", ctypes.c_double), ("imag", ctypes.c_double)]

# Загрузка библиотеки
blas = ctypes.CDLL("/mnt/c/Users/Ариша/OpenBLAS/build/lib/libopenblas.so")

# Константы
CblasRowMajor = 101
CblasNoTrans  = 111
CblasTrans    = 112
CblasUpper = 121
CblasLower = 122
CblasNonUnit = 131
CblasUnit = 132

# Настройка сигнатур (только один раз в начале)
blas.cblas_dgemv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]
blas.cblas_dgemv.restype = None

blas.cblas_sgemv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int
]
blas.cblas_sgemv.restype = None

blas.cblas_chemv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_float_complex),
    ctypes.POINTER(c_float_complex), ctypes.c_int,
    ctypes.POINTER(c_float_complex), ctypes.c_int,
    ctypes.POINTER(c_float_complex),
    ctypes.POINTER(c_float_complex), ctypes.c_int
]
blas.cblas_chemv.restype = None

blas.cblas_zhemv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_double_complex),
    ctypes.POINTER(c_double_complex), ctypes.c_int,
    ctypes.POINTER(c_double_complex), ctypes.c_int,
    ctypes.POINTER(c_double_complex),
    ctypes.POINTER(c_double_complex), ctypes.c_int
]
blas.cblas_zhemv.restype = None

blas.cblas_ssymv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int
]
blas.cblas_ssymv.restype = None

blas.cblas_dsymv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]
blas.cblas_dsymv.restype = None

blas.cblas_strmv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int
]
blas.cblas_strmv.restype = None

blas.cblas_dtrmv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]
blas.cblas_dtrmv.restype = None

blas.cblas_ctrmv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_float_complex), ctypes.c_int,
    ctypes.POINTER(c_float_complex), ctypes.c_int
]
blas.cblas_ctrmv.restype = None

blas.cblas_ztrmv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_double_complex), ctypes.c_int,
    ctypes.POINTER(c_double_complex), ctypes.c_int
]
blas.cblas_ztrmv.restype = None

blas.cblas_strsv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.c_int
]
blas.cblas_strsv.restype = None

blas.cblas_ztrsv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_double_complex), ctypes.c_int,
    ctypes.POINTER(c_double_complex), ctypes.c_int
]
blas.cblas_ztrsv.restype = None

blas.cblas_dtrsv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]
blas.cblas_dtrsv.restype = None

blas.cblas_ctrsv.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(c_float_complex), ctypes.c_int,
    ctypes.POINTER(c_float_complex), ctypes.c_int
]
blas.cblas_ctrsv.restype = None


# ───────────────────────────────────────────────
# Тесты (без повторной настройки argtypes внутри функций)
# ───────────────────────────────────────────────

def test_dgemv_no_trans():
    m, n = 3, 4
    A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]], dtype=np.float64)
    x = np.array([2,-1,0.5,3], dtype=np.float64)
    y = np.array([10,20,30], dtype=np.float64)
    alpha, beta = 2.0, 0.5
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    blas.cblas_dgemv(CblasRowMajor, CblasNoTrans, m, n, alpha, A_ptr, n, x_ptr, 1, beta, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-10, atol=1e-12, err_msg="dgemv no trans failed")


def test_sgemv_no_trans():
    m, n = 3, 4
    A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]], dtype=np.float32)
    x = np.array([2,-1,0.5,3], dtype=np.float32)
    y = np.array([10,20,30], dtype=np.float32)
    alpha, beta = 2.0, 0.5
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    blas.cblas_sgemv(CblasRowMajor, CblasNoTrans, m, n, alpha, A_ptr, n, x_ptr, 1, beta, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-5, atol=1e-5, err_msg="sgemv no trans failed")


def test_chemv_lower():
    n = 4
    A = np.zeros((n, n), dtype=np.complex64)
    for i in range(n):
        A[i,i] = np.random.uniform(-3,3)
    for i in range(n):
        for j in range(i+1,n):
            re, im = np.random.uniform(-2,2,2)
            A[i,j] = re + 1j*im
            A[j,i] = re - 1j*im

    x = (np.random.uniform(-2,2,n) + 1j*np.random.uniform(-2,2,n)).astype(np.complex64)
    y = (np.random.uniform(-3,3,n) + 1j*np.random.uniform(-3,3,n)).astype(np.complex64)
    alpha = 1.4 + 0.6j
    beta  = -0.5 + 0.3j
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_float_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_float_complex))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(c_float_complex))

    alpha_ptr = ctypes.pointer(c_float_complex(alpha.real, alpha.imag))
    beta_ptr  = ctypes.pointer(c_float_complex(beta.real, beta.imag))

    blas.cblas_chemv(CblasRowMajor, CblasLower, n, alpha_ptr, A_ptr, n, x_ptr, 1, beta_ptr, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-5, atol=1e-5, err_msg="chemv lower failed")


def test_zhemv_upper():
    n = 4
    A = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        A[i,i] = np.random.uniform(-4,4)
    for i in range(n):
        for j in range(i+1,n):
            re, im = np.random.uniform(-3,3,2)
            A[i,j] = re + 1j*im
            A[j,i] = re - 1j*im

    x = (np.random.uniform(-2,2,n) + 1j*np.random.uniform(-2,2,n)).astype(np.complex128)
    y = (np.random.uniform(-3,3,n) + 1j*np.random.uniform(-3,3,n)).astype(np.complex128)
    alpha = 2.1 - 0.7j
    beta  = 0.4 + 1.1j
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_double_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_double_complex))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(c_double_complex))

    alpha_ptr = ctypes.pointer(c_double_complex(alpha.real, alpha.imag))
    beta_ptr  = ctypes.pointer(c_double_complex(beta.real, beta.imag))

    blas.cblas_zhemv(CblasRowMajor, CblasUpper, n, alpha_ptr, A_ptr, n, x_ptr, 1, beta_ptr, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-10, atol=1e-12, err_msg="zhemv upper failed")


def test_ssymv_lower():
    n = 5
    A = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        A[i,i] = np.random.uniform(-4,4)
    for i in range(n):
        for j in range(i+1,n):
            val = np.random.uniform(-3,3)
            A[i,j] = val
            A[j,i] = val

    x = np.random.uniform(-2,2,n).astype(np.float32)
    y = np.random.uniform(-3,3,n).astype(np.float32)
    alpha, beta = 1.5, 0.7
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    blas.cblas_ssymv(CblasRowMajor, CblasLower, n, alpha, A_ptr, n, x_ptr, 1, beta, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-5, atol=1e-5, err_msg="ssymv lower failed")


def test_dsymv_upper():
    n = 5
    A = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        A[i,i] = np.random.uniform(-5,5)
    for i in range(n):
        for j in range(i+1,n):
            val = np.random.uniform(-4,4)
            A[i,j] = val
            A[j,i] = val

    x = np.random.uniform(-2,2,n).astype(np.float64)
    y = np.random.uniform(-3,3,n).astype(np.float64)
    alpha, beta = 2.3, -0.8
    expected = alpha * (A @ x) + beta * y

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    blas.cblas_dsymv(CblasRowMajor, CblasUpper, n, alpha, A_ptr, n, x_ptr, 1, beta, y_ptr, 1)
    np.testing.assert_allclose(y, expected, rtol=1e-10, atol=1e-12, err_msg="dsymv upper failed")


def test_strmv_lower_nonunit():
    n = 5
    A = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.uniform(-3,3)

    x = np.random.uniform(-2,2,n).astype(np.float32)
    expected = np.tril(A) @ x

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    blas.cblas_strmv(CblasRowMajor, CblasLower, CblasNoTrans, CblasNonUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-5, atol=1e-5, err_msg="strmv lower non-unit failed")


def test_dtrmv_upper_unit():
    n = 5
    A = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        A[i,i] = 1.0
        for j in range(i+1,n):
            A[i,j] = np.random.uniform(-4,4)

    x = np.random.uniform(-2,2,n).astype(np.float64)
    expected = np.triu(A) @ x

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    blas.cblas_dtrmv(CblasRowMajor, CblasUpper, CblasNoTrans, CblasUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-12, atol=1e-12, err_msg="dtrmv upper unit failed")


def test_ctrmv_lower_nonunit():
    n = 5
    A = np.zeros((n, n), dtype=np.complex64)
    for i in range(n):
        for j in range(i+1):
            re, im = np.random.uniform(-3,3,2)
            A[i,j] = re + 1j*im

    x = (np.random.uniform(-2,2,n) + 1j*np.random.uniform(-2,2,n)).astype(np.complex64)
    expected = np.tril(A) @ x

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_float_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_float_complex))

    blas.cblas_ctrmv(CblasRowMajor, CblasLower, CblasNoTrans, CblasNonUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-5, atol=1e-5, err_msg="ctrmv lower non-unit failed")


def test_ztrmv_upper_unit():
    n = 5
    A = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        A[i,i] = 1 + 0j
        for j in range(i+1,n):
            re, im = np.random.uniform(-4,4,2)
            A[i,j] = re + 1j*im

    x = (np.random.uniform(-2,2,n) + 1j*np.random.uniform(-2,2,n)).astype(np.complex128)
    expected = np.triu(A) @ x

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_double_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_double_complex))

    blas.cblas_ztrmv(CblasRowMajor, CblasUpper, CblasNoTrans, CblasUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-11, atol=1e-11, err_msg="ztrmv upper unit failed")


def test_strsv_lower_nonunit():
    n = 5
    A = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.uniform(-3,3) if i != j else np.random.uniform(1,5)

    b = np.random.uniform(-3,3,n).astype(np.float32)
    expected = np.linalg.solve(np.tril(A), b)

    x = b.copy()

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    blas.cblas_strsv(CblasRowMajor, CblasLower, CblasNoTrans, CblasNonUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-5, atol=1e-5, err_msg="strsv lower non-unit failed")


def test_ztrsv_upper_unit():
    n = 5
    A = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        A[i,i] = 1 + 0j
        for j in range(i+1,n):
            re, im = np.random.uniform(-4,4,2)
            A[i,j] = re + 1j*im

    b = (np.random.uniform(-3,3,n) + 1j*np.random.uniform(-3,3,n)).astype(np.complex128)
    expected = np.linalg.solve(np.triu(A), b)

    x = b.copy()

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_double_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_double_complex))

    blas.cblas_ztrsv(CblasRowMajor, CblasUpper, CblasNoTrans, CblasUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-11, atol=1e-11, err_msg="ztrsv upper unit failed")


def test_dtrsv_lower_nonunit():
    n = 5
    A = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.uniform(-3,3) if i != j else np.random.uniform(1,5)

    b = np.random.uniform(-3,3,n).astype(np.float64)
    expected = np.linalg.solve(np.tril(A), b)

    x = b.copy()

    A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    blas.cblas_dtrsv(CblasRowMajor, CblasLower, CblasNoTrans, CblasNonUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-10, atol=1e-12, err_msg="dtrsv lower non-unit failed")


def test_ctrsv_upper_unit():
    n = 5
    A = np.zeros((n, n), dtype=np.complex64)
    for i in range(n):
        A[i,i] = 1 + 0j
        for j in range(i+1,n):
            re, im = np.random.uniform(-3,3,2)
            A[i,j] = re + 1j*im

    b = (np.random.uniform(-3,3,n) + 1j*np.random.uniform(-3,3,n)).astype(np.complex64)
    expected = np.linalg.solve(np.triu(A), b)

    x = b.copy()

    A_ptr = A.ctypes.data_as(ctypes.POINTER(c_float_complex))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(c_float_complex))

    blas.cblas_ctrsv(CblasRowMajor, CblasUpper, CblasNoTrans, CblasUnit, n, A_ptr, n, x_ptr, 1)
    np.testing.assert_allclose(x, expected, rtol=1e-4, atol=1e-5, err_msg="ctrsv upper unit failed")


if __name__ == "__main__":
    print("Запускаем простые тесты...")
    test_dgemv_no_trans()
    test_sgemv_no_trans()
    test_chemv_lower()
    test_zhemv_upper()
    test_ssymv_lower()
    test_dsymv_upper()
    test_strmv_lower_nonunit()
    test_dtrmv_upper_unit()
    test_ctrmv_lower_nonunit()
    test_ztrmv_upper_unit()
    test_strsv_lower_nonunit()
    test_ztrsv_upper_unit()
    test_dtrsv_lower_nonunit()
    test_ctrsv_upper_unit()
    print("\nВсе тесты завершены")