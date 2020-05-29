class1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class1+class2

new_class.append('Peter Warden')

print(new_class)

courses = { 'Math':65,'English':70,'History':80,'French':70,'Science':60 }
total = 0
for x in courses:
    total = total + courses[x]

percentage = (total/500)*100
print(percentage)

mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Bengio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

topper = max(mathematics,key = mathematics.get)
print(topper)

first_name, last_name = topper.split(" ",2)

full_name = last_name+" "+first_name

certificate_name = full_name.upper()
print(certificate_name)
