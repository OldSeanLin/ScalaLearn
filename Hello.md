## 第一种helloworld
```scala
object Hello {
    def main(args: Array[String]) = {
        println("Hello, world")
    }
}
```
使用文本编辑器保存上面的代码，保存文件为Hello.scala，然后运行命令 **scalac** 以编译。
```
$ scalac Hello.scala
```
**scalac** is just like **javac**, and that command creates two new files:

* Hello$.class
* Hello.class

他们是和javac创建的是同一种类的二进制文件，都可以放在JVM上运行

```
$ scala Hello
```

#### 讨论

```scala
object Hello {
    def main(args: Array[String]) = {
        println("Hello, world")
    }
}
```

简短的描述：

*







