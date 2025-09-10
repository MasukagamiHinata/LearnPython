#forループ
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


#range関数(ゼロベースなので注意)をつかって以下のようにもできる
#range(start, stop, step)
for x in range(5):
    print(x) #0, 1, 2, 3, 4

for x in range(3, 6): #3~5までの整数を指定。インデックスを指定するわけではないのでコロンではなくカンマ。
    print(x) #3, 4, 5

for x in range(2, 10, 2):
    print(x)


#Whileループ
#特定のブール条件が満たされるまで繰り返される。
count = 0
while count < 5:
    print(count)
    count += 1 #count = count + 1


#break, continueステートメント
count = 0
while True: #条件を満たす(True)処理が無限に繰り返される
    print(count)
    count += 1
    if count >= 5:
        break #上記の条件を満たすと無限ループが終了する
    #output: 0,1,2,3,4 

for x in range(10):
    if x % 2 == 0:
        continue #上記条件を満たす場合は処理を行わず、かつループの先頭に戻る
                 #以降のprintは条件が満たされる場合行わないということ
    print(x)

#無限ループとcontinueとbreakを全部使って以下のようにも書ける
count = 0
while True:
    if count % 2 == 0:
        count += 1
        continue 
    print(count)
    count += 1
    if count >= 10:
        break


#以下のようにループと一緒にelseを使うことができる
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count value reached %d" %count)

for i in range(1, 10):
    if i%5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated \
           because of break but not due to fail in condition")


#Exercise
#Loop through and print out all even numbers from the numbers list in the same order they are received.
#Don't print any numbers that come after 237 in the sequence.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)

#indexを指定するやり方もできる
stop_index = numbers.index(237)
for index, number in enumerate(numbers):
    if index > stop_index:
        break
    if number % 2 == 0:
        print(number)