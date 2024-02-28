# Swap the values of two given numbers
# using assignment operators and then
# compare them to ensure they have been swapped.

variable_a = -3
variable_b = 10
result = variable_a - variable_b
print (result) #should return -13

variable_a, variable_b = variable_b, variable_a
new_result = variable_a - variable_b
print (new_result) #should return 13