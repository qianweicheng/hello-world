const rust = import('mywebassembly');

rust
  .then(m => m.greet('World!'))
  .catch(console.error);


function t1() {
    console.log("t1");
}

function t2() {
    
}

export default { t1, t2}