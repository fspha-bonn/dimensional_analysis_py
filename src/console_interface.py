def main():
    print("Starting...")
    import interpreter as intprt

    vars = list()
    i = 0
    print("Please enter you variables in the following format:")
    print("<name> = <amount> [units]")
    print("Example: p = 12 kg m^-1 s^(-2)")
    print("Please make sure to use SI base units.\n")
    while i < 7:
        in_str = input(f"Variable {i+1}: ")
        if in_str == "":
            break

        vars.append(intprt.get_var_obj(in_str))
        i+=1

    l = len(vars)
    print("\nPlease enter the desired output units. For Example: kg m^-1 s^(-2)")
    target_str = input(f"Units for target: ")
    goal = intprt.get_units_obj(target_str)

    code, powers = intprt.get_powers(vars, goal)

    if code == 1:
        print("Matrix is not invertible. The provided Vectors may not be linearily independent.")
        return

    val = 1

    if l<7 and not all(powers[i] == 0 for i in range(l, 7)):
        #units = ["s", "m", "kg", "A", "K", "mol", "cd"]
        print(f"Additional information required:", end = " ")
        for i in range(l, 7):
            print(f"{i}", end = " ") if powers[i] != 0 else None
        print(f"\n{powers}")
        return

    print("target = ", end = "")
    for i in range(l):
        name = vars[i].name
        power = powers[i]

        val *= (vars[i].value**powers[i])
        print(f"{name}^({power})", end="")

        if i < (l-1):
            print(" * ", end = "")

    print(f" = {val}{target_str}")

if __name__ == '__main__':
    main()
