# Java自带三个注解
@Override，表示当前的方法定义将覆盖超类中的方法。
@Deprecated，使用了注解为它的元素编译器将发出警告，因为注解@Deprecated是不赞成使用的代码，被弃用的代码。
@SuppressWarnings，关闭不当编译器警告信息。
# 自定义注解的注解
@Target
@Retention：表示需要在什么级别保存该注解信息。
@Document：将注解包含在Javadoc中
@Inherited：允许子类继承父类中的注解
# 自定义注解
@Target(FIELD)
@Retention(RUNTIME)
@Documented
public @interface EdoTODO{
    public enum Color{ BLUE,RED,GREEN};
    String value() default "";
    Color fruitColor() default Color.GREEN;
}

