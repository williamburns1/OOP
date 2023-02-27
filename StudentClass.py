cfrom datetime import date


class Student:
    def __init__(self, id, n, dob, c):
        self.id = id
        self.name = n
        self.dob = dob
        self.classification = c
        self.age = 0
        self.registration = ''

    def get_age(self):
        self.age = date.today().year - int(self.dob.split(sep='/')[2])
        return self.age

    def get_registration(self):
        if self.classification == 'Freshman':
            self.registration = '4/1 thru'
        elif self.classification == 'Sophomore':
            self.registration = '4/4 thru 4/6'
        elif self.classification == 'Junior':
            self.registration = '4/7 thru 4/9'
        elif self.classification == 'Senior':
            self.registration = '4/10 thru 4/12'
        else:
            self.registration = 'classification not found'
        return self.registration
