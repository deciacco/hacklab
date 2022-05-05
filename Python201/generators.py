# no return, need to pause execution
def gen_demo():
	n = 1
	yield n

	n += 1
	yield n

	n += 1
	yield n

def xor_static_key(a):
	key = 0x5

	for i in a:
		yield chr(ord(i) ^ key)

generator = gen_demo()

print(next(generator))
print(next(generator))
print(next(generator))

print ("-"*50)

for i in xor_static_key("test"):
	print(i)

print ("-"*50)

xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "test")

for i in xor_static_key2:
	print(i)

# generators good for:
# - reading large files
# - memory intensive processing
# 
# lazy execution, generate items when asked for