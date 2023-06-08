# ฟังก์ชัน (Functions)

Functions นั้นคือสิ่งที่โคตรสำคัญเลยในการเขียนโปรแกรมเพราะว่าฟังก์ชันนั้นก็คือโค้ดย่อย ๆ ที่เราสามารถนำมาใช้ซ้ำได้กี่ครั้งก็ได้ตามที่เราต้องการและยังช่วยให้เรา simplify โค้ดของเราด้วย ลองดูตัวอย่างดังต่อไปนี้

```c++
#include <iostream>
using namespace std;

double power(double, int);

int main()
{
  int exponent=18;
  double base=5.3;
  double value;

  value = power(base,exponent);
  cout.precision(12);
  cout << value << endl;

  return 0;
}

double power(double a, int n)
{
  int i;
  double val=a;

  for(i=1; i < n; i++)
    val *= a;

  return val;
}
```

Function `power()` นั้นคำนวณค่าของ (base)^(exponent) ซึ่งถูก defined ในส่วนของโค้ดในฟังก์ชัน `main()` โดยฟังก์ชันอันนี้จะทำการรับข้อมูลอินพุตเข้ามา 2 ตัว (2 arguments) นั่นคือ double กับ int แล้วก็ให้คำตอบหรือ return คืนค่าออกมาเป็น double

## Functions ในไฟล์ Source-code ที่ต่างกัน

ตัวอย่างด้านบนนั้นคือ definition ของฟังก์ชัน `power()` ในไฟล์เดียวกันกับฟังก์ชัน `main()` ซึ่งเราสามารถแยกฟังก์ชันนี้ออกจากกันให้อยู่กันคนละไฟล์ได้ เราสามารถนำโค้ดตั้งแต่บรรทัดแรกจนถึงสิ้นสุดของฟังก์ชัน `main()` เข้าไปยัดใส่ไว้ในไฟล์ใหม่ที่ชื่อว่า `func.cc` ได้และนำโค้ดที่อยู่ต่อจากฟังก์ชัน `main()` ไปใส่ไว้ในอีกไฟล์หนึ่งชื่อว่า `power.cc` แล้วเราสามารถคอมไพล์ได้ดังนี้

```shell
rangsiman% c++ -c func.c
rangsiman% c++ func.o -o func
  "power(double, int)", referenced from:
      _main in func.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

จำเห็นได้ว่ามันมี error เกิดขึ้นซึ่งเราจะต้องทำการคอมไพล์ source code แยกกันสำหรับแต่ละไฟล์ก่อนแล้วถึงค่อย link ไฟล์ objects ทั้งหมดเข้าด้วยกัน ดังนี้ 

```shell
rangsiman% c++ func.o power.o -o func
rangsiman% c++ power.o func.o -o func
rangsiman% func
1.08884397618e+13
```

## Make Utility

เมื่อเรามีไฟล์ source code หลาย ๆ ไฟล์ เช่น หลักสิบหรือถึงหลักร้อยไฟล์ ถ้าเราต้องมานั้งคอมไพล์ไฟล์และ link เองทั้งหมดก็คงเหนื่อยและไม่สะดวก ซึ่งวิธีแก้ที่ทำให้ชีวิตเราง่ายขึ้นก็คือใช้ตัวช่วย `make` ซึ่งเป็นโปรแกรมที่ช่วยในการคอมไพล์โปรแกรม
