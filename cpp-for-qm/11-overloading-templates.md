# Overloading และ Templates

ฟีเจอร์อย่างหนึ่งของภาษาที่เป็น OOP แบบ C++ นั้นก็คือมีฟังก์ชันที่เป็น overload ได้ กล่าวคือสามารถใช้ฟังก์ชันที่มีชื่อเดียวกันในการทำงานหรือมีหน้าที่แตกต่างกันไปได้ขึ้นอยู่กับ arguments ที่เราใส่เข้าไปให้กับฟังก์ชัน เช่น

```c++
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cassert>

Molecule::Molecule(const char *filename, int n, int q)
{
  natom = n;
  charge = q;

  // allocate space
  zvals = new int[natom];
  geom = new double* [natom];
  for(int i=0; i < natom; i++)
    geom[i] = new double[3];

  std::ifstream is(filename);
  assert(is.good());

  for(unsigned int i=0; i < natom; i++)
    is >> zvals[i] >> geom[i][0] >> geom[i][1] >> geom[i][2];

  is.close();
}
```
