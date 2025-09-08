#四則演算
number = 1 + 2 * 3 / 4
print(number) #出力は2.5
number = 1 + 2 * 3 / 4.0
print(number) #出力は2.5

#モジュロ演算子。除算の余りを整数で返す
remainder = 4 % 3
print(remainder) #出力は1

#乗算
squared = 4 ** 2
print(squared) #出力は16

#文字列も同様に演算できる
helloworld = "Hello" + "," +" " + "world!"
print(helloworld) #出力はHello, world!
hello_10 = "hello" * 10
print(hello_10) #出力はhellohellohellohellohellohellohellohellohellohello

#リストにも演算可能
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
sorted_all_numbers = sorted(all_numbers)
print(all_numbers) #出力は[2, 4, 6, 8, 1, 3, 5, 7]
print(sorted_all_numbers) #出力は[1, 2, 3, 4, 5, 6, 7, 8]

print([1, 2, 3] * 3) #出力は[1, 2, 3, 1, 2, 3, 1, 2, 3]

#リストの各要素に3をかけるには？
#map関数を用いて表すと以下
numbers = [1, 2, 3]
new_numbers_map = map(lambda num: num * 3, numbers)
new_numbers = list(new_numbers_map)
print(new_numbers) #出力は[3, 6, 9]

#リスト内表記を用いて表すとスマートに見える。可読性もこっちの方が高いかな？
numbers = [2, 3, 4]
new_numbers = [num * 3 for num in numbers]
print(new_numbers) #出力は[6, 9, 12]

#Exercise
#x_listとy_listという2つのリストを作成する。
# x_listとy_listには、それぞれ変数xとyのインスタンスを10個ずつ含む。
# また、作成した2つのリストを連結して、変数xとyをそれぞれ10回ずつ含むbig_listというリストを作成する。
x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
big_list = x_list + y_list
print(x_list)
print(y_list)
print(big_list)

#リストの作成にはforループを使ってもいいかもしれない
x_list = [x for x in range(10)]
y_list = [10 + y for y in range(10)]
print(x_list)
print(y_list)
