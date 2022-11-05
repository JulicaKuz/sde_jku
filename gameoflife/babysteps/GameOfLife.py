def countActiveNeighbours(field):
    counter = 0
    for r_index, row in enumerate(field):
        for c_index, cell in enumerate(row):
            if r_index == 1 and c_index == 1:
                continue
            elif cell is True:
                counter += 1
    return counter




def generate_next_round(field):
    # if countActiveNeighbours(field) < 2:
    #     return False
    if countActiveNeighbours(field) == 3 or countActiveNeighbours(field)==2:
        return True
    return False
