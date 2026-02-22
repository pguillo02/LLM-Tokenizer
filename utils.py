def most_common_pair(tokens: list[int]) -> tuple:

    if len(tokens) <=1:
        return ()

    count = dict()

    for i in range(len(tokens) - 1):
        if (tokens[i], tokens[i+1]) in count:
            count[(tokens[i], tokens[i+1])] += 1
        else:
            count[(tokens[i], tokens[i+1])] = 1 

    return max(count, key=count.get)

             