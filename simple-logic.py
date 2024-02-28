# Given a set of True or False values,
# use the logical operators to come up with
# a desired True or False outcome.

# Example: What happens if I do
# print(True == False or True)
# print(False and True or not False)

hot = True
have_pool = True
have_swimsuit = False

if hot and have_pool or have_swimsuit:
    print(True)
else:
    print(False)