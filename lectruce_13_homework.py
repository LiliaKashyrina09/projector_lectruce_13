#Task 1
class Country:
    def add(self, other_country):
        combined_name = self.name + ' ' + other_country.name
        combined_population = self.population + other_country.population
        new_country = Country()
        new_country.name = combined_name
        new_country.population = combined_population
        return new_country

bosnia = Country()
bosnia.name = 'Bosnia'
bosnia.population = 10_000_000

herzegovina = Country()
herzegovina.name = 'Herzegovina'
herzegovina.population = 5_000_000

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population) 
print(bosnia_herzegovina.name)       


#Task 2
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = self.name + ' ' + other_country.name
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)  
print(bosnia_herzegovina.name)        

#Task 3 
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):  
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

try:
    car1 = Car('Tesla', 'X', 2022)
    for i in range(2):
        car1.accelerate()  
    
    for i in range(1):
        car1.brake()  

    current_speed = car1.get_speed()
    
    if current_speed < 0:
        raise ValueError ("Speed should not be negative!")
    else:
        print(f"Car's current speed is: {current_speed}")

except ValueError as e:
    print(e)  


