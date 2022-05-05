def print_out(a):
	print("outer: {}".format(a))

	def print_in():
		print("\tinner: {}".format(a))

	return print_in

# 'a' is known to the nested function
# the value of 'a' is also returned/attached to the code
# this technique is known as the closure
test2 = print_out("test")

# the outter function is not needed for the
# nested function to work
del print_out

test2()