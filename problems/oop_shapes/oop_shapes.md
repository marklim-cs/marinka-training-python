# OOP task: Shapes

- Create a base class `Shape` with the following methods:
  - `area` - returns shape area
  - `center` - returns a tuple `(x, y)` with the coordinates of the center of the shape ([the center of mass](https://en.wikipedia.org/wiki/Center_of_mass))
  - `name` - returns the name of the shape
  - `__str__` - returns a string with the name of the shape and its parameters, and also the area and center of the shape

- Create the following classes that inherit from `Shape`:
  - `Circle` with a constructor that receives `center` and `radius`
  - `Triangle` with a constructor that receives three vertices `a`, `b` and `c`
  - `Rectangle` with a constructor that receives `top`, `left`, `width` and `height`
  - `Line` with a constructor that receives two endpoints `a` and `b`

Implement all base class's methods for each of the inherited classes.
Methods in the `Shape` class itself should raise `NotImplementedError` because the base class is abstract and should not be used directly.
