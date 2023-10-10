# Binary Search

def search(lst,n):

    l = 0
    u = len(lst) - 1

    while l<=u:
        mid = (u+l)//2

        if lst[mid] == n:
            global pos 
            pos = mid
            return True
        
        else:
            if lst[mid]<n:
                l = mid

            else:
                u = mid



num_trems = int(input("Enter The Number Of Terms To Be Added In The List: "))
lst = []

for i in range(num_trems):
    items = int(input("Enter Elements: "))
    lst.append(items)

target = int(input("Enter The Item To Be Searched: "))
if search(lst,target):
    print(f"Found At: {pos+1}")

else:
    print("Not Found")