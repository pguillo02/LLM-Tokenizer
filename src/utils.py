def most_common_pair(tokens: list[int]) -> dict:

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

def training_tokenizer(seq: list[int], iters: int) -> list[int]:
    
    i: int = 0

    while i < iters: 
        
        count: dict = most_common_pair(seq)
        mcp: tuple = max(count, key=count.get)

        seq: list[int] = swapping_most_common_pair(seq, mcp) 

        i += 1

    return seq

if __name__ == "__main__":
    
    dic = {(1,2):2, (2,3):1, (3,4):1, (4,1):1}
    #print("hola")
    #print(max(dic, key=dic.get))

    print(training_tokenizer([1,2,3,4,1,2], 2))
    