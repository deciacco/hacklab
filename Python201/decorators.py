from datetime import datetime
import time

def decorator_function(func): #the decorating function
	def wrapper(*args, **kwargs):

		#decorate or do something before the function
		print("-"*50)
		print("> Exec Started {}".format(datetime.today().strftime("%Y.%m.%d_%H:%M:%S")))
		
		#actual funtion we might already have
		func(*args, **kwargs)

		#decorate, or do something after the function 
		print("> Exec Started {}".format(datetime.today().strftime("%Y.%m.%d_%H:%M:%S")))
		print("-"*50)
	return wrapper

@decorator_function #decorate the actual_function with the decorator
def actual_function(sleep_time):
	print("sleeping for %s secs" % (sleep_time))
	time.sleep(sleep_time)

#definitions done, let's call it
actual_function(3)