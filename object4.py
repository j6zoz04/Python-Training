#類別(class)、物件(object)

#類別為手機
class Phone:
    def __init__(self,os,number,water):
        self.os=os #手機的作業系統<------屬性1
        self.number=number #手機的型號<--屬性2
        self.water=water #手機是否防水<--屬性3
#建立手機物件
#物件phone1:作業系統為ios、型號為iphone13、防水
phone1=Phone('ios','iphone 13',True)
#物件phone2:作業系統為Android、型號為U11、不防水
phone2=Phone('Android','U11',False)

#phone1、phone2都屬於"手機"類別，但為不同的物件(即使屬性一樣)。

print(phone1.os)
