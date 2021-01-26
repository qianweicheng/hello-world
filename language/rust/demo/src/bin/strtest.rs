fn main() {
    let a = "abc";
    let b = String::from("abc");
    let c = &a[..];
    println!("{} {} {}", a, b, c);
}
