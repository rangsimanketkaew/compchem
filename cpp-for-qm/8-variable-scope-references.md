# Variable Scope และ Reference Types

ตัวแปร variable สามารถถูกกำหนดให้เป็น “local” (ถูกนำมาใช้ได้เฉพาะใน section ที่ถูกกำหนดหรือ declared ขึ้นมาเช่นในฟังก์ชันนั้น ๆ) หรือเป็น “global” (ถูกนำมาใช้ได้ในโปรแกรม)

## Local Variables

ตัวอย่างของ Local variables

```c++
#include <iostream>

using namespace std;

void junk(int);

int main()
{
  int i=1;

  cout << "in main, i= " << i << endl;
  junk(i);
  cout << "in main, i= " << i << endl;

  return 0;
}

void junk(int i)
{
  i=2;
  cout << "in junk, i= " << i << endl;
}
```

ถ้าเราคอมไพล์โค้ดอันนี้แล้วทำการรันเราจะได้เอาต์พุตดังนี้ 

```
in main, i=1
in junk, i=2
in main, i=1
```

เราสามารถเปลี่ยนค่าของตัวแปรในฟังก์ชันได้อย่างไร? เราสามารถทำได้คือการกำหนดหรือใส่ address ของตัวแปร variable เข้าไปในฟังก์ชันซึ่งก็คือการใช้ pointer สำหรับ variable นั้น ๆ นั่นเอง 

```c++
#include <iostream>

using namespace std;

void junk(int *);

int main()
{
  int i=1;

  cout << "in main, i= " << i << endl;
  junk(&i);
  cout << "in main, i= " << i << endl;

  return 0;
}

void junk(int *i)
{
  *i=2;
  cout << "in junk, i= " << *i << endl;
}
```

ซึ่งโค้ดด้านบนจะให้เอาต์พุตที่แตกต่างจากโค้ดก่อนหน้านี้นิดนึง ดังนี้ 

```
in main, i=1
in junk, i=2
in main, i=2
```

## Global Variables

ถ้าเราต้องการให้ตัวแปร variable นั้นสามารถถูกเรียกใช้ในฟังก์ชันอื่น ๆ ในโปรแกรมของเราด้วยนั้นเราจะต้องประกาศ declare ให้ variable เป็น _globally_ ซึ่งสามารถทำได้ดังนี้

```c++
#include <iostream>

using namespace std;

int i;
void junk(void);

int main()
{
  i=1;

  cout << "in main, i= " << i << endl;
  junk();
  cout << "in main, i= " << i << endl;

  return 0;
}

void junk(void)
{
  i=2;
  cout << "in junk, i= " << i << endl;
}
```

ซึ่งโค้ดอันนี้จะให้เอาต์พุตเหมือนกับโค้ดก่อนหน้านี้ 

```
in main, i=1
in junk, i=2
in main, i=2
```

## Reference Types

C++ มีสิ่งที่เรียกว่า reference types ด้วยซึ่งเกี่ยวข้องกับ pointer แต่ว่าจะมีความปลอดภัยกว่าในการนำไปใช้งานถึงแม้ว่าจะ flexible น้อยกว่า pointer ก็ตาม 

Reference types สามารถถูกประกาศหรือ declared ได้โดยการใช้ `&` ดังต่อไปนี้ 

```c++
#include <iostream>

using namespace std;

void junk(int &);

int main()
{
  int i=1;

  cout << "in main, i= " << i << endl;
  junk(i);
  cout << "in main, i= " << i << endl;

  return 0;
}

void junk(int &i)
{
  i=2;
  cout << "in junk, i= " << i << endl;
}
```
