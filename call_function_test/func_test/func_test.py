import os
#查看當前路徑
print(os.path.abspath(os.path.dirname(__file__)))

#查看上級路徑
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

def func_1() :
	print("func_1")
