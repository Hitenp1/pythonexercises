#list of daily python code to enhance learning of lanaguge

#function to double character
def double_char(item):
  word = ""
  for x in item:
     word += x*2
  print (word)

double_char('The')

nums = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 88]
for item in nums:
  if item % 2 == 0 and item % 8 == 0:
    print (item)

print (list(filter(lambda x: x % 2 == 0, nums)))

print (list(map(lambda x: x**2, nums)))

# no reduce in python3
print (sum(nums))
# string of nums sum(int(i) for i in nums)



