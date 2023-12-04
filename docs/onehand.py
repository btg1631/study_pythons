one = "1"
two = " "
three = "2"
four = " "
five = "3"
print(one, two, three, four, five)

one, two = two, one
print(one, two, three, four, five)

two, four = four, two
print(one, two, three, four, five)

two, three = three, two
print(one, two, three, four, five)

three, five = five, three
print(one, two, three, four, five)

four, five = five, four
print(one, two, three, four, five)

one, three = three, one
print(one, two, three, four, five)

two, three = three, two
print(one, two, three, four, five)