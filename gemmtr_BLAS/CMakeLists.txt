cmake_minimum_required(VERSION 3.12)
project(gemmtr)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(BLA_VENDOR OpenBLAS)
find_package(BLAS REQUIRED)

add_library(gemmtr STATIC gemmtr.cpp)

add_executable(test test.cpp)
add_executable(benchmark benchmark.cpp)

target_link_libraries(test PRIVATE gemmtr ${BLAS_LIBRARIES})
target_link_libraries(benchmark PRIVATE gemmtr ${BLAS_LIBRARIES})

message(STATUS "BLAS found: ${BLAS_LIBRARIES}")
message(STATUS "BLAS include: ${BLAS_INCLUDE_DIRS}")