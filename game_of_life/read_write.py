def read_pattern(path: str) -> list[tuple[int,int]]:
    """Translates a text file into a game state."""
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

def write_pattern(path: str, pattern: list[tuple[int, int]]) -> None:
    """Encodes a final game state into a text file."""
    x_min = min([coord[0] for coord in pattern])
    x_max = max([coord[0] for coord in pattern]) 
    y_min = min([coord[1] for coord in pattern])
    y_max = max([coord[1] for coord in pattern])

    with open(path, "w") as file:
        for y in range(y_min,y_max + 1):
            line = ""
            for x in range(x_min,x_max + 1):
                if (x, y) in pattern:
                    line += "1" 
                else:
                    line += "0"
            file.write(line + "\n")