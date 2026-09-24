a=int(input("balingizni kiriting >>> "))
if a>60 and a<100:
   print("Tabriklaymiz siz imtihondan otgansiz")
elif a<60 and a>0 :
    print("siz yiqilgansiz keyingi o'tishingizga tilakdoshmiz")
elif a<0  or a>100  :
    print("xato bal")