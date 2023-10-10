# Happy Number

def happy(num):
    seen = []
    while num not in seen:
        seen.append(num)
        print(seen)
        sq_sum = 0
        while num>0:
            sq_sum += (num%10)*(num%10)
            num = num//10

        if sq_sum == 1:
            return True
        num = sq_sum
    return False

n = 21
print(happy(n))
