import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-academic-record" in j:
            exec("".join(i['source']))


class TestAcademicRecord(unittest.TestCase):
  
  def test_class_init(self):
    myRec = StudentRecord(firstName="Dusty", 
      lastName="White", 
      address="6708 Pine St", 
      dob="1/15/1987", 
      hsName="Interlake High School", 
      hsCity="Bellevue", 
      hsState="WA", 
      degree="Econ")

    self.assertTrue(myRec.firstName=="Dusty" and myRec.lastName=="White" and myRec.address=="6708 Pine St" and
      myRec.dob=="1/15/1987" and myRec.hsName=="Interlake High School" and myRec.hsCity=="Bellevue" and 
      myRec.hsState=="WA" and myRec.degree=="Econ", "Your class does not store information correctly.")

  def test_new_class_func(self):
    myRec = StudentRecord(firstName="Dusty", 
      lastName="White", 
      address="6708 Pine St", 
      dob="1/15/1987", 
      hsName="Interlake High School", 
      hsCity="Bellevue", 
      hsState="WA", 
      degree="Econ")

    myRec.newCourse("econ1", 2019, 1, 3, 4)
    myRec.newCourse("econ2", 2019, 1, 3, 3.7)
    myRec.newCourse("acct1", 2019, 2, 3, 3)
    myRec.newCourse("golf", 2019, 1, 1, 4)

    lenBefore = len(myRec.transcript)

    myRec.newCourse("golf2", 2019, 1, 1, 4)

    lenAfter = len(myRec.transcript)

    self.assertTrue(lenAfter-lenBefore==1, "Your class was unable to add a new course to the transcript.")

  def test_credit_count(self):
    myRec = StudentRecord(firstName="Dusty", 
      lastName="White", 
      address="6708 Pine St", 
      dob="1/15/1987", 
      hsName="Interlake High School", 
      hsCity="Bellevue", 
      hsState="WA", 
      degree="Econ")

    myRec.newCourse("econ1", 2019, 1, 3, 4)
    myRec.newCourse("econ2", 2019, 1, 3, 3.7)
    myRec.newCourse("acct1", 2019, 2, 3, 3)
    myRec.newCourse("golf", 2019, 1, 1, 4)

    self.assertTrue(myRec.credits()==10, "Your class did not correctly calculate total credit hours.")

  def test_gpa_calc(self):
    myRec = StudentRecord(firstName="Dusty", 
      lastName="White", 
      address="6708 Pine St", 
      dob="1/15/1987", 
      hsName="Interlake High School", 
      hsCity="Bellevue", 
      hsState="WA", 
      degree="Econ")

    myRec.newCourse("econ1", 2019, 1, 3, 4)
    myRec.newCourse("econ2", 2019, 1, 3, 3.7)
    myRec.newCourse("acct1", 2019, 2, 3, 3)
    myRec.newCourse("golf", 2019, 1, 1, 4)

    self.assertTrue(round(myRec.cumGPA(), 2)==3.61, "Your class did not correctly calculate cumulative GPA.")

  def test_scholarship_func(self):
    myRec = StudentRecord(firstName="Dusty", 
      lastName="White", 
      address="6708 Pine St", 
      dob="1/15/1987", 
      hsName="Interlake High School", 
      hsCity="Bellevue", 
      hsState="WA", 
      degree="Econ")

    myRec.newCourse("econ1", 2019, 1, 3, 4)
    myRec.newCourse("econ2", 2019, 1, 3, 3.7)
    myRec.newCourse("acct1", 2019, 2, 3, 3)
    myRec.newCourse("golf", 2019, 1, 1, 4)

    self.assertTrue(myRec.scholarship()=='Quarter-tuition', "Your class did not correctly determine the scholarship level for this test student.")