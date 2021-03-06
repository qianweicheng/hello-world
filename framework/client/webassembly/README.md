# WebAssembly
## Document
https://webassembly.org/
Rust 开发在开发效率和便捷性、包体积大小等方面还是有很大优势的
## WebAssembly Binary Toolkit
https://github.com/WebAssembly/wabt
## Rust
- 官方文档：`https://rustwasm.github.io/docs.html`
  - 入门文档: `https://rustwasm.github.io/docs/book/` or `https://github.com/rustwasm/book`
  - wasm-bindgen文档: `https://rustwasm.github.io/docs/wasm-bindgen/`
  - wasm-pack文档: `https://rustwasm.github.io/docs/wasm-pack/introduction.html`
- 名词解释
  - `wasm-pack` is your one-stop shop for building, testing, and publishing Rust-generated WebAssembly.
  - `wasm-bindgen` is a tool that facilitates interoperability between wasm modules and JavaScript.
### Install
1. wasm-pack: `cargo install wasm-pack` or `https://rustwasm.github.io/wasm-pack/installer/`
   1. `wasm-pack new myproject`
2. 使用模版: `cargo install cargo-generate`
   1. `cargo generate --git https://github.com/rustwasm/wasm-pack-template`
### Build
`wasm-pack build --target web`
### 模块管理
cargo
在线仓库: https://docs.rs/

## C/C++
https://emscripten.org/
https://hub.docker.com/r/emscripten/emsdk
### Install
```
git clone https://github.com/emscripten-core/emsdk.git

cd emsdk

# Download and install the latest SDK tools.
./emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh
```

### 宏定义
- EM_PORT_API：EM_PORT_API(double) = extern "C" EMSCRIPTEN_KEEPALIVE double xxx()
- __EMSCRIPTEN__宏用于探测是否是Emscripten环境
- __cplusplus用于探测是否C++环境
- EMSCRIPTEN_KEEPALIVE是Emscripten特有的宏，用于告知编译器后续函数在优化时必须保留，并且该函数将被导出至JavaScript
- EM_JS/EM_ASM宏内联JavaScript代码
- emscripten_run_script/emscripten_run_script_string/emscripten_run_script_int
- `-s NO_EXIT_RUNTIME=0`
- `-s FORCE_FILESYSTEM=1`