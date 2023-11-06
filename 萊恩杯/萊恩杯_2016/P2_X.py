# Hans物件，繼承str，並初始化。
class Hans(str):
	def __init__(self, string=""):
		super().__init__()


# 要動態增加的方法
def hans(string):

	h = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
	for i in input():
		string = string.replace(i, h[int(i)])
	return string



Hans.hans = property(hans)
print(Hans("1308792465").hans.upper())



"""
1308792465
"""