# We wrote loops in the form below.
# The starting value for the loop variable is 0
# by default.
# The values of the loop variable i go up to and
# not including 5.
for i in range(5):
    print(i)

print()

# The starting value for the loop variable is 1.
# The values of the loop variable i go up to and
# not including 5.
for i in range(1, 5):
    print(i)

print()

# The starting value for the loop variable is 2.
# The values of the loop variable i go up to and
# not including 11,
# printing every second number.
# The step size is 2.
for i in range(2, 11, 2):
    print(i)

print()

print(type(5))
print(type(2.3))
print(type('Hello'))
print(type(False))
print(type(range(5)))
print(type([5, 3, 1, 7, 0]))

print()

print(range(5))

print()

print(list(range(5)))
print('a' + 'b')
print(str(2.3) + 'a')
print(int('5'))

print()

my_list = [5, 3, 1, 7, 0]
# Get the first three elements in the list:
print(my_list[0:3])
# We started from 0 and went up to and not including
# 3.
# Get the last three elements in the list
# using slicing
print()
print(my_list[2:5])

print()

my_string = 'giraffe'
print(my_string[0])
print(my_string[2 : 5])

print()

print(my_list)
# Make a copy of the list.
# Make a second list that's the same as first.
copy_of_my_list = my_list[:]
print(copy_of_my_list)

print()

# This is called a "reference copy":
copy2_of_my_list = my_list
print(copy2_of_my_list)
# In general, avoid making a reference copy.
# It's considered dangerous.

print()

print(my_list)
# Here copy_of_my_list was created "properly".
# When I change copy_of_my_list, the change does not
# affect the original list.
copy_of_my_list[0] = -5
print(copy_of_my_list)
print(my_list)

print()

print(my_list)
# Here copy2_of_my_list was created
# with a reference copy, which we usually avoid, because,
# when I change copy2_of_my_list, the
# change affects the original list also.
copy2_of_my_list[-1] = 100
print(copy2_of_my_list)
print(my_list)

print()

# Where is the reference copy here? Is it actually desirable?
student_info = [['Alejandra', 43, 3.074], ['Nayeli', 61, 3.358],
                ['Hazel', 37, 3.422], ['Emma', 18, 3.163]]
print(student_info)
emma_info = student_info[3]
print(emma_info)
emma_info[1] = 20
print(emma_info)
print(student_info)






