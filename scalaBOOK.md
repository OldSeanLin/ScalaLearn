
翻译者：林雨村

时间：2019-10-15至

log

# 目录

<!-- TOC -->

- [目录](#目录)
- [1. helloworld](#1-helloworld)
            - [1.1. 讨论](#11-讨论)
- [2. helloword的另一个版本](#2-helloword的另一个版本)
- [3. the scala REPL](#3-the-scala-repl)
- [4. 两种类型的变量](#4-两种类型的变量)
    - [4.1. val和var的不同：](#41-val和var的不同)
- [5. 显式指明类型](#5-显式指明类型)
- [6. scala的内建类型](#6-scala的内建类型)
    - [6.1. 数据类型以及他们的范围：](#61-数据类型以及他们的范围)
    - [6.2. 大数：BigInt and BigDecimal](#62-大数bigint-and-bigdecimal)
    - [6.3. String and Char](#63-string-and-char)
- [7. String](#7-string)
- [8. 命令行I/O](#8-命令行io)
    - [8.1. 输出](#81-输出)
    - [8.2. 输入](#82-输入)
- [9. 流程控制](#9-流程控制)
    - [9.1. if](#91-if)
    - [9.2. for](#92-for)
        - [9.2.1. 对map使用for和foreach](#921-对map使用for和foreach)
    - [9.3. match表达式](#93-match表达式)
    - [try/catch/finally expression](#trycatchfinally-expression)
- [Classes](#classes)
    - [基础类的构造器](#基础类的构造器)
    - [val使得字段只读](#val使得字段只读)
    - [类的构造器](#类的构造器)

<!-- /TOC -->

# 1. helloworld

[↑↑](#目录)


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

#### 1.1. 讨论

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

# 2. helloword的另一个版本

[↑↑](#目录)

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


# 3. the scala REPL

[↑↑](#目录)

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

# 4. 两种类型的变量

[↑↑](#目录)

Scala用两种类型的变量：

* val 不可变变量（类似java final）
* var 可变变量

```
val s = "hello"   // immutable
var i = 42        // mutable

val p = new Person("Joel Fleischman")
```

## 4.1. val和var的不同：

[↑↑](#目录)

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


# 5. 显式指明类型

[↑↑](#目录)

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

# 6. scala的内建类型

[↑↑](#目录)


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

## 6.1. 数据类型以及他们的范围：


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

## 6.2. 大数：BigInt and BigDecimal

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

## 6.3. String and Char
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


# 7. String

[↑↑](#目录)

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

# 8. 命令行I/O

[↑↑](#目录)


## 8.1. 输出
```scala
//As we’ve already shown, you write output to standard out (STDOUT) using println:

println("Hello, world")
//That function adds a newline character after your string, so if you don’t want that, just use print instead:

print("Hello without newline")
//When needed, you can also write output to standard error (STDERR) like this:

System.err.println("yikes, an error happened")
```
>Because println is so commonly used, there’s no need to import it. The same is true of other commonly-used data types like String, Int, Float, etc.

## 8.2. 输入

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

# 9. 流程控制


[↑↑](#目录)


## 9.1. if

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

## 9.2. for
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

### 9.2.1. 对map使用for和foreach

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

scala中，for不仅仅一个for-loop，也可以是一个for-expression。它能从一个已经存在的集合中创造一个新的集合。
举个例子，给出一个整数的列表
```scala
val nums = Seq(1,2,3)
```
你可以创建新的所有值都二倍的列表
```scala
val doubledNums = for (n <- nums) yield n * 2
```
在REPL中的表现
```scala
scala> val doubledNums = for (n <- nums) yield n * 2
doubledNums: Seq[Int] = List(2, 4, 6)
```
> Using yield after for is the “secret sauce” that says, “I want to yield a new collection from the existing collection that I’m iterating over in the for-expression, using the algorithm shown.”

yield也是可以用花括号包围。
```scala
val capNames = for (name <- names) yield name.drop(1).capitalize

val capNames = for (name <- names) yield { name.drop(1).capitalize }
```

## 9.3. match表达式

scala中有match表达式的概念，在很多时候它很像java中的swtich语句。

```scala
// i is an integer
i match {
    case 1  => println("January")
    case 2  => println("February")
    case 3  => println("March")
    case 4  => println("April")
    case 5  => println("May")
    case 6  => println("June")
    case 7  => println("July")
    case 8  => println("August")
    case 9  => println("September")
    case 10 => println("October")
    case 11 => println("November")
    case 12 => println("December")
    // catch the default with a variable so you can print it
    case _  => println("Invalid month")//Any other value falls down to the _ case, which is the catch-all, default case.
}
```
match expression也能有返回值。
```scala
val monthName = i match {
    case 1  => "January"
    case 2  => "February"
    case 3  => "March"
    case 4  => "April"
    case 5  => "May"
    case 6  => "June"
    case 7  => "July"
    case 8  => "August"
    case 9  => "September"
    case 10 => "October"
    case 11 => "November"
    case 12 => "December"
    case _  => "Invalid month"
}
```
match也可以作为方法体。
```scala
def convertBooleanToStringMessage(bool: Boolean): String = bool match {
    case true => "you said true"
    case false => "you said false"
}

val result = convertBooleanToStringMessage(true)
println(result)
```
match也可以和if相结合，提供更强大的模式匹配，当然这个写法比较奇怪，你只需记住。
```scala
count match {
    case 1 => println("one, a lonely number")
    case x if (x == 2 || x == 3) => println("two's company, three's a crowd")
    case x if (x > 3) => println("4+, that's a party")
    case _ => println("i'm guessing your number is zero or less")
}

//另外的一些例子
count match {
    case 1 => {
        println("one, a lonely number")
    }
    case x if x == 2 || x == 3 => {
        println("two's company, three's a crowd")
    }
    case x if x > 3 => {
        println("4+, that's a party")
    }
    case _ => {
        println("i'm guessing your number is zero or less")
    }
}

count match {
    case 1 => 
        println("one, a lonely number")
    case x if x == 2 || x == 3 => 
        println("two's company, three's a crowd")
    case x if x > 3 => 
        println("4+, that's a party")
    case _ => 
        println("i'm guessing your number is zero or less")
}
```

如何匹配范围内的数字的例子
```scala
//十分口语化
i match {
  case a if 0 to 9 contains a => println("0-9 range: " + a)
  case b if 10 to 19 contains b => println("10-19 range: " + a)
  case c if 20 to 29 contains c => println("20-29 range: " + a)
  case _ => println("Hmmm...")
}

```
在if中使用类的字段也是可以的
```scala
stock match {
  case x if (x.symbol == "XYZ" && x.price < 20) => buy(x)
  case x if (x.symbol == "XYZ" && x.price > 50) => sell(x)
  case x => doNothing(x)
}
```
## try/catch/finally expression

[↑↑](#目录)


与Java一样，Scala也有try/catch/finally结构，允许您捕获和管理异常。主要区别在于，为了一致性，Scala使用与表达式match相同的语法:case语句来匹配可能出现的不同异常。


```scala

    // your scala code here
} 
catch {
    case foo: FooException => handleFooException(foo)
    case bar: BarException => handleBarException(bar)
    case _: Throwable => println("Got some other kind of Throwable exception")
} finally {
    // your scala code here, such as closing a database connection
    // or file handle
}
```
# Classes

[↑↑](#目录)

## 基础类的构造器

下面是类的构造器，它定义了两个参数，firstName and lastName

```scala

class Person(var firstName:String ,var lastName:String)

```

创建一个新的person实例：
```scala

val p= new Person("bill","panner")


```
由于定义的参数是**var**，所以你是可以修改它的。
```scala
scala> p.firstName = "William"
p.firstName: String = William

scala> p.lastName = "Bernheim"
p.lastName: String = Bernheim
```

粗略对应java的话就是：
```java
public class Person {

    private String firstName;
    private String lastName;
    
    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    public String getFirstName() {
        return this.firstName;
    }
    
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    
    public String getLastName() {
        return this.lastName;
    }
    
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    
}
```

## val使得字段只读

```scala
class Person(val firstName: String, val lastName: String)
```

```scala
scala> p.firstName = "Fred"
<console>:12: error: reassignment to val
       p.firstName = "Fred"
                   ^

scala> p.lastName = "Jones"
<console>:12: error: reassignment to val
       p.lastName = "Jones"
                  ^
```

> Tip:如果你想使用scala写OOP代码,就使用var定义字段以便更改.若你想写FP代码,你一般会用val.更多的下面介绍.

## 类的构造器

在scala里，基本的构造器可由以下组成：
* 构造器参数
* 调配类体中的函数
* 在类体中执行的语句或表达式

```scala
class Person(var firstName: String, var lastName: String) {

    println("the constructor begins")

    // 'public' access by default
    var age = 0

    // some class fields
    private val HOME = System.getProperty("user.home")

    // some methods
    override def toString(): String = s"$firstName $lastName is $age years old"

    def printHome(): Unit = println(s"HOME = $HOME")    
    def printFullName(): Unit = println(this) 

    printHome()
    printFullName()
    println("you've reached the end of the constructor")

}
```
```scala
scala> val p = new Person("Kim", "Carnes")
the constructor begins
HOME = /Users/al
Kim Carnes is 0 years old
you've reached the end of the constructor
p: Person = Kim Carnes is 0 years old

scala> p.age
res0: Int = 0

scala> p.age = 36
p.age: Int = 36

scala> p
res1: Person = Kim Carnes is 36 years old

scala> p.printHome
HOME = /Users/al

scala> p.printFullName
Kim Carnes is 36 years old
```
当你从其他verbose转过来，你会觉得这种写法有些奇怪，但是你多写几次就能理解其逻辑性以方便性。

在你离开此章之前，这里还有一些例子：
```
class Pizza (var crustSize: Int, var crustType: String)

// a stock, like AAPL or GOOG
class Stock(var symbol: String, var price: BigDecimal)

// a network socket
class Socket(val timeout: Int, val linger: Int) {
    override def toString = s"timeout: $timeout, linger: $linger"
}

class Address (
    var street1: String,
    var street2: String,
    var city: String, 
    var state: String
)
```

# 辅助类

辅助类（auxiliary Scala class），在我看来很像java中的重载构造函数。用this函数定义辅助类。

关于辅助类，你只需要知道两条规则：
* 每个辅助构造函数必须有不同的声明--不同的参数列表
* 每个构造函数必须调用之前的构造函数。

```scala
val DefaultCrustSize = 12
val DefaultCrustType = "THIN"

// the primary constructor
class Pizza (var crustSize: Int, var crustType: String) {

    // one-arg auxiliary constructor
    def this(crustSize: Int) {
        this(crustSize, DefaultCrustType)
    }

    // one-arg auxiliary constructor
    def this(crustType: String) {
        this(DefaultCrustSize, crustType)
    }

    // zero-arg auxiliary constructor
    def this() {
        this(DefaultCrustSize, DefaultCrustType)
    }

    override def toString = s"A $crustSize inch pizza with a $crustType crust"

}
```

```scala
val p1 = new Pizza(DefaultCrustSize, DefaultCrustType)
val p2 = new Pizza(DefaultCrustSize)
val p3 = new Pizza(DefaultCrustType)
val p4 = new Pizza
```

## NOTES
两条重要的说明：
* The DefaultCrustSize and DefaultCrustType variables are not a preferred way to handle this situation, but because we haven’t shown how to handle enumerations yet, we use this approach to keep things simple.
* Auxiliary class constructors are a great feature, but because you can use default values for constructor parameters, you won’t need to use this feature very often. The next lesson demonstrates how using default parameter values like this often makes auxiliary constructors unnecessary:

# 应用构造器默认参数
[↑↑](#目录)
先前我们展示定义Sockets
```scala
class Socket(var timeout: Int, var linger: Int) {
    override def toString = s"timeout: $timeout, linger: $linger"
}
```
接下来我使用默认参数定义
```
class Socket(var timeout: Int = 2000, var linger: Int = 3000) {
    override def toString = s"timeout: $timeout, linger: $linger"
}
```
通过定义默认参数，我们有如下new
```scala
new Socket()
new Socket(1000)
new Socket(4000, 6000)
```
```scala
scala> new Socket()
res0: Socket = timeout: 2000, linger: 3000

scala> new Socket(1000)
res1: Socket = timeout: 1000, linger: 3000

scala> new Socket(4000, 6000)
res2: Socket = timeout: 4000, linger: 6000
```
当然更具可读性的就是如下new
```scala
val s = new Socket(timeout=2000, linger=3000)
```

# 初识scala函数

## 定义一个带有一个输入的函数

定义一个方法，输入一个a参数，返回其两倍数
```
def double(a: Int) = a * 2
```

## 定义函数的返回类型

```scala

def double(a: Int): Int = a * 2

def add(a: Int, b: Int, c: Int): Int = a + b + c
```

## 多行函数
如果函数式单行的，你可像上面的模式书写函数。否则你需要花括号包裹作用域。

```scala
def addThenDouble(a: Int, b: Int): Int = {
    val sum = a + b
    val doubled = sum * 2
    doubled
}
```
上面的例子可以看出，最后一行的语句或者表达式就是返回的值。

# Enumerations（完整的pizza类）
Enumerations是一个十分有用的工具，用来创建一组实例。things like the days of the week, months in a year, suits in a deck of cards, etc.

我们有一点超前，因为没有解释语法。但是下面是创建week的
enumeration

```scala 
  sealed trait DayOfWeek
case object Sunday extends DayOfWeek
case object Monday extends DayOfWeek
case object Tuesday extends DayOfWeek
case object Wednesday extends DayOfWeek
case object Thursday extends DayOfWeek
case object Friday extends DayOfWeek
case object Saturday extends DayOfWeek
```

如同展示的那样，我们声明了一个基础的trait，然后被每一个需要的case object继承。

trait和case object在之后我们讨论。

下面我们创建pizza相关的enumerations
```scala 
 sealed trait Topping
case object Cheese extends Topping
case object Pepperoni extends Topping
case object Sausage extends Topping
case object Mushrooms extends Topping
case object Onions extends Topping

sealed trait CrustSize
case object SmallCrustSize extends CrustSize
case object MediumCrustSize extends CrustSize
case object LargeCrustSize extends CrustSize

sealed trait CrustType
case object RegularCrustType extends CrustType
case object ThinCrustType extends CrustType
case object ThickCrustType extends CrustType


```

之后我们可以定义pizza类如下：
```scala 
  class Pizza (
    var crustSize: CrustSize = MediumCrustSize, 
    var crustType: CrustType = RegularCrustType
) {

    // ArrayBuffer is a mutable sequence (list)
    val toppings = scala.collection.mutable.ArrayBuffer[Topping]()

    def addTopping(t: Topping): Unit = toppings += t
    def removeTopping(t: Topping): Unit = toppings -= t
    def removeAllToppings(): Unit = toppings.clear()

}
```

完整的带main函数的pizza类如下：
```scala 
  import scala.collection.mutable.ArrayBuffer

sealed trait Topping
case object Cheese extends Topping
case object Pepperoni extends Topping
case object Sausage extends Topping
case object Mushrooms extends Topping
case object Onions extends Topping

sealed trait CrustSize
case object SmallCrustSize extends CrustSize
case object MediumCrustSize extends CrustSize
case object LargeCrustSize extends CrustSize

sealed trait CrustType
case object RegularCrustType extends CrustType
case object ThinCrustType extends CrustType
case object ThickCrustType extends CrustType

class Pizza (
    var crustSize: CrustSize = MediumCrustSize, 
    var crustType: CrustType = RegularCrustType
) {

    // ArrayBuffer is a mutable sequence (list)
    val toppings = ArrayBuffer[Topping]()

    def addTopping(t: Topping): Unit = toppings += t
    def removeTopping(t: Topping): Unit = toppings -= t
    def removeAllToppings(): Unit = toppings.clear()

    override def toString(): String = {
        s"""
        |Crust Size: $crustSize
        |Crust Type: $crustType
        |Toppings:   $toppings
        """.stripMargin
    }
}

// a little "driver" app
object PizzaTest extends App {
   val p = new Pizza
   p.addTopping(Cheese)
   p.addTopping(Pepperoni)
   println(p)
}
```

# trait

[↑↑](#目录)
前言：
Scala traits are a great feature of the language. As you’ll see in the following lessons, you can use them just like a Java interface, and you can also use them like abstract classes that have real methods. Scala classes can also extend and “mix in” multiple traits.

# 把trait当做接口使用

想像你要写代码去给猫狗这样的动物建模，每个动物都有尾巴。你可以定义一个尾巴trait：
```scala 

trait TailWagger {
    def startTail(): Unit
    def stopTail(): Unit
}
 
```

```java 
  public interface TailWagger {
    public void startTail();
    public void stopTail();
}
```
## 继承trait

```scala 
 class Dog extends TailWagger {
    // the implemented methods
    def startTail(): Unit = println("tail is wagging")
    def stopTail(): Unit = println("tail is stopped")
} 
```

或者简写
```scala 
  class Dog extends TailWagger {
    def startTail() = println("tail is wagging")
    def stopTail() = println("tail is stopped")
}
```

## 多重继承

你可将动物的很多特性分割成很多小的，逻辑上的，模块的组件。

```scala 

trait Speaker {
    def speak(): String
}

trait TailWagger {
    def startTail(): Unit
    def stopTail(): Unit
}

trait Runner {
    def startRunning(): Unit
    def stopRunning(): Unit
} 
```

你的狗可以继承这些属性，并且实现这些必要的方法。

```scala 
class Dog extends Speaker with TailWagger with Runner {

    // Speaker
    def speak(): String = "Woof!"

    // TailWagger
    def startTail(): Unit = println("tail is wagging")
    def stopTail(): Unit = println("tail is stopped")

    // Runner
    def startRunning(): Unit = println("I'm running")
    def stopRunning(): Unit = println("Stopped running")

} 
```

Notice how **extends** and **with** are used to create a class from multiple traits:

* **extends**继承第一个trait
* **with**继承随后的trait

但是scalatrait不是像java中的接口。。。

# 使用trait就像抽象类


[↑↑](#目录)

In the previous lesson we showed how to use Scala traits like the original Java interface, but they have much more functionality than that. You can also add real, working methods to them and use them like abstract classes, or more accurately, as mixins.

```scala
trait Pet {
    def speak { println("Yo") }   // concrete implementation of a speak method
    def comeToMaster(): Unit      // abstract
}


class Dog(name: String) extends Pet {
    def comeToMaster(): Unit = println("Woo-hoo, I'm coming!")
}
```



## 重写一个被实现的方法。


```scala
class Cat extends Pet {
    // override 'speak'
    override def speak(): Unit = println("meow")
    def comeToMaster(): Unit = println("That's not gonna happen.")
}
```

在REPL中
```scala
scala> val c = new Cat
c: Cat = Cat@1953f27f

scala> c.speak
meow

scala> c.comeToMaster
That's not gonna happen.
```
## 多重继承带有行为的traits

```scala
trait Speaker {
    def speak(): String   //abstract
}

trait TailWagger {
    def startTail(): Unit = println("tail is wagging")
    def stopTail(): Unit = println("tail is stopped")
}

trait Runner {
    def startRunning(): Unit = println("I'm running")
    def stopRunning(): Unit = println("Stopped running")
}
//Now you can create a Dog class that extends all of those traits while providing behavior for the speak method:
class Dog(name: String) extends Speaker with TailWagger with Runner {
    def speak(): String = "Woof!"
}
//And here’s a Cat class:

class Cat extends Speaker with TailWagger with Runner {
    def speak(): String = "Meow"
    override def startRunning(): Unit = println("Yeah ... I don't run")
    override def stopRunning(): Unit = println("No need to stop")
}

```

The REPL shows that this all works like you’d expect it to work. First, a Dog:
```scala
scala> d.speak
res0: String = Woof!

scala> d.startRunning
I'm running

scala> d.startTail
tail is wagging
```
Then a Cat:
```scala
scala> val c = new Cat
c: Cat = Cat@1b252afa

scala> c.speak
res1: String = Meow

scala> c.startRunning
Yeah ... I don't run

scala> c.startTail
tail is wagging
```


# 抽象类（abstract classes）
[↑↑](#目录)

scala的抽象类和java的抽象类是一样的，但是traits太强大了，所以你很少适应抽象类。事实上，你只会在以下情况下使用抽象类：
* 你想创建一个要求构造函数参数的基础类
* 你的代码会被java代码调用


## scala traits 不允许构造器参数

```scala
// this won’t compile
trait Animal(name: String)
//Therefore, you need to use an abstract class whenever a base behavior must have constructor parameters:


abstract class Animal(name: String)

```


但是，请注意类只能继承一个抽象类。

## 当你的代码会被java代码调用
java不认识trait，所以你的代码要想被java调用，就得用抽象函数。

## 抽象类的语法

抽象类的语法和trait完全一样。
```scala
abstract class Pet (name: String) {
    def speak(): Unit = println("Yo")   // concrete implementation
    def comeToMaster(): Unit            // abstract method
}

class Dog(name: String) extends Pet(name) {
    override def speak() = println("Woof")
    def comeToMaster() = println("Here I come!")
}
```


注意参数name是由下向上传递的，所以name=‘fido’用dog传递给pet。
```scala
abstract class Pet (name: String) {
    def speak { println(s"My name is $name") }
}

class Dog(name: String) extends Pet(name)

val d = new Dog("Fido")
d.speak


scala> d.speak
My name is Fido
```
# scala的集合

你将经常使用的基础集合类有：

class| description 
---------|----------
ArrayBuffer | 	an indexed, mutable sequence
List | 	a linear (linked list), immutable sequence
Vector | an indexed, immutable sequence 
Map | 	the base Map (key/value pairs) class
Set | 	the base Set class

**map**和**set**可变和不可变的版本

> In the following lessons on Scala collections classes, whenever we use the word immutable, it’s safe to assume that the class is intended for use in a functional programming (FP) style. With these classes you don’t modify the collection; you apply functional methods to the collection to create a new result. You’ll see what this means in the examples that follow.

# ArrayBuffer
[↑↑](#目录)

如果你是从OOP来的移民，那么Arraybuffer就可能是你最方便的类。因为他是一个可变的序列，你可以用函数去改变它的内容，这些函数和java的序列是一样的额。

```scala
import scala.collection.mutable.ArrayBuffer

val ints = ArrayBuffer[Int]()
val names = ArrayBuffer[String]()
```

你可以有多种方式添加元素。

```scala
val ints = ArrayBuffer[Int]()
ints += 1
ints += 2

```
```scala
scala> ints += 1
res0: ints.type = ArrayBuffer(1)

scala> ints += 2
res1: ints.type = ArrayBuffer(1, 2)
```

也可以初始化添加元素

```scala
val nums = ArrayBuffer(1, 2, 3)


//Here are a few ways you can add more elements to this ArrayBuffer:

// add one element
nums += 4

// add multiple elements
nums += 5 += 6

// add multiple elements from another collection
nums ++= List(7, 8, 9)

```    

也可以删除元素用-=和--=函数

```scala
// remove one element
nums -= 9

// remove multiple elements
nums -= 7 -= 8

// remove multiple elements using another collection
nums --= Array(5, 6)
```

在REPL中

```scala
scala> import scala.collection.mutable.ArrayBuffer

scala> val nums = ArrayBuffer(1, 2, 3)
val nums: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3)

scala> nums += 4
val res0: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4)

scala> nums += 5 += 6
val res1: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5, 6)

scala> nums ++= List(7, 8, 9)
val res2: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5, 6, 7, 8, 9)

scala> nums -= 9
val res3: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5, 6, 7, 8)

scala> nums -= 7 -= 8
val res4: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5, 6)

scala> nums --= Array(5, 6)
val res5: ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4)

```

## ArrayBuffe能干更多的活


```scala
val a = ArrayBuffer(1, 2, 3)         // ArrayBuffer(1, 2, 3)
a.append(4)                          // ArrayBuffer(1, 2, 3, 4)
a.append(5, 6)                       // ArrayBuffer(1, 2, 3, 4, 5, 6)
a.appendAll(Seq(7,8))                // ArrayBuffer(1, 2, 3, 4, 5, 6, 7, 8)
a.clear                              // ArrayBuffer()

val a = ArrayBuffer(9, 10)           // ArrayBuffer(9, 10)
a.insert(0, 8)                       // ArrayBuffer(8, 9, 10)
a.insert(0, 6, 7)                    // ArrayBuffer(6, 7, 8, 9, 10)
a.insertAll(0, Vector(4, 5))         // ArrayBuffer(4, 5, 6, 7, 8, 9, 10)
a.prepend(3)                         // ArrayBuffer(3, 4, 5, 6, 7, 8, 9, 10)
a.prepend(1, 2)                      // ArrayBuffer(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a.prependAll(Array(0))               // ArrayBuffer(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

val a = ArrayBuffer.range('a', 'h')  // ArrayBuffer(a, b, c, d, e, f, g)
a.remove(0)                          // ArrayBuffer(b, c, d, e, f, g)
a.remove(2, 3)                       // ArrayBuffer(b, c, g)

val a = ArrayBuffer.range('a', 'h')  // ArrayBuffer(a, b, c, d, e, f, g)
a.trimStart(2)                       // ArrayBuffer(c, d, e, f, g)
a.trimEnd(2)                         // ArrayBuffer(c, d, e)
```

# List
[↑↑](#目录)

List 是一个线性的，不可变的序列。那意味着你不能像链表一样改变它。任何时候你添加或删除元素，你都是从一个已经存在的List创建一个新的List。

## Creating Lists 创建List
```scala

val ints = List(1, 2, 3)
val names = List("Joel", "Chris", "Ed")
```

虽然没必要，但是你还是可以声明列表的类型

```scala
val ints: List[Int] = List(1, 2, 3)
val names: List[String] = List("Joel", "Chris", "Ed")

```

## Adding elements to a List 添加元素

因为他是不可变的，所以你的每次更改都会产生一个新的list，因此，你得用一个变量去接受他。

```scala
val a = List(1,2,3)
//You prepend elements to a List like this:

val b = 0 +: a
//and this:

val b = List(-1, 0) ++: a
```

```scala
scala> val b = 0 +: a
b: List[Int] = List(0, 1, 2, 3)

scala> val b = List(-1, 0) ++: a
b: List[Int] = List(-1, 0, 1, 2, 3)
```

> 因为它是一个单链表，因此你应该只用其预置的元素，而不是去改变它。它添加元素相对来说是一个缓慢的操作，尤其你对一个大序列进行操作。

>**tips** 如果你想要预置和添加元素到不可变的序列，请用vector

因为list是一个linked-class，所以不是用索引访问元素。如果你想使用索引访问元素，使用Vector和ArrayBuffer.

## 怎么去记忆成员函数

将“+”字符看成是代表序列的一边，所以当你使用+：你就知道列表list需要在右边.
```scala
0 +: a
```
相应的，：+列表就在左边

```scala
a:+4
```

一件很好的事情就是他们的名字是一致的，所以其他不可变的序列也是用一样的函数，就像Seq和Vector。

## 怎么循环列表

```scala
val names = List("Joel", "Chris", "Ed")



scala> for (name <- names) println(name)
Joel
Chris
Ed

```
所有的序列类都可以用上面的方法遍历。


# Vector

[↑↑](#目录)


Vector是可索引的，不可变的序列。
你可以通过listOfPeople(999999)快速访问Vector。


除了Vec是可索引的而List不可以外，两个类是一样的。

```scala
val nums = Vector(1, 2, 3, 4, 5)

val strings = Vector("one", "two")

val peeps = Vector(
    Person("Bert"),
    Person("Ernie"),
    Person("Grover")
)

```

它不可变，所以你添加新元素就得创建一个新的对象。

```scala
scala> val a = Vector(1,2,3)
a: Vector[Int] = List(1, 2, 3)

scala> val b = a :+ 4
b: Vector[Int] = List(1, 2, 3, 4)

scala> val b = a ++ Vector(4, 5)
b: Vector[Int] = List(1, 2, 3, 4, 5)

scala> val b = 0 +: a
b: Vector[Int] = List(0, 1, 2, 3)

scala> val b = Vector(-1, 0) ++: a
b: Vector[Int] = List(-1, 0, 1, 2, 3)

```
vector不是linked-list


# Map

Scala has both mutable and immutable Map classes. In this lesson we’ll show how to use the mutable class.

## Creating a mutable Map

```scala

//To use the mutable Map class, first import it:

import scala.collection.mutable.Map
//Then you can create a Map like this:

val states = collection.mutable.Map("AK" -> "Alaska")
```

## Adding elements to a Map

```scala
scala> val states = collection.mutable.Map("AK" -> "Alaska")
states: scala.collection.mutable.Map[String,String] = Map(AK -> Alaska)

scala> states += ("AL" -> "Alabama")
res0: states.type = Map(AL -> Alabama, AK -> Alaska)

scala> states += ("AR" -> "Arkansas", "AZ" -> "Arizona")
res1: states.type = Map(AZ -> Arizona, AL -> Alabama, AR -> Arkansas, AK -> Alaska)

scala> states ++= Map("CA" -> "California", "CO" -> "Colorado")
res2: states.type = Map(CO -> Colorado, AZ -> Arizona, AL -> Alabama, CA -> California, AR -> Arkansas, AK -> Alaska)

```
## Removing elements from a Map

```scala
scala> states -= "AR"
res3: states.type = Map(CO -> Colorado, AZ -> Arizona, AL -> Alabama, CA -> California, AK -> Alaska)

scala> states -= ("AL", "AZ")
res4: states.type = Map(CO -> Colorado, CA -> California, AK -> Alaska)

scala> states --= List("AL", "AZ")
res5: states.type = Map(CO -> Colorado, CA -> California, AK -> Alaska)
```
## Updating Map elements

```scala
scala> states("AK") = "Alaska, A Really Big State"

scala> states
res6: scala.collection.mutable.Map[String,String] = Map(CO -> Colorado, CA -> California, AK -> Alaska, A Really Big State)
```
## Traversing a Map

There are several different ways to iterate over the elements in a map. Given a sample map:

```scala
val ratings = Map(
    "Lady in the Water"-> 3.0, 
    "Snakes on a Plane"-> 4.0,
    "You, Me and Dupree"-> 3.5
)
```

a nice way to loop over all of the map elements is with this for loop syntax:

```scala
for ((k,v) <- ratings) println(s"key: $k, value: $v")
```
Using a match expression with the foreach method is also very readable:

```scala

ratings.foreach {
    case(movie, rating) => println(s"key: $movie, value: $rating")
}
```

看(MapClassDocumentation)[https://docs.scala-lang.org/overviews/collections-2.13/maps.html]获得更多例子和信息


# set
元素不可重复。

Scala has both mutable and immutable Set classes. In this lesson we’ll show how to use the mutable class.


## Adding elements to a Set
To use a mutable Set, first import it:

```scala
scala> val set = scala.collection.mutable.Set[Int]()
val set: scala.collection.mutable.Set[Int] = Set()

scala> set += 1
val res0: scala.collection.mutable.Set[Int] = Set(1)

scala> set += 2 += 3
val res1: scala.collection.mutable.Set[Int] = Set(1, 2, 3)

scala> set ++= Vector(4, 5)
val res2: scala.collection.mutable.Set[Int] = Set(1, 5, 2, 3, 4)
```

如果你要添加元素在集合中已经存在，则会被忽视。

Set also has an add method that returns true if an element is added to a set, and false if it wasn’t added. The REPL shows how it works:

```scala
scala> set.add(6)
res4: Boolean = true

scala> set.add(5)
res5: Boolean = false
```

## Deleting elements from a Set

You remove elements from a set using the -= and --= methods, as shown in the following examples:

```scala
scala> val set = scala.collection.mutable.Set(1, 2, 3, 4, 5)
set: scala.collection.mutable.Set[Int] = Set(2, 1, 4, 3, 5)

// one element
scala> set -= 1
res0: scala.collection.mutable.Set[Int] = Set(2, 4, 3, 5)

// two or more elements (-= has a varargs field)
scala> set -= (2, 3)
res1: scala.collection.mutable.Set[Int] = Set(4, 5)

// multiple elements defined in another sequence
scala> set --= Array(4,5)
res2: scala.collection.mutable.Set[Int] = Set()
```


There are more methods for working with sets, including clear and remove, as shown in these examples:

```scala
scala> val set = scala.collection.mutable.Set(1, 2, 3, 4, 5)
set: scala.collection.mutable.Set[Int] = Set(2, 1, 4, 3, 5)

// clear
scala> set.clear()

scala> set
res0: scala.collection.mutable.Set[Int] = Set()

// remove
scala> val set = scala.collection.mutable.Set(1, 2, 3, 4, 5)
set: scala.collection.mutable.Set[Int] = Set(2, 1, 4, 3, 5)

scala> set.remove(2)
res1: Boolean = true

scala> set
res2: scala.collection.mutable.Set[Int] = Set(1, 4, 3, 5)

scala> set.remove(40)
res3: Boolean = false
```


Scala has several more Set classes, including SortedSet, LinkedHashSet, and more. Please see the (Set class documentation)[https://docs.scala-lang.org/overviews/collections-2.13/sets.html] for more details on those classes.


# Anonymous Functions 匿名函数

学习匿名函数可让你更好地理解什么是函数式编程。

首先看下面例子

```scala
val ints = List(1,2,3)

```
获取ints每个元素的翻倍数组。

```scala
val doubledInts = ints.map(_ * 2)
val doubledInts = ints.map((i: Int) => i * 2)
val doubledInts = ints.map(i => i * 2)
```
以上三种方式都可以。

> 在scala中，_是通配符。

## 匿名函数和filter函数。

```

val ints = List.range(1, 10)

scala> val x = ints.filter(_ > 5)
x: List[Int] = List(6, 7, 8, 9)

scala> val x = ints.filter(_ < 5)
x: List[Int] = List(1, 2, 3, 4)

scala> val x = ints.filter(_ % 2 == 0)
x: List[Int] = List(2, 4, 6, 8)
```

## 稍稍往下挖一点

你可能想知道**map**和**filter**是怎么运行的。简短的回答就是map要求一个函数，这个函数将输入转化为另一个数。filter就是要求一个函数，输入参数返回一个布尔类型的数。

所以下面的写法是可行的

```scala
val ints = List(1,2,3)
def double(i: Int): Int = i * 2   //a method that doubles an Int
val doubledInts = ints.map(double)
```

```scala
def lessThanFive(i: Int): Boolean = if (i < 5) true else false

//or more concisely, like this:

def lessThanFive(i: Int): Boolean = (i < 5)



val ints = List.range(1, 10)
val y = ints.filter(lessThanFive)
```



# 一般的序列方法

scala集合类的强大之处在于他们准备了很多的预建函数。其中一个收益之处就是你不再需要自定义一个for循环去操作集合。

我们只展示最常用的函数给你：

* map
* filter
* foreach
* head
* tail
* take, takeWhile
* drop, dropWhile
* find
* reduce, fold

## **重要注意点**
这些方法不会改变集合，而是返回一个新的集合。

```scala
scala> val nums = (1 to 10).toList
nums: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> val names = List("joel", "ed", "chris", "maurice")
names: List[String] = List(joel, ed, chris, maurice)

```

## 简单的list例子

```scala
scala> val nums = (1 to 10).toList
nums: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> val names = List("joel", "ed", "chris", "maurice")
names: List[String] = List(joel, ed, chris, maurice)
```

#### map方法

**map**方法会对列表的每一个元素应用你的算法。然后会返回一个由你改变的元素组成的新的列表。



```scala
cala> val doubles = nums.map(_ * 2)
doubles: List[Int] = List(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
```

也可以书写一个匿名函数

```scala
scala> val doubles = nums.map(i => i * 2)
doubles: List[Int] = List(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

```
不过在本课程当中，我们总是用第一个，因为它更简短。

```scala
scala> val capNames = names.map(_.capitalize)
capNames: List[String] = List(Joel, Ed, Chris, Maurice)

scala> val doubles = nums.map(_ * 2)
doubles: List[Int] = List(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

scala> val lessThanFive = nums.map(_ < 5)
lessThanFive: List[Boolean] = List(true, true, true, true, false, false, false, false, false, false)
```
上面的例子说明，你可以合法返回一个和原来类型不一样的列表。

#### filter方法
filter方法从一个给定的列表中返回一个新的过滤过的列表。
```scala
scala> val lessThanFive = nums.filter(_ < 5)
lessThanFive: List[Int] = List(1, 2, 3, 4)

scala> val evens = nums.filter(_ % 2 == 0)
evens: List[Int] = List(2, 4, 6, 8, 10)

scala> val shortNames = names.filter(_.length <= 4)
shortNames: List[String] = List(joel, ed)
```
上面的方法用map就是返回bool类型列表了。


#### foreach

foreach用来循环集合中的所有元素。就像之前我们在课程中提到的，foreach是用来提供副作用的。比如输出信息。


```scala

scala> names.foreach(println)
joel
ed
chris
maurice
```

**num**list有一点长，所以我们不想完全输出它。
```scala
scala> nums.filter(_ < 4).foreach(println)
1
2
3
```

#### head方法
head方法从Lisp和函数式编程语言中来。它用来打印列表的头元素。
```scala
scala> nums.head
res0: Int = 1

scala> names.head
res1: String = joel
```
因为字符串也是列表，所以也可进行head、。
```scala
scala> "foo".head
res2: Char = f

scala> "bar".head
res3: Char = b
```

#### tail

tail和head一样 ，来自于Lisp和函数式编程语言。它用来打印每一个在head后面的元素。
```scala
scala> nums.tail
res0: List[Int] = List(2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> names.tail
res1: List[String] = List(ed, chris, maurice)
```
字符串也可以作用。
```scala
scala> "foo".tail
res2: String = oo

scala> "bar".tail
res3: String = ar
```

#### take, takeWhile

这两个方法提供给你一个很好的方式取出元素，去创建一个新列表。
```scala
scala> nums.take(1)
res0: List[Int] = List(1)

scala> nums.take(2)
res1: List[Int] = List(1, 2)

scala> names.take(1)
res2: List[String] = List(joel)

scala> names.take(2)
res3: List[String] = List(joel, ed)

scala> nums.takeWhile(_ < 5)
res4: List[Int] = List(1, 2, 3, 4)

scala> names.takeWhile(_.length < 5)
res5: List[String] = List(joel, ed)
```
####  drop, dropWhile

这两个函数是上面两个函数的对应相反的函数。
```scala
scala> nums.drop(1)
res0: List[Int] = List(2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> nums.drop(5)
res1: List[Int] = List(6, 7, 8, 9, 10)

scala> names.drop(1)
res2: List[String] = List(ed, chris, maurice)

scala> names.drop(2)
res3: List[String] = List(chris, maurice)

scala> nums.dropWhile(_ < 5)
res4: List[Int] = List(5, 6, 7, 8, 9, 10)

scala> names.dropWhile(_ != "chris")
res5: List[String] = List(chris, maurice)
```

#### reduce
When you hear the term, “map reduce,” the “reduce” part refers to methods like reduce. It takes a function (or anonymous function) and applies that function to successive elements in the list.

The best way to explain reduce is to create a little helper method you can pass into it. For example, this is an add method that adds two integers together, and also gives us some nice debug output:
```scala
def add(x: Int, y: Int): Int = {
    val theSum = x + y
    println(s"received $x and $y, their sum is $theSum")
    theSum
}
```
Now, given that method and this list:
```scala

val a = List(1,2,3,4)
this is what happens when you pass the add method into reduce:

scala> a.reduce(add)
received 1 and 2, their sum is 3
received 3 and 3, their sum is 6
received 6 and 4, their sum is 10
res0: Int = 10
```
As that result shows, reduce uses add to reduce the list a into a single value, in this case, the sum of the integers in the list.

Once you get used to reduce, you’ll write a “sum” algorithm like this:
```scala
scala> a.reduce(_ + _)
res0: Int = 10
Similarly, this is what a “product” algorithm looks like:

scala> a.reduce(_ * _)
res1: Int = 24

```

That might be a little mind-blowing if you’ve never seen it before, but after a while you’ll get used to it.

> Before moving on, an important part to know about reduce is that — as its name implies — it’s used to reduce a collection down to a single value.

## 总结

这些方法让你远离书写for循环。但是本书不会完全的覆盖介绍，详细见[ the collections overview of sequence traits.](https://docs.scala-lang.org/overviews/collections-2.13/seqs.html)

# 普通的map的方法（map是个类，不是前面提到的函数）
在这节课，我们将会阐述一些被用的最多的map方法。在这些初始的例子中，我们将会使用immutable的map

给定一个不可变的map：
```scala
val m = Map(
    1 -> "a", 
    2 -> "b", 
    3 -> "c",
    4 -> "d"
)
```

下面是map可用函数的例子：
```scala
// how to iterate over Map elements
scala> for ((k,v) <- m) printf("key: %s, value: %s\n", k, v)
key: 1, value: a
key: 2, value: b
key: 3, value: c
key: 4, value: d

// how to get the keys from a Map
scala> val keys = m.keys
keys: Iterable[Int] = Set(1, 2, 3, 4)

// how to get the values from a Map
scala> val values = m.values
val values: Iterable[String] = MapLike.DefaultValuesIterable(a, b, c, d)

// how to test if a Map contains a value
scala> val contains3 = m.contains(3)
contains3: Boolean = true

// how to transform Map values
scala> val ucMap = m.transform((k,v) => v.toUpperCase)
ucMap: scala.collection.immutable.Map[Int,String] = Map(1 -> A, 2 -> B, 3 -> C, 4 -> D)

// how to filter a Map by its keys
scala> val twoAndThree = m.view.filterKeys(Set(2,3)).toMap
twoAndThree: scala.collection.immutable.Map[Int,String] = Map(2 -> b, 3 -> c)

// how to take the first two elements from a Map
scala> val firstTwoElements = m.take(2)
firstTwoElements: scala.collection.immutable.Map[Int,String] = Map(1 -> a, 2 -> b)

```
> Note that the last example probably only makes sense for a sorted Map.

## Mutable Map examples

给定一个初始化的可变map：
```scala
val states = scala.collection.mutable.Map(
    "AL" -> "Alabama", 
    "AK" -> "Alaska"
)
```
下面是你可以对可变map做的操作。
```scala
// add elements with +=
states += ("AZ" -> "Arizona")
states += ("CO" -> "Colorado", "KY" -> "Kentucky")

// remove elements with -=
states -= "KY"
states -= ("AZ", "CO")

// update elements by reassigning them
states("AK") = "Alaska, The Big State"

// retain elements by supplying a function that operates on
// the keys and/or values
states.retain((k,v) => k == "AK")
```
## see also
见[ Map class documentation](https://docs.scala-lang.org/overviews/collections-2.13/maps.html)获取更多细节和例子。
[见博客看"->","=>"的区别](https://blog.csdn.net/someInNeed/article/details/90047624)

# Tuples
tuple是一个简洁的类，这个类可以存储异质的项在一个容器里。举个例子，假设你有一个下面的类：
```scala
class Person(var name: String)
```
你不用像下面那样创建一个数据类去存储它：
```scala
class SomeThings(i: Int, s: String, p: Person)
```
而是可以用tuple：
```scala
val t = (3, "Three", new Person("Al"))

```

就像展示得那样，你直接把一些元素放入圆括号即可。
**tuple**可以包含2到22个项。这些人类名分别为Tuple2,...,Tuple22

## 更多得细节

这里有两个双元素得tuple

```scala
scala> val d = ("Maggie", 30)
d: (String, Int) = (Maggie,30)
```
三元素tuple
```scala
scala> case class Person(name: String)
defined class Person

scala> val t = (3, "Three", new Person("David"))
t: (Int, java.lang.String, Person) = (3,Three,Person(David))

```

有好几种访问元素的方式，其中一种就是用索引访问。每一个索引值前面都有一个前缀'_'

```scala
scala> t._1
res1: Int = 3

scala> t._2
res2: java.lang.String = Three

scala> t._3
res3: Person = Person(David)
```

其他可以炫酷访问的方式。

```scala

scala> val(x, y, z) = (3, "Three", new Person("David"))
x: Int = 3
y: String = Three
z: Person = Person(Al)

```

## Returning a tuple from a method

你想像python一样返回多个数值？python使用了元组，而tuple很像元组。

```scala
def getStockInfo = {
    // other code here ...
    ("NFLX", 100.00, 101.00)  // this is a Tuple3
}

val (symbol, currentPrice, bidPrice) = getStockInfo
```
在java中你要实现上面的返回得要创建专门的类感觉有些多余，所以tuple十分方便。

> 
## 注意

tuple不是集合，所有集合方法如：map、filter、etc都无法使用。

# 一个面向对象的例子(AN OOP EXAMPLE)

https://docs.scala-lang.org/overviews/scala-book/oop-pizza-example.html 讲了oop编程的例子，就不再翻译了。


# SBT and ScalaTest
在下一节课，你将看到一对常用的工具。

* SBT build tool
* Scala Test

# SBT
你可以用Ant、Maven、Gradle构建scala项目。但是一个名叫SBT的工具是首选。

由于不涉及编程以及项目没用到它，就不学习了。以后如果有机会用到可以看下面的网址。

https://docs.scala-lang.org/overviews/scala-book/scala-build-tool-sbt.html

# ScalaTest
ScalaTest是一个测试框架，很像java中的Junit

和上一节一样原因，就不学习了。

https://docs.scala-lang.org/overviews/scala-book/sbt-scalatest-tdd.html

# BDD测试风格
参考：

https://docs.scala-lang.org/overviews/scala-book/sbt-scalatest-bdd. 
                     
https://dannorth.net/introducing-bdd/     
                                                         
                                                           
https://baike.baidu.com/item/%E8%A1%8C%E4%B8%BA%E9%A9%B1%E5%8A%A8%E5%BC%80%E5%8F%91/9424963?fromtitle=BDD&fromid=10735732&fr=aladdin                   
https://blog.csdn.net/Testfan_zhou/article/details/90898603 



# 函数式编程

我们将介绍scala支持函数式编程。

函数式编程式一种强调只使用纯碎的函数和不可变变量的编程风格。与其用这种描述，不如说程序员有一种强烈的渴望把他们的代码看作数学--把他们的函数看成一系列的代数等式。in that regard，你可以说程序员作为数学家。这种强烈的渴望使他们只用纯粹的函数以及不可变变量，因为在代数和其他形式的数学中也是这样使用得。

函数式编程是一个巨大的话题，这里只用一种简单的方式把整个话题压缩入这本小小的书中，但是在接下来的课程中，我们将让你体味函数编程，并展示一些scala提供给开发者的函数式编程工具。

# pure function

pure function 的定义：

* 函数的输出只和它的输入有关。 
* 它不会改变任何隐状态。
* 它不会从外部世界读取数据，包括控制台，web服务，数据，文件等。也不会把数据写到外部世界。

按照这种定义，函数相同的输入会有相同的输出。


## Examples of pure functions
Given that definition of pure functions, as you might imagine, methods like these in the scala.math._ package are pure functions:

* abs
* ceil
* max
* min
These Scala String methods are also pure functions:

* isEmpty
* length
* substring
Many methods on the Scala collections classes also work as pure functions, including drop, filter, and map.

## Examples of impure functions
相反地，下面一些非纯粹函数的列子，因为它们违反了定义。

**foreach**函数式不纯粹的，因为它只用来产生副作用，比如标准输出。

>一个明显的线索关于**foreach**不纯粹是它的签名声明--它返回类型是**Unit**。因为它不反回任何东西，所以逻辑上调用它只能取得副作用。同样的任何返回**Unit**的函数都不是纯粹函数。

Data和time相关函数如：getDayOfWeek, getHour, and getMinute都是不纯粹的，因为它们的输出不依赖它们的输入。


In general, impure functions do one or more of these things:

* Read hidden inputs, i.e., they access variables and data not explicitly passed into the function as input parameters
* Write hidden outputs
* Mutate the parameters they are given
* Perform some sort of I/O with the outside world

## But impure functions are needed …

当然一个不能读写外部世界的应用是毫无用处的，所以一些人如下建议：
```
Write the core of your application using pure functions, and then write an impure “wrapper” around that core to interact with the outside world. If you like food analogies, this is like putting a layer of impure icing on top of a pure cake.
```

## 书写纯粹函数

在scala中书写纯粹函数是一件很简单的事情，只需要用scala函数语法书写。

书写翻倍函数：

```scala
def double(i: Int): Int = i * 2
```

尽管本书没有覆盖递归，但我们仍给出富有挑战性的例子：对整数列表求和。（其实我没有看懂）
```scala
def sum(list: List[Int]): Int = list match {
    case Nil => 0//Nil是空List 
    case head :: tail => head + sum(tail)//lsit相等于head类和tail类组成。
}

```
[模式匹配](https://blog.csdn.net/Pengjx2014/article/details/82505337)
[list高级操作](https://blog.csdn.net/yuan_xw/article/details/49100627)
[match博客](https://blog.csdn.net/Next__One/article/details/77666782)

```
4种操作符的区别和联系

(1) :: 该方法被称为cons，意为构造，向队列的头部追加数据，创造新的列表。用法为 x::list,其中x为加入到头部的元素，无论x是列表与否，它都只将成为新生成列表的第一个元素，也就是说新生成的列表长度为list的长度＋1(btw, x::list等价于list.::(x))

(2) :+和+: 两者的区别在于:+方法用于在尾部追加元素，+:方法用于在头部追加元素，和::很类似，但是::可以用于pattern match ，而+:则不行. 关于+:和:+,只要记住冒号永远靠近集合类型就OK了。

(3) ++ 该方法用于连接两个集合，list1++list2

(4) ::: 该方法只能用于连接两个List类型的集合
————————————————
版权声明：本文为CSDN博主「pantherCode」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liu136313/article/details/79012626

```

#  Passing Function Around


FP的一个特性是允许你将函数作为变量，也就是说你可以把它作为函数的参数。之前在本书中看到的**map**和**filter**就是这样展现的：

```scala
val nums = (1 to 10).toList

val doubles = nums.map(_ * 2)
val lessThanFive = nums.filter(_ < 5)
```

在那些列子中，匿名函数被传入**map**和**filter**中。在本节中，我们示范下面的例子。
```scala
def double(i: Int): Int = i * 2   //a method that doubles an Int
val doubles = nums.map(double)
```

>如果你喜欢非正式的说法，也可以说是一个类把另外一个类的带参构造器作为参数。


# No Null Values

Functional programming is like writing a series of algebraic equations, and because you don’t use null values in algebra, you don’t use null values in FP. That brings up an interesting question: In the situations where you might normally use a null value in Java/OOP code, what do you do?

Scala’s solution is to use constructs like the Option/Some/None classes. We’ll provide an introduction to the techniques in this lesson.

## A first example

尽管第一个例子并没有处理空值问题，但是这也是一个很好的方式展示Option/Some/None类，所以我们从此开始。


想象一下，你想要写一个函数去转换String到Integer，然后你还想写一个优雅的方式去处理异常，比如当你得到一个String：“foo”而不是类似像“1”，抛出异常。

面对这样的函数，初步猜想可能是下面这样。
```scala
def toInt(s: String): Int = {
    try {
        Integer.parseInt(s.trim)
    } catch {
        case e: Exception => 0
    }
}
```
这样的函数在发生转换异常时返回0，但是这就不能知道你是真的接受一个“0”还是其他的未定义字符串。

## Using Option/Some/None

scala 的解决方案就是使用三个类，**Option/Some/None**。**Some**，**None**是**Option**的子类。
所以解决方案是下面这样的：


* 你申明toInt函数，反悔Option
* 如果toInt接受字符串参数可以转换为Integer就封装入Some。
* 如果toInt不能转换，就返回None。

```scala
def toInt(s: String): Option[Int] = {
    try {
        Some(Integer.parseInt(s.trim))
    } catch {
        case e: Exception => None
    }
}
```

```scala
scala> val a = toInt("1")
a: Option[Int] = Some(1)

scala> val a = toInt("foo")
a: Option[Int] = None
```
处理Null时也可以采用上面的方法。


## 详解Option[T]
在Scala里Option[T]实际上是一个容器，就像数组或是List一样，你可以把他看成是一个可能有零到一个元素的List。
当你的Option里面有东西的时候，这个List的长度是1（也就是 Some），而当你的Option里没有东西的时候，它的长度是0（也就是 None）。

for循环
如果我们把Option当成一般的List来用，并且用一个for循环来走访这个Option的时候，如果Option是None，那这个for循环里的程序代码自然不会执行，于是我们就达到了不用检查Option是否为None这件事。


```
scala> val map1 = Map("key1" -> "value1")
map1: scala.collection.immutable.Map[String,String] = Map(key1 -> value1)
 
scala> val value1 = map1.get("key1")
value1: Option[String] = Some(value1)
 
scala> val value2 = map1.get("key2")
value2: Option[String] = None
 
scala> def printContentLength(x: Option[String]) {
     |   for (c <- x){
     |     println(c.length)
     |   }
     | }
printContentLength: (x: Option[String])Unit
 
scala> printContentLength(value1)
6
 
scala> printContentLength(value2)

```
## map操作
在函数式编程中有一个核心的概念之一是转换，所以大部份支持函数式编程语言，都支持一种叫map()的动作，这个动作是可以帮你把某个容器的内容，套上一些动作之后，变成另一个新的容器。
现在我们考虑如何用Option的map方法实现length: xxx的输出形式：

 

/**先算出 Option 容器内字符串的长度
然后在长度前面加上 "length: " 字样
最后把容器走访一次，印出容器内的东西*/

```
scala> value1.map(_.length).map("length: " + _).foreach(println)
length: 6
 
scala> value1.map("length: " + _.length).foreach(println)
length: 6

```
透过这样「转换」的方法，我们一样可以达成想要的效果，而且同样不用去做「是否为 None」的判断。

## Being a consumer of toInt
作为toInt的消费之，你怎么去处理其返回值？

有两种主要的回答：
* 使用match表达式
* 使用for表达式

### Using a match expression

```scala

toInt(x) match {
    case Some(i) => println(i)
    case None => println("That didn't work.")
}
```
在本例中，如果x被转换为Int，那么第一个case的语句就会被执行。反之，执行第二个情形的语句。
### Using for/yield


```scala
val y = for {
    a <- toInt(stringA)
    b <- toInt(stringB)
    c <- toInt(stringC)
} yield a + b + c
val stringA = "1"
val stringB = "2"
val stringC = "3"

scala> val y = for {
     |     a <- toInt(stringA)
     |     b <- toInt(stringB)
     |     c <- toInt(stringC)
     | } yield a + b + c
y: Option[Int] = Some(6)

//As shown, y is bound to the value Some(6).

//To see the failure case, change any of those strings to something that won’t convert to an integer. When you do that, you’ll see that y is a None:

y: Option[Int] = None
```

## Options can be thought of as a container of 0 or 1 items

option可以看作0或者1个元素容器。

 * Some is a container with one item in it
 * None is a container, but it has nothing in it

 ## Using foreach

 因为Some和None可以被认为是容器，他们可以被看作是集合类。As a result, they have all of the methods you’d expect from a collection class, including map, filter, foreach, etc.

这就带来一个有趣的问题，下面两个会打印出啥东西？
```scala

toInt("1").foreach(println)
toInt("x").foreach(println)
```

答案是，前者打印1，后者啥都不打印。

## Using Option to replace null values

```scala
class Address (
    var street1: String,
    var street2: String,
    var city: String, 
    var state: String, 
    var zip: String
)


val santa = new Address(
    "1 Main Street",
    null,               // <-- D'oh! A null value!
    "North Pole",
    "Alaska",
    "99705"
)
```

解决方案：

```scala
class Address (
    var street1: String,
    var street2: Option[String],
    var city: String, 
    var state: String, 
    var zip: String
)
```
根据这定义的函数，开发者写正确的函数：
```scala
val santa = new Address(
    "1 Main Street",
    None,
    "North Pole",
    "Alaska",
    "99705"
)
```
或者
```scala
val santa = new Address(
    "123 Main Street",
    Some("Apt. 2B"),
    "Talkeetna",
    "Alaska",
    "99676"
)
```

## Option isn’t the only solution

This lesson focused on the** Option/Some/None **solution, but Scala has a few other alternatives. For example, a trio of classes known as **Try/Success/Failure **work in the same manner, but a) you primarily use these classes when code can throw exceptions, and b) the Failure class gives you access to the exception message. For example, **Try/Success/Failure **is commonly used when writing methods that interact with files, databases, and internet services, as those functions can easily throw exceptions. These classes are demonstrated in the Functional Error Handling lesson that follows.

