#!/usr/bin/env bash
set -e

SCRIPT_DIR=$(dirname $0)
cd $SCRIPT_DIR
PROJECT_ROOT=$(pwd)
echo "Workspace:${PROJECT_ROOT}"


usage() {
  cat <<EOF
Usage :
  -h                            Display this message
  -c                            run docker with custom command
  -d                            run docker with bash
  -g                            use gcc to build a executable file
  -1                            run in cli mode（hello）
  -2                            run in cli mode (network)
  -3                            run in cli mode (socket-client)
EOF
}

function run_docker_bash() {
    docker run --rm -it \
    -v $(pwd):/src \
    -u $(id -u):$(id -g) \
    emscripten/emsdk \
    bash
}

function run_docker_custom_command() {
    docker run --rm -it \
    -v $(pwd):/src \
    -u $(id -u):$(id -g) \
    emscripten/emsdk \
    emcc -O1 \
    --js-library src/library.js \
    -s WASM=1 \
    -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap", "ccall"]' \
    src/hello.c \
    -o dist/hello.js
}

unset mode
while getopts :hcdg123 OPTION; do
  case $OPTION in
  c)
    mode="run_docker_custom_command"
    ;;
  d)
    mode="run_docker_bash"
    ;;
  g)
    mode="gcc"
    ;;
  1)
    mode="1"
    ;;
  2)
    mode="2"
    ;;
  3)
    mode="3"
    ;;
  h)
    mode="help"
    ;;
  *) ;;
  esac
done

if [ "$mode" = "run_docker_custom_command" ]; then
  run_docker_custom_command
elif [ "$mode" = "run_docker_bash" ]; then
  run_docker_bash
elif [ "$mode" = "gcc" ]; then
  gcc src/socket_client.c -o socket_client
elif [ "$mode" = "1" ]; then
  emcc -O1 \
    -s WASM=1 \
    -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap", "ccall"]' \
    src/hello.c \
    --js-library src/library.js \
    -g4 --source-map-base "http://localhost:8080/dist/" \
    -o dist/hello.js
elif [ "$mode" = "2" ]; then
  emcc -O1 \
    -s WASM=1 \
    -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap", "ccall"]' \
    src/tcp_echo_client.cpp \
    -o dist/tcp_echo_client.js
       # src/test_sockets_echo_client.c \
    # -o dist/test_sockets_echo_client.js
elif [ "$mode" = "3" ]; then
  emcc -O1 \
    -s WASM=1 \
    -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap", "ccall"]' \
    -s ASSERTIONS=1 \
    -s NO_EXIT_RUNTIME=1 \
    -s WEBSOCKET_URL="ws://localhost:8088" \
    -s PROXY_POSIX_SOCKETS=1 \
    -lwebsocket.js \
    -s USE_PTHREADS=1 \
    -s PROXY_TO_PTHREAD=1 \
    -s FORCE_FILESYSTEM=1 \
    -s LLD_REPORT_UNDEFINED \
    -g4 --source-map-base "http://localhost:8080/dist/" \
    src/socket_client.c \
    -o dist/socket_client.js
else
  usage
fi