cmake_minimum_required(VERSION 3.10)
project(gemmtr)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(OPENBLAS_PATH "/mnt/c/Users/Ариша/OpenBLAS")

add_library(gemmtr gemmtr.cpp)

add_executable(test test.cpp)
add_executable(benchmark benchmark.cpp)

target_link_libraries(test PRIVATE gemmtr)
target_link_libraries(benchmark PRIVATE gemmtr)

target_link_libraries(gemmtr PRIVATE ${OPENBLAS_PATH}/libopenblas.so)