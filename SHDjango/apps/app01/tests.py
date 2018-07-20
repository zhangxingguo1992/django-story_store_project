
from functools import wraps
def check_user_login(func):
	@wraps(func)
	def _wrapper(*args, **kwargs):
		print(args)
		request = args[0]
		print(request.name)
		print(kwargs)
		return func(*args, **kwargs)
	return _wrapper

@check_user_login
def test(request):
	print("111111")
	print(request)
	return 1

class Md(object):
	def __init__(self):
		self.name = "aaaa"
		self.address = "bbbb"


if __name__ == "__main__":
	test(Md())
