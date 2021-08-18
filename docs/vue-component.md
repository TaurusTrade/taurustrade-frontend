# 定义组件

Vue组件的API主要包含三部分：prop、event、slot

- props  表示组件接收的参数，最好用对象的写法，这样可以针对每个属性设置类型、默认值或自定义校验属性的值，此外还可以通过type、validator等方式对输入进行验证

  + 单向数据流 
    
    父级 prop 的更新会向下流动到子组件中，但是反过来则不行

    单向数据流是Vue组件一个非常明显的特征，不应该在子组件中直接修改props的值

    + 如果传递的prop仅仅用作展示，不涉及修改，则在模板中直接使用即可
    + 如果需要对prop的值进行转化然后展示，则应该使用computed计算属性
    + 如果prop的值用作初始化，应该定义一个子组件的data属性并将prop作为其初始值


    在子组件修改props，却不会修改父组件，这是因为extractPropsFromVNodeData中是通过浅复制将attrs传递给props的。
    
    浅复制意味着在子组件中对对象和数组的props进行修改还是会影响父组件，这就违背了单向数据流的设计。因此需要避免这种情况出现。


组件之间的通信
这里可以参考:[vue组件通信全揭秘](https://juejin.cn/post/6844903702411608072)，写的比较全面

父子组件的关系可以总结为 

  + **prop 向下传递** 
  + **事件event向上传递**
  
祖先组件和后代组件（跨多代）的数据传递，可以使用provide和inject来实现

此外，如果需要跨组件或者兄弟组件之间的通信，可以通过eventBus或者vuex等方式来实现。



  

- slot   可以给组件动态插入一些内容或组件，是实现高阶组件的重要途径；当需要多个插槽时，可以使用具名slot
- event  是子组件向父组件传递消息的重要途径



# 引入组件

## 全局引入

```
import Vue from "vue"
import somePlugin from "../src/somePlugin"

Vue.use(somePlugin)
```