mod second;
use second::ClassName;
mod front_of_house;
use front_of_house::demo1;
use front_of_house::demo2;

extern crate demo;

fn main() {
    demo::eat_at_restaurant();
    demo1::say_hi();
    demo2::say_hi2();

    let mut vector = vec![1, 2, 3, 4];
    vector.push(5);
    println!("{:?}", vector);
    println!("Hello, world!");

    let object = ClassName::new(1024);
    object.public_method();
}
