while True:
    print("'dog'|'cat'|'rabbit'")
    choose = input("Write your animal: ").lower().strip()

    if choose == "dog":
        print("for their dog I recommend beef-flavored kibble; that way, its coat will be more beautiful.")
    elif choose == "cat":
        print("for their cat I recommend fish-flavored kibble; that way, its coat will be more selky")
    elif choose == "rabbit":
        print("for your rabbit I recommend carrots or vegetables; that will keep it healthy.")


