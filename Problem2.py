n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
sum = 0
for i in range(k):
    sum = sum + numbers[i]
max= sum
for i in range(k, n):
    sum = sum - numbers[i - k]
    sum = sum+ numbers[i]
    if sum > max:
        max = sum
print(max)