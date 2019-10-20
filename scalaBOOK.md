# 第一种helloworld
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

* 它在一个名叫hello的objec中定义了一个main函数
* object和class是类似的，但你要使用类时，你得特定地使用一个class的实列
* main接受一个字符串数组 args 
* Array是一个Java原始array的封装数组。

上面的scala代码十分像下面的java代码

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, world")
    }
}
```
scala 运行在jvm上，并且可以使用已经存在的java库。

# helloword的另一个版本

scala提供了一个更加方便的方式，不用写main函数，只需要继承APP trait，就像下面的：
```scala
object Hello2 extends App {
    println("Hello, world")
}
```
用**scalac**和**scala**后，这个运行结果和之前是一样的。

因App trait有它自己main方法，所以你不需要去再写一个，稍后我们将展示如何使用这种方法访问命令行参数，但简单的是:它们在名为args的字符串数组中可用。

> 我之前并没有提到trait，它很像是java中抽象类和接口的结合

```scala
object HelloYou extends App {
    if (args.size == 0)
        println("Hello, you")
    else
        println("Hello, " + args(0))
}
```

输出：
```linux
$ scala HelloYou
Hello, you

$ scala HelloYou Al
Hello, Al
```

这表明：
* 命令行参数（args）是自动创建的，
* 你判定args的元素个数用args.size(或者是args.length,如果你喜欢的话)
* **args**是一个数组，并且args是一个对象，所以你访问其元素使用圆括号。args（0），args（1）


# the scala REPL

REPL(Read-Evaluate-Print-Loop)其实就是终端交互，通过命令行输入实现.

只需在操作系统输入scala
```
$ scala
Welcome to Scala 2.13.0 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_131).
Type in expressions for evaluation. Or try :help.

scala> _
```
它每个表达式后面都会跟着结果。
```
scala> val x = 1
x: Int = 1

scala> val y = x + 1
y: Int = 2
```
如果你没有指明表达接受结果的变量，REPL就会自动创建以res开头的变量，第一个是res0，第二个是res1,etc...
```scala
scala> 2 + 2
res0: Int = 4

scala> 3 / 3
res1: Int = 1
```
你可以使用这些自动创建的变量
```scala
scala> val z = res0 + res1
z: Int = 5
```

For more information on the Scala REPL, see the [Scala REPL overview](https://docs.scala-lang.org/overviews/repl/overview.html)

# 两种类型的变量

Scala用两种类型的变量：

* val 不可变变量（类似java final）
* var 可变变量

```
val s = "hello"   // immutable
var i = 42        // mutable

val p = new Person("Joel Fleischman")
```

## val和var的不同：
```
scala> val a = 'a'
a: Char = a

scala> a = 'b'
<console>:12: error: reassignment to val
       a = 'b'
         ^
scala> var a = 'a'
a: Char = a

scala> a = 'b'
a: Char = b
```

scala一般都用val，因为这个规则使你的代买更像代数，并且帮助你开始函数式编程的道路，因为函数式编程的所有字段都是不可变的。

REPL不是完全和IDE中的代码一样得，有些事情你可以在REPL中做，但是在真实的环境中就不行。比如：你可以在REPL中重新定义字段val。

```
scala> val age = 18
age: Int = 18

scala> val age = 19
age: Int = 19
```


# 显式指明类型

编译器可以自动分辨等号右边的类型，你也可以直接指明变量的类型

```
val s: String = "hello"
var i: Int = 42
```
在大多数情况下，你不写类型使你的代码跟容易阅读。
```scala
// For instance, in this example it’s obvious that the data type is Person, so there’s no need to declare the type on the left side of the expression:

val p = new Person("Candy")
// By contrast, when you put the type next to the variable name, the code feels unnecessarily verbose:

val p: Person = new Person("Leo")
// In summary:

val p = new Person("Candy")           // preferred
val p: Person = new Person("Candy")   // unnecessarily verbose
```

在一些特定的情况下，你最好指定类型，比如使用第三方库。有些时候编译器也会错误的假定你的变量类型，这时候你必须显式地指明类型。

# scala的内建类型

注意，Scala的数据类型都是对象，不是基本数据类型。
```
val b: Byte = 1
val x: Int = 1
val l: Long = 1
val s: Short = 1
val d: Double = 2.0
val f: Float = 3.0
```
Int和Double是默认的数字类型。若你想使用Long，Short等，你就要显式的指明。

## 数据类型以及他们的范围：


Data Type | Possible Values| 
---------|-------|
Boolean	|true or false|
Byte|	8-bit signed two’s complement integer (-2^7 to 2^7-1, inclusive)-128 to 127|
Short|	16-bit signed two’s complement integer (-2^15 to 2^15-1, inclusive)32,768 to 32,767|
Int	|32-bit two’s complement integer (-2^31 to 2^31-1, inclusive)2,147,483,648 to 2,147,483,647 |
Long|	64-bit two’s complement integer (-2^63 to 2^63-1, inclusive)(-2^63 to 2^63-1, inclusive)|
Float|32-bit IEEE 754 single-precision float 1.40129846432481707e-45 to 3.40282346638528860e+38|
Double|	64-bit IEEE 754 double-precision float4.94065645841246544e-324d to 1.79769313486231570e+308d|
Char|	16-bit unsigned Unicode character (0 to 2^16-1, inclusive)0 to 65,535|
String|	a sequence of Char|

## 大数：BigInt and BigDecimal

```
var b = BigInt(1234567890)
var b = BigDecimal(123456.789)
```
BigInt 、 BigDecimal 支持数据类型的操作
```
scala> var b = BigInt(1234567890)
b: scala.math.BigInt = 1234567890

scala> b + b
res0: scala.math.BigInt = 2469135780

scala> b * b
res1: scala.math.BigInt = 1524157875019052100

scala> b += 1

scala> println(b)
1234567891
```
## String and Char
隐式声明
```
val name = "Bill"
val c = 'a'
```
也可以显式声明
```
val name: String = "Bill"
val c: Char = 'a'
```


# String

String有很多美妙的特性，但是我们想花一点时间突出介绍两个重要的特性。

1. 字符串内插特性（ 原文：string interpolation）

```scala
val firstName = "John"
val mi = 'C'
val lastName = "Doe"

//you can append them together like this, if you want to:

val name = firstName + " " + mi + " " + lastName
//However, Scala provides this more convenient form:

val name = s"$firstName $mi $lastName"
//This form creates a very readable way to print strings that contain variables:

println(s"Name: $firstName $mi $lastName")
```
就如展示的那样，所有你要做的就是在字符串前加上一个字母“s”，然后在你的变量名前边添加一个“$"记号。“s”启用string interpolation，“$”指明内插的内容。

scala对string interpolation还有很多特性，比如你可用花括号包围你的变量名。
```scala
println(s"Name: ${firstName} ${mi} ${lastName}")
```
这确实你帮助阅读代码，但是它更加重要的意义在于你可以在花括号里放表达式，下面的REPL例子：

```linux
scala> println(s"1+1 = ${1+1}")
1+1 = 2
```
关于 string interpolation 还有其他特性：
* 你可以在字符串前面加上“f”，这可以让你能以printf风格插入字符串。
* 原始插值器（原文 interpolator）不会对字符串中的文字(比如\n)执行转义
* 你可以创建你自己的字符串插值器

See the [string interpolation documentation](https://docs.scala-lang.org/overviews/core/string-interpolation.html) for more details.

2. 多行字符串特性

你可以用三重引号创建一个多行字符串。

```scala
val speech = """Four score and
               seven years ago
               our fathers ..."""
```
这个方法有个缺点就是第一行后面的行都是缩进的，可以在下面REPL例子中看到：
```scala
scala> val speech = """Four score and
     |                seven years ago
     |                our fathers ..."""
speech: String =
Four score and
                   seven years ago
                   our fathers ...
```
上面的输出错开了，显然不是我们想要的。以简单的方式就是在每一行的开头加入标价字符“|”，然后调用 **stripMargin** 方法。REPL下换行自动标识的“|”不算数。
```scala
scala> val speech = """Four score and
     |                |seven years ago
     |                |our fathers ...""".stripMargin
speech: String =
Four score and
seven years ago
our fathers ...
```

# 命令行I/O

## 输出
```scala
//As we’ve already shown, you write output to standard out (STDOUT) using println:

println("Hello, world")
//That function adds a newline character after your string, so if you don’t want that, just use print instead:

print("Hello without newline")
//When needed, you can also write output to standard error (STDERR) like this:

System.err.println("yikes, an error happened")
```
>Because println is so commonly used, there’s no need to import it. The same is true of other commonly-used data types like String, Int, Float, etc.
## 输入

输入的最简单方式就是使用 **readline** 函数。
你首先要import：
```scala
import scala.io.StdIn.readLine
```
下面示范怎么用它：
```scala
import scala.io.StdIn.readLine

object HelloInteractive extends App {

    print("Enter your first name: ")
    val firstName = readLine()

    print("Enter your last name: ")
    val lastName = readLine()

    println(s"Your name is $firstName $lastName")

}
```

输出：
```
$ scala HelloInteractive
Enter your first name: Alvin
Enter your last name: Alexander
Your name is Alvin Alexander
```

# 流程控制

## if

一个基本的scala if：
```scala
if (a==b)  doSomething()
```
也可以加上花括号：
```scala
if(a==b){
    doSomething()

}
```

if /else 结构：
```scala
if (a == b) {
    doSomething()
} else {
    doSomethingElse()
}
```

if/else-if/else结构：
```scala
if (test1) {
    doX()
} else if (test2) {
    doY()
} else {
    doZ()
}
```
从上面的说明可以看出scala的if和java除了分号外，基本可以写成一样的。

但是还是有区别的：scala中if表达式总是返回一个结果。
```scala
val minValue = if (a < b) a else b
```
基于此，scala不要求特定的三元操作。
返回返回值的行称为表达式，而不返回返回值的行称为语句。函数式编程中，总是要求返回表达式。

## for
scala的for循环能用来迭代集合中的元素。
```scala
scala> val nums = Seq(1,2,3)
nums: Seq[Int] = List(1, 2, 3)

scala> for (n <- nums) println(n)
1
2
3

```
>Seq and List 是两种线性集合，在Scala这些集合的优先级高于Array。

为了遍历集合中的元素，你可以用集合带有的foreach函数。
```scala
people.foreach(println)//这充分说明了,在函数式编程里,函数是可以作为参数的
```

绝大多数的集合类都有foreach的实现。
### 对map使用for和foreach

```scala
val ratings = Map(
    "Lady in the Water"  -> 3.0, 
    "Snakes on a Plane"  -> 4.0, 
    "You, Me and Dupree" -> 3.5
)


for ((name,rating) <- ratings) println(s"Movie: $name, Rating: $rating")

ratings.foreach {
    case(movie, rating) => println(s"key: $movie, value: $rating")
}//明显是匿名函数的写法
```


TODO 翻译进度https://docs.scala-lang.org/overviews/scala-book/for-expressions.html
