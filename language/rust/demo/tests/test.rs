
#[test]
#[cfg(feature="bar")]
fn c1() {
    assert_eq!(1,1);
}

#[test]
#[cfg(feature="foo")]
fn c2() {
    assert_eq!(1,1);
}

// #[test]
// #[cfg(feature="c3")]
// fn c3() {
//     assert_eq!(1,1);
// }
