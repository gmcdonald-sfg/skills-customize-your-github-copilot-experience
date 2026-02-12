# 📘 Assignment: Python Classes

## 🎯 Objective

Learn how to define and use classes in Python to model real-world objects and behaviors.

## 📝 Tasks

### 🛠️ Define a Simple Class

#### Description
Create a class named `Car` that represents a car with attributes for make, model, and year. Add a method to display information about the car.

#### Requirements
Completed program should:

- Define a class `Car` with `make`, `model`, and `year` attributes
- Include a method `display_info()` that prints the car's details
- Create an instance of `Car` and call `display_info()`

#### Example Input
```python
# Create a Car instance
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
```

#### Example Output
```
2020 Toyota Camry
```


### 🛠️ Add Methods and Interactions

#### Description
Expand the `Car` class to include a method to update the car's mileage and another to display the current mileage.

#### Requirements
Completed program should:

- Add a `mileage` attribute to the `Car` class (default 0)
- Add a method `update_mileage(new_mileage)` to update the mileage
- Add a method `display_mileage()` to print the current mileage
- Demonstrate updating and displaying mileage for a `Car` instance

#### Example Input
```python
my_car = Car("Honda", "Civic", 2021)
my_car.update_mileage(15000)
my_car.display_mileage()
```

#### Example Output
```
Current mileage: 15000 miles
```
