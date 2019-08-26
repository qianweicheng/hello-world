# AUX_SOURCE_DIRECTORY(. SRC_LIST)
# INCLUDE_DIRECTORIES(/Users/qianweicheng/git2/python-cmake-buildsystem/)

# add_library( native-lib
#             SHARED
#             src/main/cpp/native-lib.cpp )
# gcc main.c `python3-config --cflags` `python3-config --ldflags`
# gcc main.c -o main -I./include  -L . -l mybridge
# set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")
#FIND_PACKAGE(mybridge)
# AUX_SOURCE_DIRECTORY(. DIR_SRCS)
# ADD_EXECUTABLE(main ${DIR_SRCS})

PROJECT(main)
CMAKE_MINIMUM_REQUIRED(VERSION 3.4.1)
INCLUDE_DIRECTORIES(./include)
LINK_DIRECTORIES(.)
ADD_EXECUTABLE(main main.c)
TARGET_LINK_LIBRARIES(main mybridge)

