from timeit import default_timer as timer
from datetime import timedelta
n = int(input())
line = list(map(int, input().split()))
# line = [int(item) for item in line]


# function to print triplets with 0 sum
def findTriplets2(arr, n):
    found = False
    triplets = []
    for i in range(n - 1):

        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                triplets.append([x, arr[i], arr[j]])
                found = True
            else:
                s.add(arr[j])
    return triplets


def findTriplets3(arr, n):
    found = False
    triplets = []
    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):

            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                triplets.append([x, arr[l], arr[r]])
                l += 1
                r -= 1
                found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1
    return triplets


start = timer()
triplets = findTriplets3(line, n)
end = timer()
print(timedelta(seconds=end-start))
# print(triplets)
start2 = timer()
triplets = [t[0] * t[1] * t[2] for t in triplets]
max = max(triplets)
if max < 0:
    print(-1)
else:
    print(max)
end2 = timer()
print(timedelta(seconds=end2-start2))