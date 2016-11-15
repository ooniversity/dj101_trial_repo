from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from courses.models import Course, Lesson
from .models import Student
from coaches.models import Coach


def add_student():
    coach1=Coach.objects.create(
        user=User.objects.create(),
        date_of_birth='1980-01-01',
        gender='F',
        phone='0-800-345-657-765',
        address='City',
        skype='SomeSkype',
        description='somedescription') 
    course1 = Course.objects.create(
        name='SomeCourse',
        short_description='SomeDescription',
        description='SomeBigDescription',
        coach=coach1,
        assistant=coach1)
    course2 = Course.objects.create(
        name='SomeCourse2',
        short_description='SomeDescription2',
        description='SomeBigDescription2',
        coach=coach1,
        assistant=coach1)
    student1 = Student.objects.create(
        name = 'student1',
        surname = 'st1',
        date_of_birth = '1982-09-09',
        email = 'st1@st.com',
        phone = '0-800-900-500-67',
        address = 'City',
        skype = 'stskype1')
    student1.courses.add(course1)
    student2 = Student.objects.create(
        name = 'student2',
        surname = 'st2',
        date_of_birth = '1982-02-09',
        email = 'st2@st.com',
        phone = '0-800-900-510-67',
        address = 'City2',
        skype = 'stskype2')
    student2.courses.add(course2)

class StudentsListTest(TestCase):
    
    def test_student_valid_links(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
    def test_student_list_code0(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_student_list_number0(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 0) 
    def test_student_list_codenot0(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_student_list_numbernot0(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertEqual(Student.objects.all().count(), 2)
    def test_student_list_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/')
        self.assertTemplateUsed(response, 'students/student_list.html')
    def test_valid_student_name_edit(self):
        client = Client()
        add_student()
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'student1')
    def test_student_title(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertContains(response, 'PyStudents')     
        
    #def test_student_edit(self):
       # client = Client()
        #add_student
        #response = self.client.post('/students/edit/1/', {'name': 'St1_1', 'surname': 'St_11', 'date_of_birth': '1905-05-05', 'email': 'dyt@dyt.com', 'phone': '09-09-09', 'address': 'Somecity', 'skype': 'skype'})
        #response = self.client.get('/students/1/')
        
        #self.assertEqual(response.status_code, 302)
       # self.assertContains(response, student1)
		
class StudentsDetailTest(TestCase):
    def test_student_valid_links2(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
    def test_detail_name(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'student1')  
    def test_detail_surname(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'st1') 
    def test_detail_address(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'City')
    def test_detail_skype(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        
        self.assertContains(response, 'stskype1') 
    def test_student_detail_template(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        self.assertTemplateUsed(response, 'students/student_detail.html')
    def test_detail_phone(self):
        client = Client()
        add_student()
        response = self.client.get('/students/1/')   
        self.assertContains(response, '0-800-900-500-67') 
# Create your tests here.
