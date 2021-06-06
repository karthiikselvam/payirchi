def minimumBribes(q):
    count = 0
    for indx in range(len(q)-1):
        if (q[indx] > q[indx + 1]):      
            val = q[indx] - 1
            diff = abs(val - indx)
            if (diff) <= 2:
                count += diff
            else:
                break
     
    if count > 0:
        print(count )
    else:
        print("Too chaotic")

minimumBribes([2, 1, 5 ,3, 4])