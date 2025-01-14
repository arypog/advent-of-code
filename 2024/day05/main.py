def parse(path):
    rules = []
    updates = []

    with open(path, 'r') as f: 
        for line in f:
            if '|' in line:
                x, y = map(int, line.split('|'))
                rules.append((x,y))
            elif ',' in line:
                updates.append(list(map(int,line.split(','))))

    return rules, updates

def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            ix = update.index(x)
            iy = update.index(y)
            
            if ix > iy: 
                return False
    return True

def is_invalid(update, rules):
    for x, y in rules:
        if x in update and y in update:
            ix = update.index(x)
            iy = update.index(y)
            
            if ix > iy: 
                update[ix], update[iy] = update[iy], update[ix];
                is_invalid(update, rules)
    return True

def main():
    #rules, updates = parse('in/in.test')
    rules, updates = parse('in/in.pub')

    total = 0
    invalid_updates = []
    for update in updates:
        if is_valid_update(update, rules):
            total += (update[len(update) // 2])
        else:
            invalid_updates.append(update)

    invalid_total = 0
    for update in invalid_updates:
        if is_invalid(update, rules):
            invalid_total += (update[len(update) // 2])
    print(total, invalid_total)

main()