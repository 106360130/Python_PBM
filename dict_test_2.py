#可以將輸入的變數變成dict中的key
name = input("Name : ")
stu_list = {}
stu_list["name"] = name
stu_list["scores"] = {}


subject = input("subject : ")
score = input("score : ")
#stu_list[subject] = score


stu_list["scores"][subject] = score

print(stu_list)
stu_list = {}
print(stu_list)
#可以將輸入的變數變成dict中的key