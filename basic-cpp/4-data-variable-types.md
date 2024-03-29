# Data type และ Variables

Data type คือประเภทหรือชนิดของข้อมูล

Variables คือตัวแปร

ประเภทของข้อมูลนั้นมีเยอะมาก ๆ และก็มักจะถูกใช้บ่อยครั้งในการเขียนโปรแกรมคำนวณวิทยาศาสตร์โดยเฉพาะในภาษา C++

| Name   | Data                                                   | Typical Size (bytes) |
| :----- | :----------------------------------------------------- | :------------------- |
| int    | Integer                                                | 4                    |
| char   | Character                                              | 1                    |
| float  | Floating-point number                                  | 4                    |
| double | Double-precision Floating-point number                 | 8                    |
| void   | No Type (useful for defining functions with no return) | N/A                  |

โน๊ต: ขนาดของ data types สามารถที่จะเปลี่ยนหรือ vary ไปตามระบบของคอมพิวเตอร์ได้ ดังนั้นเราไม่ควรที่จะจำตัวเลขไปเพียงค่าเดียว ขนาดของข้อมูลในตารางข้างบนนั้นได้มาจากการใช้ฟังก์ชัน `sizeof()` ในการหาขนาดของข้อมูลในโปรแกรมของเรา

ตัวแปรคืออะไร? จริง ๆ แล้วตัวแปรหรือ variable นั้นก็คือตำแหน่งของหน่วยความจำที่ถูกใช้ในการเก็บข้อมูลเอาไว้ โดยตัวแปรก็คือชื่อที่ถูกกำหนดขึ้นมา ตัวอย่างเช่น

```C++
int iter = 0;       // ตัวแปรจำนวนเต็มที่มีค่าเริ่มต้นคือ 0
double energy;      // A double-precision floating-point number - ไม่มีการกำหนดค่าเริ่มต้น
int z_vals[50];     // อาร์เรย์ ที่มีการเก็บข้อมูลจำนวนเต็ม 50 integers
double geom[10][3]; // อาร์เรย์ขนาด 2 มิติของทศนิยม doubles
```
