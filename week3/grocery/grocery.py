
List = {}

while True:
    try:
        Item = input()
        Item = Item.upper()

        if Item in List:
            List[Item] += 1
        else:
            List[Item] = 1

    except EOFError:
        List = sorted(List.items())
        for number, name in List:
            print(f"{name} {number}")
        break
