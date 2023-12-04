one = "1"
two = " "
three = "2"
four = " "
five = "3"
print("{} {} {} {} {}".format(one, two, three, four, five))

one, two = two, one
print("{} {} {} {} {}".format(one, two, three, four, five))

two, four = four, two
print("{} {} {} {} {}".format(one, two, three, four, five))

two, three = three, two
print("{} {} {} {} {}".format(one, two, three, four, five))

three, five = five, three
print("{} {} {} {} {}".format(one, two, three, four, five))

four, five = five, four
print("{} {} {} {} {}".format(one, two, three, four, five))

one, three = three, one
print("{} {} {} {} {}".format(one, two, three, four, five))

two, three = three, two
print("{} {} {} {} {}".format(one, two, three, four, five))

print("--------------------------------------")

first = "1"
second = " "
third = "2"
fourth = " "
fifth = "3"
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

second = first
first = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

fourth = second
second = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

second = third
third = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

third = fifth
fifth = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

fifth = fourth
fourth = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

first = third 
third = " "
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))

third = second
second = " " 
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))


