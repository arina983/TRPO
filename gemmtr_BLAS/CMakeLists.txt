cmake_minimum_required(VERSION 3.10)
project(gemmtr)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenBLAS REQUIRED)

add_library(gemmtr gemmtr.cpp)

add_executable(test test.cpp)
add_executable(benchmark benchmark.cpp)

target_link_libraries(test PRIVATE gemmtr OpenBLAS::OpenBLAS)
target_link_libraries(benchmark PRIVATE gemmtr OpenBLAS::OpenBLAS)