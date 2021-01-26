mod utils;
use wasm_bindgen::prelude::*;
use js_sys::Array;
extern crate web_sys;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
    fn fun_js(s: &str);

    // Use `js_namespace` here to bind `console.log(..)` instead of just
    // `log(..)`
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);

    // The `console.log` is quite polymorphic, so we can bind it with multiple
    // signatures. Note that we need to use `js_name` to ensure we always call
    // `log` in JS.
    #[wasm_bindgen(js_namespace = console, js_name = log)]
    fn log_u32(a: u32);

    // Multiple arguments too!
    #[wasm_bindgen(js_namespace = console, js_name = log)]
    fn log_many(a: &str, b: &str);
}

#[wasm_bindgen]
pub fn greet() {
    alert("Hello, myproject!");
    fun_js("Hello, js!");
    greet1("weicheng");
    // greet2();
}

#[wasm_bindgen]
pub fn greet1(name: &str) {
    log("Hello from Rust!");
    log_u32(42);
    log_many("Logging", name);
}

#[wasm_bindgen]
pub fn strings() -> Array {
    let arr = Array::new_with_length(10);
    for i in 0..arr.length() {
        let s = JsValue::from_str(&format!("str {}", i));
        arr.set(i, s);
    }
    arr
}
 
#[wasm_bindgen]
pub fn greet2() -> Result<(), JsValue> {
    // Use `web_sys`'s global `window` function to get a handle on the global
    // window object.
    let window = web_sys::window().expect("should have a window in this context");
    let document = window.document().expect("should have a document on window");
    let body = document.body().expect("document should have a body");

    // Manufacture the element we're gonna append
    let val = document.create_element("p")?;
    val.set_inner_html("Hello from Rust!");

    body.append_child(&val)?;

    Ok(())
}