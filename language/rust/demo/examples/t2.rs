use std::cell::Cell;
struct Person {
  name: String,
  age: usize,
  count: Cell<usize>, // 一共有多少个副本，包含自身
}

impl Clone for Person {
    fn clone(&self) -> Self {
      let new_count = self.count.get() + 1;
      self.count.set(new_count);  // ok
      Person {
        name: self.name.clone(),
        age: self.age,
        count: Cell::new(new_count),
      }
    }
}

fn main() {
  let person = Person { name: "zengsai".to_string(), age: 18, count: Cell::new(1) };
  //    ^         ^
  //    |         |
  // 所有者     对象或值
  
  println!("Person count : {}", person.count.get());  // OUTPUT: Person count : 1
  
  let person_cloned_1: Person = person.clone();

  println!("Person count : {}", person.count.get());  // OUTPUT: Person count : 2
  
  let person_cloned_2: Person = &person;
 
  println!("Person count : {}", person.count.get());  // OUTPUT: Person count : 3
}