#Creating a class named Person
class Person:
    #Assigning values to object properties 
    def __init__(self, name, age, gender, interests):
        self.name       = name
        self.age        = age
        self.gender     = gender
        self.interests  = ' , '.join(interests)
    #Creating an object hello
    def hello(self):
      # print 'Hello, my name is' , self.name, 'and i am',  self.age, 'years old. My interests are',  self.interests
        # return f'Hello, my name is {self.name}, and i am {self.age} years old. My interests are:' self.interests
        return 'Hello, my name is {} and I am {} years old. My interests are {}'.format(self.name,self.age,self.interests)

person1 = Person("Ryan" , 30 ,"male",["being a hardarse", "agile," , "ssd hard drive."])
greeting = person1.hello()
print(greeting)
