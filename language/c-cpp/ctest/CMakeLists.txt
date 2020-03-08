cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 14)
project(test_sqrt)

include_directories(
include
)

add_library(mytest1 STATIC src/lib1.c src/lib2.c src/b1.c src/b2.c)
add_library(mytest2 STATIC src/lib1.c src/lib2.c src/b1.c src/b2.c)

add_executable(${PROJECT_NAME} src/main.c)

# 对于重名的函数，加上这个标签就可以在链接的时候去重
# set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -all_load")
target_link_libraries(${PROJECT_NAME} mytest1)
target_link_libraries(${PROJECT_NAME} mytest2)
