#代入する値自体にシングルクォートが含まれているなら、それを囲むのはダブルクォートでないといけない
astring = "hello world"
print("single quotes are '' ") #output: single quotes are ''
print(len(astring)) #output: 11  スペースも文字列の要素に含まれる


#メソッド"index"は一番初めに出てくる文字しか認識しない
astring = "hello world"
print(astring.index("o")) 

#output: 4 
# 一番初めに出てくる"o"の、最初の文字からの距離が4文字ということ


#メソッド"count"。要素を数え上げる
astring = "hello world"
print(astring.count("l"))

#output: 3
# astring中に含まれる要素"l"が3つあるということ


#スライス
astring = "hello world"
print(astring[3:7])

#output: lo w
#３～６番目の文字が帰ってくる。ほとんどのプログラミング言語がこの仕様。

#"it makes doing math inside those brackets easier."とは？なぜeasierなのかあまり想像がつかない
#文字と文字の間の見えない仕切りに番号が割り振られていて、仕切りの右側が番号で指定されているイメージを持った。
#そういえばテキストを打ち込むときのカーソルも文字自体ではなくて文字と文字の間に位置しているよね。
#あるいは左クリック長押しで範囲指定する時のイメージ。


#If you just have one number in the brackets, 
# it will give you the single character at that index. 
astring = "hello world"
print(astring[3]) 

#output: l


#If you leave out the first number but keep the colon, 
# it will give you a slice from the start to the number you left in. 
astring = "hello world"
print(astring[3:]) 

#output: lo world


#If you leave out the second number,
# it will give you a slice from the first number to the end.
astring = "hello world"
print(astring[:7]) 

#output: hello w


#負の数をブラケットの中に入れることもできる。最後からn番目という感じ。
astring = "hello world"
print(astring[-3]) #output: r
print(astring[-1]) #output: d
print(astring[-0]) #output: h
print(astring[0])  #output: h

#仕切りの右側が指定されている(イメージ)ので[-1]は"d"。


#さらにコロンを付加(:step)することでstep段飛ばしをすることも可能
astring = "hello world"
print(astring[2:7:2]) #output: low 2の要素l、4の要素o、6の要素w

#"The general form is [start:stop:step]."


#strrev関数と同様の働き(文字列反転)ができる構文
astring = "hello world"
print(astring[::-1]) #output: dlrow olleh

#strrevはPythonには組み込まれてないがreversed()なら可能か


#大文字にしたり小文字にしたりするメソッドもある
astring = "hello world"
print(astring.upper()) #ooutput: HELLO WORLD
print(astring.lower()) #output: hello world


#文字列が何で終わっているか、何で始まっているかを判定するメソッドも
astring = "hello world"
print(astring.startswith("hello")) #True
print(astring.endswith("aa")) #False


#文字列をリストに分割することもできる
astring = "Hello world!"
afewwords = astring.split(" ") #スペースで分割
print(afewwords) #output: ['hello', 'world']



#Exercise
#文字列を変更して、正しい情報を出力するようにコードを修正してみてください。
s = "Strithera wat kkkome"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))   

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

#力技でどうにかした感。なんのExerciseなのかわかんなかった
