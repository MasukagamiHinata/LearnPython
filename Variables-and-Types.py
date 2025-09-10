#浮動小数点数
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#文字列に対する演算の実行
hello = "Hello"
world = "world"
print(hello + "," + " " + world + "!")

#同じ行で複数の変数に同時に代入
a, b = 2, 3
print(a, b)

#数と文字列を混ぜて演算子を実行することはできない
a = 1
b = 2
c = "3"
print(a + b + c)

#上記の出力。
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#なぜ"unspported"なんだろう？出来たほうが一見便利そうなのに。何か事情があるみたい

#exercise
# 文字列、整数、浮動小数点数を作成すること。
# 文字列はmystringと名付け、"hello "という単語を含むものとする。
# 浮動小数点数はmyfloatと名付け、10.0という数値を含むものとし、整数はmyintと名付け、20という数値を含むものとする。
mystring = "hello"
myint = int(20.05)
myfloat = float(10)
