def countActiveNeighbours(field):
    counter = 0
    for r_index, row in enumerate(field):
        for c_index, cell in enumerate(row):
            if r_index == 1 and c_index == 1:
                continue
            elif cell is True:
                counter += 1
    return counter
