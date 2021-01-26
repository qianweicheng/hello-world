extern crate demo;
use demo::front_of_house::demo1::say_hi;

fn main() {
    demo::eat_at_restaurant();
    say_hi();
    let mut vector = vec![1, 2, 3, 4];
    vector.push(5);
    println!("{:?}", vector);
    println!("Hello, world!");
}
