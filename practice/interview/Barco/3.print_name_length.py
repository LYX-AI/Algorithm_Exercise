def print_name_length(filename:str):
    with open(filename,'r') as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            print(f"{name}:{len(name)}")

print_name_length('log.txt')