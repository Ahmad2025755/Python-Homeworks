class Introduction:

  species = "Ahmad"


  def __init__(self , name , age):
  
    self.name = name
    self.age = age


Ahmad = Introduction("Ahmad", "11")

print("My name is {} and I am {} years old".format(Ahmad.name, Ahmad.age))