import pytest
# print(os.curdir)
# from calculator import subtract
from calculator import *
class TestCalculator:
	# Addition tests
	def test_add_str(self):
		assert add("2","3") == 5

	def test_add_int(self):
		assert add(2,3) == 5 

	def test_add_float(self):
		assert add(2,3.01) == 5.01 

	# Subtraction tests
	def test_sub_str(self):
		assert subtract("2","3") == -1

	def test_sub_int(self):
		assert subtract(12,3) == 9 

	def test_sub_float(self):
		assert subtract(122,3.01) == 118.99 

	# Multiplication
	def test_mul_str(self):
		assert multiply("2","-3") == -6

	def test_mult_int(self):
		assert multiply(12,3) == 36

	def test_mult_float(self):
		assert multiply(12,3.01) == 36.12

	# Division
	def test_div_str(self):
		assert divide("3","-2") == -1.5

	def test_div_int(self):
		assert divide(12,3) == 4

	def test_div_float(self):
		assert divide(12,3.01) == 3.98671096345515
	
	def test_div_byZero(self):
		with pytest.raises(ZeroDivisionError):
			divide(1,0)

	# Integer Division
	def test_intdiv_str(self):
		quotient, remainder = divide_integer("3","2")
		assert quotient == 1
		assert remainder == 1

	def test_intdiv_int(self):
		quotient, remainder = divide_integer(12,3)
		assert quotient == 4
		assert remainder == 0

	def test_intdiv_float(self):
		with pytest.raises(TypeError):
			divide_integer(14.5, 3.5)

	# def test_div_byZero(self):
	# 	with pytest.raises(not ZeroDivisionError):
	# 		divide(1,0)
		


	