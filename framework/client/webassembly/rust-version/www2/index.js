const rust = import('mywebassembly');

rust
  .then(function(m){
      m.greet('World!')
      let s = m.strings()
      for(let item in s) {
          console.log(s[item]);
      }
      m.greet2()
    })
  .catch(console.error);