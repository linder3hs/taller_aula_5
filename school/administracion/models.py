from django.db import models

# Vamos a crear 4 modeles 
# 1: Person
# 2: Student
# 3: Teacher
# 4: ClassRoom

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()


    class Meta:
        abstract = True


class ClassRoom(models.Model):
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self):
        return self.name + " - " + str(self.start_time)

    class Meta:
        db_table = "classrooms"


class Student(Person):
    classroom_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    grade_lab = models.FloatField(default=0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)

    class Meta:
        db_table = "students"


class StudentProxy(Student):
    class Meta:
        ordering = ["first_name", "last_name"]
        proxy = True
    
    def average(self):
        return self.grade_exam * 0.1 + self.grade_lab * 0.6 + self.grade_final * 0.3


class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = "teachers"


class TeacherProxy(Teacher):
    class Meta:
        proxy = True

    def get_bonnus(self):
        return self.salary + self.rating * 100


class Book(models.Model):
    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=400)
    average_rating = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=200)
    language_code = models.CharField(max_length=200)
    num_pages = models.CharField(max_length=200)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=200)

    class Meta:
        db_table = "books"
