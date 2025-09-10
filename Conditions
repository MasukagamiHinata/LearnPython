#Pythonは条件を評価するためにブール論理を用いる
x = 2
print(x == 2) #True
print(x == 3) #False
print(2 < 3) #True
print(2 != 3) #True


#ブール演算・if文
name = "John"
age = 23
if name == "John" and age == 23:
    print("John is 23 years old")

if name == "John" or name == "Rick":
    print("eithe John or Rick")


#in演算子
#リストなどのイテラブルなオブジェクト・コンテナ内に指定されたオブジェクトが存在するかどうかチェック可能
name = "John"
if name in ["John", "Rick"]:
    print("either John or Rick")

#elifによって条件分岐を足すこともできる
x = 1
y = 1
if x == 2:
    print("x is 2") #xが2ならばこの文が出力される
elif y == 2:
    print("x isn't 2 but y is 2") #xが2ではなく、yが2ならばこの文が出力される
else:
    print("x and y aren't 2") #x, yともに2でなければこの文が出力される。


#is演算子
#数値や変数ではなくインスタンスそのものにマッチする。
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) #true
print(x is y) #false

x_str = "aaa"
y_str = "aaa"
print(x_str is y_str) #true

#notも使える
print(not False) #true
print((not False == False)) #False


#Exercise
#Change the variables in the first section, so that each if statement resolves as True.
number = 16
second_number = 10
first_array = [0, 1]
second_array = [1,2,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 3:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if second_array and second_array[0] == 1: #second_arrayが1(True)かつsecond_array[0]が1ならば
    print("5") 
    #Pythonにおいて、if文の条件で非ゼロの数値はTrueと評価される。

if not second_number == 5: 
    print("6")
