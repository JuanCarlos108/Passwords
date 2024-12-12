import random as r , string as s

elements = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.punctuation + s.digits

password = ""

longitud = int(input("¿Que tan larga sera la variable?"))
for i in range (longitud):
    password += r.choice(elements)
print(password)
