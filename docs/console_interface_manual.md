# Console Interface

The console interface provides a simple and local way to interact with the api. For this manual I will assume python 3.x can be called with `python3`.

## Dependencies

Dependencies show latest tested version. Script may work with older versions, but they are untested.

| Library | Version
|---------|---------
| numpy   | >= 1.22.3

## Using the console interface

### Starting the script

To start the script open your console or terminal and navigate to the src folder of the python application.

```
> python3 console_interface.py
Starting...
Please enter you variables in the following format:
<name> = <amount> [units]
Example: p = 12 kg m^-1 s^(-2)
Please make sure to use SI base units.
```

### Setting the base vectors
Now you will be asked to put in up to 7 variables. For example:

```
Variable 1: x = 2m
Variable 2: v = 3m*s^-1
Variable 3:
```

If you leave a variable empty that and all following variables will be skipped.

The variables must have the syntax of

```
[name] = [value][unit 1]^[power]*[unit_2]^[power]*...
```
If the power is one it can be omitted. If a power is given the separator by * or by a whitespace can be omitted.

Make sure to use only SI-Base units:
`s`,`m`,`kg`,`A`,`K`, `mol` & `cd`

### Setting the target vector
When you have set the variables you will need to enter the target units. For example:

```
Units for target: s^1
```

As with the variables the units must follow the format:
```
[unit 1]^[power]*[unit_2]^[power]*...
```
If the power is one it can be omitted. If a power is given the separator by * or by a whitespace can be omitted.

Make sure to use only SI-Base units:
`s`,`m`,`kg`,`A`,`K`, `mol` & `cd`

### Output
The script will guess a solution to the problem using dimensional analysis, display that solution and calculate the target variable using the provided variables.

```
Variables given: 2
Too few strings, padding with identity matrix...
target = x^(1.0) * v^(-1.0) = 0.6666666666666666s
```
