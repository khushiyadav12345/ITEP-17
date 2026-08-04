s = "LRLLRRLR"
l_count = 0
r_count = 0
counter = 0

for ch in s:
    if ch == "R":
        r_count += 1
    else:
        l_count += 1
            
    if r_count == l_count:
            counter += 1
print(f"{counter}")
         