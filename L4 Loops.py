while True:
    script = True
    username = input ("insert name... ")
    print("Hallo", username)
    print("Wat is LMF+AO?")
    print("A: LMFOA")
    print("B: LMFAO")
    inputText = input()
    if inputText == "A" or inputText == ("a"):
        print("Fout Automatisch Restart")
        script = True 
        print("")
    elif inputText == "B" or inputText == ("b"):
        print("Goedzo wil je herstarten Y/N")
        inputText = input()
        if inputText == ("Y") or inputText == ("y"):
            script = True
            print("")
        elif inputText == ("N") or inputText == ("n"):
            break
            exit()