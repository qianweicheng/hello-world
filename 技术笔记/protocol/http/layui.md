#### http://www.layui.com/doc/
1. layui使用三次控制table
<div class="layui-container">  
    常规布局（以中型屏幕桌面为例）：
    <div class="layui-row">
        <div class="layui-col-md9">
        你的内容 9/12
        </div>
        <div class="layui-col-md3">
        你的内容 3/12
        </div>
    </div>
</div>

3. 列间距
layui-col-space1	列之间间隔 1px
layui-col-space3	列之间间隔 3px
layui-col-space5	列之间间隔 5px
layui-col-space8	列之间间隔 8px

4. 动画class="layui-anim layui-anim-up"
5. 控件
lay-ignore 使用系统
<button class="layui-btn">一个标准的按钮</button>
原始	class="layui-btn layui-btn-primary"
默认	class="layui-btn"
百搭	class="layui-btn layui-btn-normal"
暖色	class="layui-btn layui-btn-warm"
警告	class="layui-btn layui-btn-danger"
禁用	class="layui-btn layui-btn-disabled"

<input type="text" name="title" required lay-verify="required" placeholder="请输入标题" autocomplete="off" class="layui-input">
required：注册浏览器所规定的必填字段 
lay-verify：注册form模块需要验证的类型 
class="layui-input"：layui.css提供的通用CSS类 

<select name="city" lay-verify="">
  <option value="010">北京</option>
  <option value="021" disabled>上海（禁用效果）</option>
  <option value="0571" selected>杭州</option>
</select>     

默认风格：
<input type="checkbox" name="" title="写作" checked>
<input type="checkbox" name="" title="发呆"> 
<input type="checkbox" name="" title="禁用" disabled> 
 
原始风格：
<input type="checkbox" name="" title="写作" lay-skin="primary" checked>
<input type="checkbox" name="" title="发呆" lay-skin="primary"> 
<input type="checkbox" name="" title="禁用" lay-skin="primary" disabled> 
<input type="checkbox" name="xxx" lay-skin="switch">
<input type="checkbox" name="yyy" lay-skin="switch" lay-text="ON|OFF" checked>
<input type="checkbox" name="zzz" lay-skin="switch" lay-text="开启|关闭">
<input type="checkbox" name="aaa" lay-skin="switch" disabled>

<input type="radio" name="sex" value="nan" title="男">
<input type="radio" name="sex" value="nv" title="女" checked>
<input type="radio" name="sex" value="" title="中性" disabled>

<textarea name="" required lay-verify="required" placeholder="请输入" class="layui-textarea"></textarea>


<form class="layui-form layui-form-pane" action="">
  内部结构都一样，值得注意的是 复选框/开关/单选框 这些组合在该风格下需要额外添加 pane属性（否则会看起来比较别扭），如：
    <div class="layui-form-item" pane>
        <label class="layui-form-label">单选框</label>
        <div class="layui-input-block">
        <input type="radio" name="sex" value="男" title="男">
        <input type="radio" name="sex" value="女" title="女" checked>
        </div>
    </div>
   <div class="layui-form-item">
    <label class="layui-form-label">短输入框</label>
    <div class="layui-input-inline">
      <input type="text" name="username" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input">
    </div>
  </div>
</form>

6. CSS
layui-main	用于设置一个宽度为 1140px 的水平居中块（无响应式）
layui-inline	用于将标签设为内联块状元素
layui-box	用于排除一些UI框架（如Bootstrap）强制将全部元素设为box-sizing: border-box所引发的尺寸偏差
layui-clear	用于消除浮动（一般不怎么常用，因为layui几乎没用到浮动）
layui-btn-container	用于定义按钮的父容器。（layui 2.2.5 新增）
layui-btn-fluid	用于定义流体按钮。即宽度最大化适应。（layui 2.2.5 新增）
layui-icon	用于图标
layui-elip	用于单行文本溢出省略
layui-unselect	用于屏蔽选中
layui-disabled	用于设置元素不可点击状态
layui-circle	用于设置元素为圆形
layui-show	用于显示块状元素
layui-hide	用于隐藏元素
赤色：class="layui-bg-red"
橙色：class="layui-bg-orange"
墨绿：class="layui-bg-green"
藏青：class="layui-bg-cyan"
蓝色：class="layui-bg-blue"
雅黑：class="layui-bg-black"