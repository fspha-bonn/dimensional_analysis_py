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

# Interpreter

The interpreter has one function and 3 wrapper functions. It imports the `parser`, the `engine` and `numpy`.

**1) get_powers(variable_objects, target_object)**\
The `get_powers` function calculates the powers of how to combine a list of `Variable` objects into an object with provided target units as a `TargetUnit` object. It returns a list of floating point numbers where the nth object in that list is the power of the nth variable.

*Arguments*:
- `variable_objects`: list or iterable of `parser.Variable` objects.
- `target_object`: a ``get_var_obj(eq_string)`parser.TagetUnit` object.

*Returns*
- `powers`: `numpy.array` of floats, length 7.

**2) Wrapper functions**

For convenience the Interpreter wraps functions from the parser and engine.

|           Name           | Wrapped Function |
|--------------------------|------------------|
| `get_var_obj(eq_string)` | `parser.get_var(eq_string)`
| `get_units_obj(unit_str)`| `parser.get_units(unit_str)`
| `calculate(base, target)`| `engine.analyze(base, target)` 
