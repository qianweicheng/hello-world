message(STATUS "now using Findmybridge.cmake find mybridge lib")
# SET(MYBRIDGE_FOUND TRUE)
# FIND_PATH(MYBRIDGE_INCLUDE_DIRS PATHS /Users/qianweicheng/git-x/hello-world/language/cmake/c2ptest)
FIND_LIBRARY(MYBRIDGE_LIBRARIES NAME mybridge PATHS /Users/qianweicheng/git-x/hello-world/language/cmake/c2ptest)
