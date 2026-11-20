def calculeaza(a, b, operatie="adunare"):
    if operatie == "adunare":
        return a + b
    if operatie == "inmultire":
        return a * b
    raise ValueError("Operatia trebuie sa fie 'adunare' sau 'inmultire'.")


if __name__ == "__main__":
    print(calculeaza(4, 5, "adunare"))
    print(calculeaza(4, 5, "inmultire"))
