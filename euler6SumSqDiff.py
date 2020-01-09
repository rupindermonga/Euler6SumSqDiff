

def SumSqDiff(n):
    sum1 = n*(n+1)/2
    sum2 = n*(n+1)*(2*n+1)/6

    final_sum = sum1**2 - sum2

    return final_sum

final = SumSqDiff(100)
print(final)