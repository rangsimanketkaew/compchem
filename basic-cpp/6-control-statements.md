# Control Statements

โปรแกรม executable ที่เราคอมไพล์มาได้นั้นประกอบไปด้วย statements/instructions หลาย ๆ อันต่อกันซึ่งจะมีการทำงานเป็นลำดับไล่จากบนลงล่างขึ้นอยู่กับว่าฟังก์ชันอันถูกเรียกใช้งานก่อน

Control statements คือการกำหนดว่าเมื่อไหร่ flow ของโปรแกรมนั้นควรจะต้องถูก distupted ซึ่งการถูก disrupted ในที่นี้ไม่ได้เป็นการทำให้โปรแกรมสิ้นสุดการทำงานแต่เป็นการหยุดชั่วคราวและทำกระบวนการนั้น ๆ ตามหน้าที่ของ statements เช่น วนซ้ำหรือข้าม instruction ไป

เริ่มต้นคือเป็น control statements ที่มีการใส่เงื่อนไข

<table>
  <tr>
    <td><b>if-else</b></td>
    <td>Select different instructions based on a given set of conditions.</td>
  </tr>
</table>

```C++
if(iter >= maxiter){
    cout<< " Number of iterations exceeded\n";
    exit(2);
}
else {
    cout << "iter = " << iter << endl;
}
```

<table>
  <tr>
    <td><b>switch</b></td>
    <td>A multi-choice if statement.</td>
  </tr>
</table>

```c++
switch(val){
   case 0:
     cout << " Zilch\n";
   case 1:
     cout << " Uno\n";
   case 2:
     cout << " Dos\n";
   case 3:
     cout << " Tres\n;
   default:
     cout << "A bunch";
     break;
}
```

<table>
  <tr>
    <td><b>while loop</b></td>
    <td>Repeat a series of instructions while the given conditions hold true.</td>
  </tr>
</table>

```c++
int iter = 0;
int maxiter = 10;
while(iter < maxiter){
  x_coord += 2.0;
  iter++;
}
```

โน๊ต:
- ค่าของ `iter` และ `maxiter` จะต้องถูกกำหนด (initialized) ด้านนอกของลูป (loop)
- แล้วก็ถ้า `iter` ไม่ถูกปรับขึ้นข้างใน loop นั้นจะทำให้เกิด infinite loop หรือการวนไปเรื่อย ๆ ไม่มีที่สิ้นสุดเพราะว่าเงื่อนไขนั้นไม่เป็นจริงหรือตรงตามเงื่อนไขที่จะทำให้ instruction นั้นหยุดการทำงาน

<table>
  <tr>
    <td><b>do-while loop</b></td>
    <td>Similar to while, but the instructions are always evaluated at least one time, since the condition is not checked until the end.</td>
  </tr>
</table>

```c++
do {
   x_coord += 2.0;
   iter++;
} while(iter < maxiter);
```

<table>
  <tr>
    <td><b>for loop</b></td>
    <td>One of the most common and powerful control statements. Defines an initial state, a condition, and increment. Loop continues incrementing until the condition is no longer true.</td>
  </tr>
</table>

การเขียน loop แบบมาตรฐานทั่วไป

```c++
for(int i = 0; i < max; i++)
{
    cout<< " iter = "<< i << endl;
}
```

จริง ๆ แล้ว for loop นั้นมีหลายรูปแบบและเขียนได้แตกต่างกันขึ้นอยู่กับว่าต้องการออกแบบให้โปรแกรมนั้นมีหน้าที่อย่างไรซึ่งสิ่งที่กำหนด for loop นั้นก็คือ `iterators` 

ตัวอย่าง For loop ที่ใช้ `std::vector<double>::iterator`

```c++
#include <vector>
std::vector<double> vec = {1.0,2.0,3.0,4.0};
cout << " vec = { ";
for(std::vector<double>::iterator it = vec.begin(); it != vec.end(); ++it) {
  cout << " " << *it <<" "; \\ it is a pointer to an element of the vector
                            \\ we use the * operator to get the value pointed to by "it"
}
cout << " }\n";

```

ตัวอย่างด้านล่างคือ Range-based for loop ซึ่งเป็นการเขียนโค้ดด้านบนให้สั้นขึ้น

```c++
#include <vector>
std::vector<double> vec = {1.0,2.0,3.0,4.0};
cout << " vec = { ";
for(double& val: vec} {
  cout << " " << val << " ";
}
cout << " }\n";
```

<table>
  <tr>
    <td><b>break</b></td>
    <td>Exit a loop or switch based on a given condition (usually placed after an if statement for some condition).</td>
  </tr>
</table>

```c++
for(int i = 0; i < max; i++) {
   energy += 2.0;
   cout << " iter = " << i << endl;
   if(energy > 10.0) break;
}

```

โปรแกรมจะหลุดออกจาก For loop ด้านบนนี้เมื่อ `energy` นั้นมีค่ามากกว่า 10.0 ถึงแม้ว่า `i` มีค่าน้อยกว่า `max`
