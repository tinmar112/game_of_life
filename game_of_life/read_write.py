def read_pattern(path: str) -> list[tuple[int,int]]:
    list = []
    with open(path, "r") as file:
        lines = file.readlines()
        for y in range(len(lines)):
            for x in range (len(lines[y])):
                value = lines[y][x]
                if value != '\n':
                    if int(value) == 1:
                        list.append((x,y))
    return list