// 两种方式都可以
// 但不能有export default function
// export function add(a, b) {
//   console.log("a+b=" + (a + b));
// }

// export function add2(a, b) {
//   console.log("!--->a+b=" + (a + b));
// }

module.exports.add = function(a,b) {
  console.log("add");
};

module.exports.add2 = function (a, b) {
  console.log("add2");
};

[1, 2, 3].map((n) => n + 1);

const getMessage = ()=> {
console.log("hello world.")
};
getMessage();