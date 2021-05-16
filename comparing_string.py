"""
Reference :
https://dotblogs.com.tw/Eyelash/2020/05/29/175046
"""

#比較字串
dict = {
"status" : "OK",
"status_2" : "Cool"
}

print(dict["status"])

if dict["status"] == "OK" :
	print("True")

if dict["status"] is "OK" :
	print("True")

if dict["status_2"] == "OK" :
	print("True_2")
#比較字串

#"==" 和 "is"的差別
#"==" 和 "!="為一組；"is" 和 "is not"為一組
#"=="是比較變數的"值"，而"is"是比較"記憶體位址"
a = ["eyelash","test"] #定義一個陣列
c = ["eyelash","test"] #定義相同內容的陣列

print(a == c) # 結果會是True，因為"值"都相同
print(a is c) # 結果會是False，因為"記憶體位址"不一樣

a = ["eyelash","test"] # 與第二個範例相同
c = ["eyelash","test"] # 與第二個範例相同

print(f"a[0] is c[0] => [{a is c}]") # 結果是： a[0] is c[0] => [False] 
print(f"a[0] is c[0] => [{a[0] is c[0]}]") # 結果是： a[0] is c[0] => [True] 

print(id(a)) 
print(id(c))
print(a is c) # 結果是：False，因為"a"和"c"的記憶體位置不一樣

print(id(a[0])) 
print(id(c[0]))
print(a[0] is c[0]) # 結果是：True，因為"a[0]"和"c[0]"的記憶體位置不一樣

print(id("eyelash"))  #記憶體位址與"a[0]"、"c[0]"一樣，因為要節省記憶體空間，所以都導向相同的記憶體位址
print(a[0] is "eyelash") # 結果是：True
print(c[0] is "eyelash") # 結果是：True
#"==" 和 "is"的差別







