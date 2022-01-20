from turtle import *
import random
import time
n = 80.0

 7speed("fastest")
 8screensize(bg='seashell')
 9left(90)
10forward(3*n)
11color("orange", "yellow")
12begin_fill()
13left(126)
14
15for i in range(5):
16    forward(n/5)
17    right(144)
18    forward(n/5)
19    left(72)
20end_fill()
21right(126)
22
23color("dark green")
24backward(n*4.8)
25def tree(d, s):
26    if d <= 0: return
27    forward(s)
28    tree(d-1, s*.8)
29    right(120)
30    tree(d-3, s*.5)
31    right(120)
32    tree(d-3, s*.5)
33    right(120)
34    backward(s)
35tree(15, n)
36backward(n/2)
37
38for i in range(200):
39    a = 200 - 400 * random.random()
40    b = 10 - 20 * random.random()
41    up()
42    forward(b)
43    left(90)
44    forward(a)
45    down()
46    if random.randint(0, 1) == 0:
47            color('tomato')
48    else:
49        color('wheat')
50    circle(2)
51    up()
52    backward(a)
53    right(90)
54    backward(b)
55time.sleep(60)