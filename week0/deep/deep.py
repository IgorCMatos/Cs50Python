
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? \n").strip().lower().replace("-"," ")

if answer == "42" or answer == "forty two":
    print("Yes")
else:
    print("no")
