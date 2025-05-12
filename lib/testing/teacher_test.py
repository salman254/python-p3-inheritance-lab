from lib.teacher import Teacher
from lib.user import User

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        # Use the fully qualified class reference for the test
        assert User in Teacher.__bases__

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("My", "Teacher")
        assert (my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher")

    def test_teach_method(self):
        '''returns a string from the "knowledge" list.'''
        my_teacher = Teacher("My", "Teacher")
        assert my_teacher.teach() in Teacher.knowledge
