import datetime

script = True
while True: 
    print("[o]Hello you!, Ik ben Jason")
    print("[o]Wie ben jij?")
    username = input("[u]Mijn naam is : ")
    print("")
    print("[o]Hallo", username)
    print("")
    print("[o]De huidige tijd is ")
    x = datetime.datetime.now()
    print(x)
    print("")
    print("[o]Wil jij dit script herstarten? Y/N")

    scriptinput = input()
    if scriptinput == "y" or scriptinput == "Y":
        script = True
        print("[o]*Het script word gerestart*")
        print("")
    elif scriptinput == "n" or scriptinput == "N": 
        print("[o]Thanks for running")
        exit()