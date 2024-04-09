def check_vowels():
    name=input("Ingrese su nombre ")
    name=name.lower()
    a= "a" in name
    e= "e" in name
    i= "i" in name
    o= "o" in name
    u= "u" in name
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")
