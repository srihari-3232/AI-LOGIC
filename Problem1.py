
n = int(input("Enter number of ranges: "))
ranges = []
for i in range(n):
    start, end = map(int, input("Enter start and end: ").split())
    ranges.append([start, end])
ranges.sort()
start = ranges[0][0]
end = ranges[0][1]
for i in range(1, n):
    new_start = ranges[i][0]
    new_end = ranges[i][1]
    if new_start <= end:
        if new_end > end:
            end = new_end
    else:
        print(start, end)
        start = new_start
        end = new_end
print(start, end)