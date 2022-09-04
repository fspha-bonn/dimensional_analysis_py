import parser, engine, numpy as np

def log(string):
    print(string)

def get_powers(variable_objects, goal_object):

    print(f"Variables given: {len(variable_objects)}")

    if len(variable_objects) > 7:
        log("Too many strings, aborting")
        raise Error("To many strings.")

    vectors = list()
    for variable in variable_objects:
        vectors.append(variable.get_unit_vector())

    if len(variable_objects) < 7:
        log("Too few strings, padding with identity matrix...")
        #vectors += [[0]*7]*(7-len(variable_objects))
        pad = np.identity(7)[len(variable_objects):,:]
        print(f"padding: {pad}")
        vectors = np.concatenate((vectors, pad), axis = 0)

    print(vectors)
    goal = goal_object.get_unit_vector()
    print(goal)

    return engine.analyze(vectors, goal)

def get_var_obj(eq_string):
    return parser.get_var(eq_string)

def get_units_obj(unit_str):
    return parser.get_units(unit_str)

def calculate(base, goal):
    return engine.analyze(base, goal)
