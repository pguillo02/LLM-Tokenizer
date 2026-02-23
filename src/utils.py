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

def swapping_most_common_pair(tokens: list[int], mcp:tuple) -> list[int]:
    
    merged_tokens: list[int] = []
    try: 
        new_token: int = max(tokens) + 1
    except:
        new_token = 0 

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

    print(merged_tokens)
        
    
    return merged_tokens
             

if __name__ == "__main__":

    print(most_common_pair([]))