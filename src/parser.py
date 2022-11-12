import numpy as np


def get_dimensions():
    """
    Hard coded function that fetches the dict from dimensions.json and converts to numpy arrays.
    Returns dict
    """

    import json
    with open("dimensions.json") as file:
        unit_vecs = json.load(file)

    #print(json.dumps(unit_vecs, indent = 2))

    for dim in unit_vecs:
        unit_vecs[dim] = np.array(unit_vecs[dim])
        #print(f"{dim}:\t{unit_vecs[dim]}")

    return unit_vecs

unit_mapping = get_dimensions()

###########
#  LEXER  #
###########

WORD, NUM, POW, LPAREN, RPAREN, EQ = ("word", "num", "pow", "lparen", "rparen", "eq")
word_allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
whitespace = " *\t"

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, \"{self.value}\")"

    def __repr__(self):
        return self.__str__()

class Lexer(object):

    def __init__(self, string):
        self.string = string

    def __is_num__(self, i):
        return self.string[i].isnumeric() or self.string[i] in ",."

    def get_num(self, i):
        string = self.string
        val = ""

        if string[i] in  "+-":
            val += string[i]
            i += 1

        while i<len(string) and self.__is_num__(i):
            val += string[i]
            i += 1

        val.replace(",", ".")
        return float(val), i

    def get_word(self, i):
        val = ""
        while i<len(self.string) and self.string[i] in word_allowed:
            val += self.string[i]
            i+=1

        return val, i

    def tokenize(self):
        string = self.string
        tokens = list()

        i = 0
        while i < len(string):

            if self.__is_num__(i) or string[i] in "+-":
                val, i = self.get_num(i)
                tokens.append(Token(NUM, val))

            elif string[i] == "^":
                tokens.append(Token(POW, "^"))
                i += 1

            elif string[i] == "=":
                tokens.append(Token(EQ, "="))
                i += 1

            elif string[i] == "(":
                tokens.append(Token(LPAREN, "("))
                i += 1

            elif string[i] == ")":
                tokens.append(Token(RPAREN, ")"))
                i += 1

            elif string[i] in word_allowed:
                val, i = self.get_word(i)
                tokens.append(Token(WORD, val))

            elif string[i] in whitespace:
                i+=1

            else:
                raise Error(f"Unexpected character at {i}: {string[i]}")

        return tokens

############
#  Parser  #
############

class Unit:
    def __init__(self, unit, power):
        self.unit = unit
        self.power = power

    def __str__(self):
        return f"{self.unit}^({self.power})"

    def __repr__(self):
        return self.__str__()

class TargetUnits:
    def __init__(self, units):
        self.units = units

    def get_unit_vector(self):
        global unit_mapping
        vector = np.zeros(7)

        for unit in self.units:
            if unit.unit not in unit_mapping:
                raise ValueError(f"Unknown unit {unit}")

            #print(unit_mapping[unit.unit])
            vector += unit.power*unit_mapping[unit.unit]

        return vector

    def __str__(self):
        return f"Units: {self.units}"

    def __repr__(self):
        return self.__str__()

class Variable:
    def __init__(self, name, value, units):
        self.name = name
        self.value = value
        self.units = units

    def __str__(self):
        return f"Var: {self.name} = {self.value} * {self.units}"

    def __repr__(self):
        return self.__str__()

    def get_unit_vector(self):
        global unit_mapping
        vector = np.zeros(7)

        for unit in self.units:
            if unit.unit not in unit_mapping:
                raise ValueError(f"Unknown unit {unit}")

            vector += unit.power*unit_mapping[unit.unit]

        return vector

class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0
        self.current_token = tokens[self.i]

    def next_token(self):
        self.i += 1
        if self.i >= len(self.tokens):
            return

        self.current_token = self.tokens[self.i]

    def error(self, expected, got):
        raise Exception(f'Invalid syntax. Expected {expected}, but got {got}.')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.

        if self.current_token.type == token_type:
            self.next_token()
        else:
            self.error(token_type, self.current_token.type)

    def equation(self):
        """
        equation: WORD EQ NUM* term
        """
        name = self.current_token.value
        self.eat(WORD)
        self.eat(EQ)

        if self.current_token.type == NUM:
            value = self.current_token.value
            self.eat(NUM)
        else:
            value = 1.0

        units = self.term()
        return Variable(name, value, units)

    def term(self):
        """
        term: unit term*

        returns list of units
        """

        unit = self.unit()
        if self.i >= len(self.tokens):
            return [unit]
        else:
            return [unit] + self.term()

    def unit(self):
        """
        unit: WORD (POW (LPAREN NUM RPAREN | NUM))*
        """
        unit = self.current_token.value
        self.eat(WORD)

        if self.current_token.type == POW:
            self.eat(POW)

            if self.current_token.type == NUM:
                power = self.current_token.value
                self.eat(NUM)
            else:
                self.eat(LPAREN)
                power = self.current_token.value
                self.eat(NUM)
                self.eat(RPAREN)
        else:
            power = 1.0

        return Unit(unit, power)

    def parse_eq(self):
        return self.equation()

    def parse_units(self):
        return TargetUnits(self.term())


def get_var(arg):
    lexer = Lexer(arg)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse_eq()

def get_units(arg):
    lexer = Lexer(arg)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse_units()
