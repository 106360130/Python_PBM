
#取出dict中的dict的值
dict_test = {'name': '789', 'scores': {'789': 789.0}}

print(dict_test["name"])
print(dict_test["scores"])
print(dict_test["scores"]["789"])  #取出"dict_test"中的"scores"中的"789"值
#取出dict中的dict的值


#列印出dict中的key有那些
dict_test_2 = {"1" : "Jeff", "2" : "Leo", "3" : "Joy"}

for content in dict_test_2.keys() :
	print(content)
	print(type(content))
#列印出dict中的key有那些
	
	
#列印出dict中的key的值
dict_test_3 = {'name': '789', 'scores': {'789': 789.0, '546' : 85}}

for subject in dict_test_3["scores"].keys() :
	print(subject)
	print(type(subject))
	print(dict_test_3["scores"][subject])
#列印出dict中的key的值
	
	
#列印出list的最後一個值
dict_test_4 = {'name': '789', 'num_list': [1, 5, 86, 8, 6]}
print(dict_test_4["num_list"][-1])
#列印出list的最後一個值
