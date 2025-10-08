HomeworkDictionary  = {}

HomeworkDictionary = {1: "Banana", 2: "Ball"}


HomeworkDictionary = {'name': 'Umar',1: [2,3,4]}

HomeworkDictionary = {'name': 'Umar', 'age': 26}


print(HomeworkDictionary['name'])
print(HomeworkDictionary.get('age'))

HomeworkDictionary['age'] = 27
print(HomeworkDictionary)

HomeworkDictionary["Address"] = "Lahore"
print(HomeworkDictionary)

HomeworkDictionary.pop('age')
print(HomeworkDictionary)

print("Address", HomeworkDictionary.get("Address"))

HomeworkDictionary.clear()
print(HomeworkDictionary) 