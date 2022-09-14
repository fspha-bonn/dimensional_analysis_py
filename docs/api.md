# Dimensional Analysis API

The api for using Dimensional analysis comes in three parts: The parser, the interpreter and the engine. This documentation provides instructions on how to use every part of the API.

## Parser

The parser converts an input-string into a usable Variable or Unit object.

The parser has two fuctions

**1) get_var(string_input)**\
The function `get_var(string_input)` returns a `Variable(obj)` object.

The input-string must be of the format

```
name = [value][unit 1]^[power]*[unit_2]^power*...
```

If the power is one it can be omitted. If a power is given the seperator by * or by a whitespace can be omitted.

**2) get_unit(string_input)**\
The function `get_uni(string_input)` returns a `TargetUnit(obj)` object.

The input-string must be of the format

```
[unit 1]^[power]*[unit_2]^power*...
```

If the power is one it can be omitted. If a power is given the seperator by * or by a whitespace can be omitted.


**Variable(obj)**\
The `Variable` object has three properties: `name`, `value` & `unit`.

- `name` (`str`) is the provided string for the variable.
- `value` (`float`) is the provided floating point number for the value of that variable.

- `units` is a list of `Unit` objects.

The `Variable(obj)` class has the following functions:

|      name       |  arguments | description
|-----------------|------------|------------
| get_unit_vector |    self    | returns vector as `numpy.array` in unit space
|    \_\_str__    |    self    | Returns String representation of Object. Equivalent to \_\_repr__.

**TargetUnit(obj)**\
The `TargetUnit` object has one property: `unit`.

- `units` is a list of `Unit` objects.

The `TargetUnit(obj)` class has the following functions:

|      name       |  arguments | description
|-----------------|------------|------------
| get_unit_vector |    self    | returns vector as `numpy.array` in unit space
|    \_\_str__    |    self    | Returns String representation of Object. Equivalent to \_\_repr__.

**Unit(obj)**\
The `Unit` object has two properties: `unit` & `power`.

- `unit` is the string representing the name of the unit.
- `power` is the float provided as the power of that unit in the string, or the coordinate of that vector in unit space.

The `Unit(obj)` class has the following functions:

|      name       |  arguments | description
|-----------------|------------|------------
|    \_\_str__    |    self    | Returns String representation of Object. Equivalent to \_\_repr__.
