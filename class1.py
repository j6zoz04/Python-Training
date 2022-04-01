#定義類別，命名為Test
#變數x與函式say()統稱為Test這個類別的"屬性(Attributes)"
#類別Test，有兩個屬性:x 和 say()
class Test:
    x=3 #定義封裝的變數->類別屬性
    def say(): #定義封裝的函式->類別屬性
        print('Hello')

#使用Test這個類別
Test.x+3 #取得屬性x的資料，然後+3
print(Test.x+3) #3+3=6
Test.say() #呼叫屬性say()函式



    

