# VUE
vue: https://cn.vuejs.org/index.html
vuex: https://vuex.vuejs.org/zh/
vue-router: https://router.vuejs.org/
vue-cli: https://cli.vuejs.org/zh/config/
## Framework
nuxt
## Vue
#### 选项
- el：挂载root元素
- data：可以是一个对象，也可以是一个函数
- computed：计算属性
- watch
- methods：用于存储各种方法
- components： 注册组件
#### 生命周期
- beforeCreate
- created
- beforeMount
- mounted
- beforeUpdate
- updated
- beforeDestory
- destoryed
## 模版
- 双大括号会将数据解释为普通文本，而非 HTML 代码。为了输出真正的 HTML，你需要使用 v-html 指令
- 双大括号: JavaScript 
## 指令
- v-bind:[attr]='value', 缩写`:attr`: 表示attr与value绑定 
- v-on (@缩写)
    `<form v-on:submit.prevent="onSubmit">...</form>`
- v-if
- v-for
  `(item, index) in items` or `item in items` 
  排序：`:key="item.id"`
  自定监控如下方法
    push()
    pop()
    shift()
    unshift()
    splice()
    sort()
    reverse()
## 组件
#### 选项
- data：一个组件的data选项通常是一个函数, 每个实例可以维护一份被返回对象的独立的拷贝，否则不同组件公用一个状态
- 属性(props)不可变: 所有的 prop 都使得其父子 prop 之间形成了一个单向下行绑定，
     数组形式:["a","b"]
     字典格式:
     ```
        {
            "title":String,
            "count":{
                type: Number,
                required: true,
                default: 100                
            },
            "prop1:{
                type: String,
                required: true
                default: function () {
                    return { message: 'hello' }
                },
                validator: function (value) {
                    return ['success', 'warning', 'danger'].indexOf(value) !== -1
                }
            }
        }
     ```
- 计算属性(computed)
    计算属性是基于它们的响应式依赖进行缓存的。只在相关响应式依赖发生改变时它们才会重新求值
- 侦听属性(watch),慎用
- methods
- template
- 自定义事件:
  大小写敏感
  <my-component v-on:myevent="doSomething"></my-component>
  this.$emit('myevent')
  - 将原生事件绑定到组件: `<base-input v-on:focus.native="onFocus"></base-input>
`
#### 定义
- method 1
``` 
Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
```
- method 2:Single file component
``` xxx.vue
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>
<script>
export default {
    name:"button-counter"
    props: {
        msg: String
    }
}
// or 
export default Vue.component('question', {
    props: {
        msg: String
    }
})
</script>
<style scoped>
</style>
```
- method 3
```
<template src="./template.html"></template>
<style src="./style.css"></style>
<script src="./script.js"></script>
```
#### 组件注册
- 全局注册
    ```
        Vue.component('my-component-name', {
        // ... 选项 ...
        })
    ```
- 局部注册
    ```
        new Vue({
        el: '#app',
        components: {
            'component-a': ComponentA,
            'component-b': ComponentB
        }
        })
    ```
- 基础组件的自动化全局注册
```
const requireComponent = require.context(
  // 其组件目录的相对路径
  './components',
  // 是否查询其子目录
  false,
  // 匹配基础组件文件名的正则表达式
  /Base[A-Z]\w+\.(vue|js)$/
)
```
## 路由
- 简单路由
```
const NotFound = { template: '<p>Page not found</p>' }
const Home = { template: '<p>home page</p>' }
const About = { template: '<p>about page</p>' }

const routes = {
  '/': Home,
  '/about': About
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})
```
- vue-routers
https://router.vuejs.org/
    1. VueRouter 添加到Vue中
    2. 配置路由
    3. router-view
容易遇到的错:
    1. 拼写错误
    2. xxx.vue只有模版，没有export default
## 状态管理
- simple store
简单应用自己实现一个store
```
var store = {
  debug: true,
  state: {
    message: 'Hello!'
  },
  setMessageAction (newValue) {
    if (this.debug) console.log('setMessageAction triggered with', newValue)
    this.state.message = newValue
  },
  clearMessageAction () {
    if (this.debug) console.log('clearMessageAction triggered')
    this.state.message = ''
  }
}

var vmA = new Vue({
  data: {
    privateState: {},
    sharedState: store.state
  }
})

var vmB = new Vue({
  data: {
    privateState: {},
    sharedState: store.state
  }
})
```
使用(必须通过方法)：
```
this.sharedState.setMessageAction()
this.sharedState.getMessageAction()
```
- vuex
  - 更改 Vuex 的 store 中的状态的唯一方法是提交 mutation: `store.commit('increment')`
  - Action 提交的是 mutation，而不是直接变更状态。Action 可以包含任意异步操作。

## 帮助
- 查看编译配置: `vue inspect`
- chainWebpack vs configWebpack
  chainWebpack会覆盖configWebpack的内容, 一般配置一些chainWebpack里面没有的东西

