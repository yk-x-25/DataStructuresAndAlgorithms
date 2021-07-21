res = {}
def change(amount):
    if res.get(amount):
        return res[amount]

    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5,5]
    if amount == 26:
        return [7,7, 7, 5]
    if amount == 27:
        return [5, 5, 5, 5,7]
    if amount == 28:
        return [7, 7, 7, 7]  
    
    result = change(amount-5)
    result.append(5)
    res[amount]=result 
    return result


if __name__ == "__main__":
    
    integer = 15
    for i in range(24,1001):
        ans = change(i)
        

        print(ans)