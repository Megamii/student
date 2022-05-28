class Student:
    #[assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age,tracks,score):
        # Instance variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
# create first object
s1 = Student("Bob", 26, ["FE","BE"], 20.90)

# instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)
print('tracks:', s1.tracks)
print('score:',s1.score)

# instance variable
s2 =  Student(name="Peter", age=36, tracks="UI/UX", score=21)
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)
print('tracks:', s2.tracks)
print('score:',s2.score)

       
def method(self):
   return 'instance method called', self

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Peter = Student(name="Peter", age=36, tracks="UI/UX", score=21)

class Student:
    
    def __init__(self, name, age,tracks,score):
        # Instance variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


stud = Student("Bob", 26,["FE","BE"], 20.90)

print ('Enter 1. To change students name 2. To change age 3.To add track 4.To get score')
choice = int(input())

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# modify instance variable
stud.name = 'peter'
stud.age = 36

print('After')
print('Name:', stud.name, 'Age:', stud.age)


if choice == 1 :
    print('Enter  a valid name', input())
   
if choice == 2:
    print('Enter a new age:', int(input()))

if choice == 3:
    print('Enter new track:', input())
    
if choice == 4 :
    print('Your score is ', s1.score )

else:
    print('You have made no  valid selection')

