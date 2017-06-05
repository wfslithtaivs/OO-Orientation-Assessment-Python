"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Object-orientation require next 3 things:

    Abstraction - allows to abstract certain logic.

    Incapsulation - allows to abstract complicated object-behaviour.

    Polymorphism - allows using "generally alike" objects similar ways
    without any knowledge of implementation details.

2. What is a class?

    Class in Python is a specific data type that subclasses (by default) Class Object
    and abstract certain behaviour pattern.
    Designed to implement object-oriented concepts.

3. What is an instance attribute?

    Any attribute that might be accessed using following syntax:
        class_instance.attribute_name

    Depends on context might return instance specific value
    or value for higher level class (up to Object) one.

4. What is a method?

    Method is a function belongs to a specific class.

5. What is an instance in object orientation?

    Instance in OO is an object of a specific class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute belongs to class and might be accessed by instances of class.
   Instance attribute belongs to instance of class and can't accessed from class level.

   Usage:
    class attribute count keeps track of number of class instances ever created.

    instance attribute name stores specific name of cat of class Cat.
"""

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Class Student"""

    def __init__(self, fname, lname, address):
        """ Initialises instance attributes"""

        self.first_name = fname
        self.last_name = lname
        self.address = address


class Question(object):
    """ Class Question"""

    def __init__(self, question, answer):
        """Initialises instance attributes"""

        self.question = question
        self.correct_answer = answer


class Exam(object):
    """ Class Exam"""

    def __init__(self, name):
        """Initialises instance attributes"""

        self.name = name
        self.questions = []

    def add_question(self, question):
        """Adds question object to the list of exam questions"""

        self.questions.append(question)

    def administer(self):
        """Run exam"""

        num_right_answers = 0
        total_questions = len(self.questions)

        for i in range(total_questions):
            student_answer = raw_input(self.questions[i].question + " > ")
            if student_answer == self.questions[i].correct_answer:
                num_right_answers += 1

        return (float(num_right_answers)/total_questions) * 100


class Quiz(Exam):
    """Class Quiz"""

    def administer(self):
        """Return pass or fail"""

        res = super(Quiz, self).administer()
        return int(res >= 50)


class StudentExam(object):
    """ Class StudentExam to allow Student to take an Exam and store result"""

    def __init__(self, student, test):
        """Initialises instance attributes"""

        self.student = student
        self.test = test

    def take_test(self):
        """Take exam and store result for student"""

        self.student_score = self.test.administer()


class StudentQuiz(StudentExam):
    """ Class StudentQuiz to allow Student to take a Quiz and store result.
        Same logic, just a different name """


def example():
    """ Creates objects for student and exam and allows student to take exam
        using StudentExam object"""

    # create object of exam class and add questions
    exam = Exam('midterm')
    print "Welcome to %s exam:" % (exam.name)
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    exam.add_question(set_q)
    pwd_q = Question('What does pwd stand for?', 'print working directory')
    exam.add_question(pwd_q)
    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    exam.add_question(list_q)
    # create object of Student class
    student = Student("Kate", "S", "/usr/bin/python")
    # create object of StudentExam class and pass student and exam as a parameters
    student_exam = StudentExam(student, exam)
    student_exam.take_test()
    # print result of taking result by student
    print "Your exam score is", student_exam.student_score

    # Take weekly Quiz
    quiz = Quiz('weekly')
    print "Welcome to %s quiz: " % (quiz.name)
    quiz.add_question(set_q)
    quiz.add_question(pwd_q)
    quiz.add_question(list_q)
    student_quiz = StudentQuiz(student, quiz)
    student_quiz.take_test()
    print "Your quiz score is", student_quiz.student_score

if __name__ == '__main__':
    example()
