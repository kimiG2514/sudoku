import math
from backtrack import backtrack

#returns a reduced search domain comprised of options with the least number of constraints
def mrvDomains(board):
    domains = {}
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                domains[i, j] = set(range(1, len(board) + 1))

    n = int(math.sqrt(len(board)))

    for i in range(len(board)):
        for j in range(len(board)):
            if type(board[i][j]) is not set:
                x_range = range(n)
                block1 = int(i / n)
                set_1 = {block1 * n + x for x in x_range}
                block2 = int(j / n)
                set_2 = {block2 * n + x for x in x_range}

                #check to see if the key in already in the row, column, or block
                for key in domains.keys():
                    if key[0] == i or key[1] == j or (key[0] in set_1 and key[1] in set_2):
                        domains[key].discard(board[i][j])

    minimum_remaining_value = None;
    for domain in domains.values():
        if minimum_remaining_value is not None:
            minimum_remaining_value = min(minimum_remaining_value, len(domain))
        else:
            minimum_remaining_value = len(domain)

    #Problem not solvable
    if minimum_remaining_value == 0:
        return None

    minimum_domains = {x: domains[x]
                   for x in domains.keys()
                   if len(domains[x]) == minimum_remaining_value}

    return minimum_domains


def select(board):
    min_domains = mrvDomains(board)

    if not min_domains:
        return None, None, None

    vals = min_domains.popitem()
    return vals[0][0], vals[0][1], vals[1]


#search driver
def search(board):
    return backtrack(board, select, True)
