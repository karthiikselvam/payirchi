def kidsWithCandies(candies,extraCandies):
    maxval = max(candies)
    for i in range(len(candies)): 
        if candies[i] == maxval:
            candies[i] = True 
        else:
            if extraCandies + candies[i] >= maxval:
                candies[i] = True
            else:
                candies[i] = False 
    
    return candies

result = kidsWithCandies([12,1,12],10)
print(result)

# One liner :
# maxval = max(candies)
# return [True if x+extracandies >= maxval else False  for x in candies]

