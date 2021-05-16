"""
參考資料
https://blog.csdn.net/leorx01/article/details/71141643
"""
#呼叫不同資料夾中的function

#查看當前路徑
import os
func_test_path = os.path.abspath(os.path.dirname(__file__))
print("type(func_test_path) : {}".format(type(func_test_path)))
print("1 : {}".format(func_test_path))
print("1 : {}".format(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))
print("1 : {}".format(os.path.abspath(os.path.join(os.getcwd(), "."))))

#查看上級路徑
print("2 : {}".format(os.path.abspath(os.path.join(os.getcwd(), ".."))))

#查看上上級路徑
print("3 : {}".format(os.path.abspath(os.path.join(os.getcwd(), "../.."))))

##查看上上上級路徑
print("4 : {}".format(os.path.abspath(os.path.join(os.getcwd(), "../../.."))))

#當前路徑 + "指定路徑"
func_test_path = os.path.join(func_test_path, "func_test")
print("5 : {}".format(func_test_path))

#將function的路徑增加到"sys.path"中
import sys
sys.path.append(func_test_path)
#print(sys.path)

#就可以使用其他資料夾中的function
#且是用"相對路經"的方式
from func_test import func_1
func_1()



