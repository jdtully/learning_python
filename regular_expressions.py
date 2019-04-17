 
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_213114.txt"
handle = open(name)
import re
nums = float()
totaler =float()
for line in handle:
    f_nums = re.findall('[0-9]+',line)
    if len(f_nums) > 0:
        for num in f_nums:
            nums += int(num)
print(nums)

