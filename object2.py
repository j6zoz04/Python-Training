#Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):#self為固定寫法，x、y為丟進來的參數
        self.x=x #把參數x賦予給屬性(封裝在物件中的變數)x
        self.y=y
        
#建立第一個實體物件 p1
p1=Point(3,4)
#使用實體物件 p1: 實體物件.實體屬性名稱
print(p1.x,p1.y)
#建立第二個實體物件 p2
p2=Point(5,6)
#使用實體物件 p2: 實體物件.實體屬性名稱
print(p2.x,p2.y)