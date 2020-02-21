class Person:
    def __init__(self, name, age, gender, interests):
        self.name       = name
        self.age        = age
        self.gender     = gender
        self.interests  = interests

    def hello(self):
        list        = ' , '.join(self.interests)
        print 'Hello, my name is' , self.name, 'and i am',  self.age, 'years old. My interests are',  list



person1 = Person("Ryan" , 30 ,"male",["being a hardarse", "agile," + " and " "ssd hard drive."])
greeting = person1.hello()
print(greeting)
