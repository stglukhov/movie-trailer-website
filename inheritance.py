class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructor"
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last Name - " + self.last_name)
        print ("Eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print ("Last Name - " + self.last_name)
        print ("Eye color - " + self.eye_color)
        print "Number of toys - " + str(self.number_of_toys)

billy=Parent("cyrus","blue")
miley = Child("Cyrus", "Blue", 5)
#print (billy.last_name)
#print (miley.last_name)
#print (miley.number_of_toys)
billy.show_info()
miley.show_info()
