#實體物件的建立與使用
class Point:
    #定義初始化函式
    def __init__(self):
        self.x=3 #實體屬性
        self.y=4 #實體屬性
    #注意 : 實體屬性與類別屬性為不同概念
    #建立實體物件
    #此實體物件包含 x 和 y 兩種屬性

#建立實體物件，放入變數obj中
obj=Point()
print(obj.x) 