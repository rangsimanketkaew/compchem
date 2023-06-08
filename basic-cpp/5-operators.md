# Operators

ในภาษา C++ นั้นมีตัวดำเนินการ (Operator) หลาย ๆ ตัวที่ภาษาอื่น ๆ ก็ใช้ซึ่งก็เป็นการดำเนินการทางคณิตศาสตร์ทั่วไปไม่ได้มีความพิศดารอะไรมาก

## Arithmetic Operators

| Operator | Action                            | Example                              |
| :------- | :-------------------------------- | :----------------------------------- |
| =        | Assignment                        | `x = y`                              |
| +        | Addition                          | `c = a+b`                            |
| -        | Subtraction                       | `c = a-b`                            |
| \*       | Multiplication                    | `c = a*b`                            |
| /        | Division                          | ` c = a/b`                           |
| %        | Modulo (remainder after division) | `rem = a%b`                          |
| +=       | Add then assign                   | ` a += b` (equivalent to ` a = a+b`) |
| -=       | Subtract then assign              | ` a-=b` (equivalent to `a = a-b`)    |
| \*=      | Multiply then assign              | ` a*=b` (equivalent to ` a = a*b`)   |
| /=       | Divide then assign                | ` a /=b` (equivalent to ` a = a/b`)  |
| ++       | Increment                         | `a = 0; a++;` (a now is 1 )          |
| --       | Decrement                         | `a = 1; a--;` (a is now 0)           |

## Boolean Comparison Operators

| Operator | Action                   | Example   |
| :------- | :----------------------- | :-------- |
| ==       | Equal to                 | `a == b`  |
| !=       | Not equal to             | ` a != b` |
| >        | Greater than             | ` a > b`  |
| <        | Less than                | `a < b`   |
| >=       | Greater than or equal to | ` a >= b` |
| <=       | Less than or equal to    | ` a <= b` |

Note: Boolean operator statements return zero if false and non-zero if true

## Logical Operators

| Operator | Action | Example                |
| :------- | :----- | :--------------------- | --- | ---------- |
| &&       | And    | `(a == b) && (b == c)` |
| \|\|     | Or     | ` (a == b)             |     | (b == c) ` |
| !        | Not    | `!(a == b)`            |

โน๊ต: ลิสต์ด้านบนนั้นจะมี operator บางตัวที่มีนิยามหรือหลายความหมายได้ซึ่งขึ้นอยู่กับบริบท เช่น `*` คือ operator ที่สามารถใช้ในการคูณระหว่างตัวเลขได้และก็สามารถเป็นตัวที่ใช้ในการ dereference pointer ได้เช่นเดียวกัน ถ้าอยากดูรายละเอียดเพิ่มเติมผมแนะนำเว็บนี้ครับ [Pointers/references](https://github.com/CrawfordGroup/ProgrammingProjects/wiki/Variable-Scope-and-Reference-Types) 