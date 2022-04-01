#FullName 實體物件的設計: 分開紀錄姓(last name)、名(first name)資料的全名
#類別 : 全名(FullName)
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
#物件 : name1
name1=FullName('DENG-HUEI','LIAN')
print(name1.first,name1.last)

#物件 : name2
name2=FullName('JOHNSON','KL')
print(name2.first,name2.last)
