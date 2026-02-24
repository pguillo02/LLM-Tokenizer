def most_common_pair(tokens: list[int]) -> dict:
    """
    Function that recieves a list of tokens and returns a dictionary that contains the pairs present in the list a their frequency.

    In:
        tokens: list[int] = list of tokens

    Returns:
        count: dict() = Dictionary in which keys are the present pairs as tuples and values are the frequency count[(pair[0], pair[1])] = frequency.
    """

    if len(tokens) <=1:
        return ()

    count = dict()

    for i in range(len(tokens) - 1):
        if (tokens[i], tokens[i+1]) in count:
            count[(tokens[i], tokens[i+1])] += 1
        else:
            count[(tokens[i], tokens[i+1])] = 1 

    return count

def swapping_most_common_pair(tokens: list[int], mcp:tuple, new_token: int) -> list[int]:
    """
    Function that recieves a list of tokens, the most commun pair and the new_token that replaces it. The idea is for the function to replace every complete pair with 
    the new token, in order of reducing the length of the sequence.

    In:
        tokens: list[int] = the list of tokens
        mcp: tuple = the most commun pair as a tuple (pair[0], pair[1])
        new_token: int = the new token thats going to replace the mcp

    Returns: 
        merged_tokens: list[int] = new sequence with the new token
    """
    
    merged_tokens: list[int] = []

    i: int = 0
 
    while i < (len(tokens) - 1):
        
        if (tokens[i], tokens[i+1]) == mcp:
            merged_tokens.append(new_token)
            i += 2
        else:
            merged_tokens.append(tokens[i])

            i += 1

    if i == len(tokens ) - 1:
        merged_tokens.append(tokens[i])       
    
    return merged_tokens

def training_tokenizer(seq: list[int], iters: int, min_freq = 2) -> list[tuple]:
    """
    Loop for training the tokenizer. The function recieves a sequence and a number of iterations and learns a new reduction of the sequence every iteration. 

    In: 
        seq: list[int] = sequence used in the training
        iters: int = number of iterations of the training loop
        min_freq = 2: minimum frequency for a pair merged to be useful. 

    Return:
        merges: list[tuple(tuple(pair), new_token)] = reductions learned in the training process
    """

    if len(seq) < 2:
        print("Text length must be of at least two units")
        return 0
    
    i: int = 0
    merges: list[tuple] = []

    new_token: int = 255
    
    while i < iters: 
        new_token += 1 
        count: dict = most_common_pair(seq)
        mcp: tuple = max(count, key=count.get)

        if count[mcp] < min_freq:
            break

        seq = swapping_most_common_pair(seq, mcp, new_token)

        merges.append((mcp, new_token)) 

        i += 1

    return merges
    