fn main() {
    let mut a = vec![1, 2, 3, 4];
    a.drain(0..2);
    println!("hello world: {:?}", a);
}