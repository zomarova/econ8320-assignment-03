import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-complex-number" in j:
            exec("".join(i['source']))


class TestComplexNumber(unittest.TestCase):
  
  def test_class_init(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    self.assertTrue(a.real == 1 and a.imag == 3 and b.real==-2 and b.imag==4, "Your class does not seem to store the real/imaginary components of a complex number correctly.")

  def test_add(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    c = a+b
    self.assertTrue(c.real==-1 and c.imag==7, "Your addition method does not function properly.")

  def test_complex_conjugate(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    c = a.conjugate()
    self.assertTrue(c.real==1 and c.imag==-3, "Your class does not correctly calculate complex conjugates.")

  def test_subtract(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    c = a-b
    self.assertTrue(c.real==3 and c.imag==-1, "Your subtraction method does not work correctly.")

  def test_multiply(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    c = a*b
    self.assertTrue(c.real==-14 and c.imag==-2, "Your multiplication method does not work correctly.")

  def test_divide(self):
    a = ComplexNumber(1, 3)
    b = ComplexNumber(-2, 4)

    c = a/b
    self.assertTrue(c.real==0.5 and c.imag==-0.5, "Your division method does not work correctly.")