#定義類別 Test
#
class Test:
    color=['red','blue','yellow','green'] #定義封裝的變數
    def choose_color(cc): #定義封裝的函式
        if cc in Test.color:
            print(cc)
        else:
            print('無此顏色')

#使用類別 Test 中的 choose_color(cc) 屬性
print(Test.choose_color('black'))
#print(Test.choose_color('blue')) 