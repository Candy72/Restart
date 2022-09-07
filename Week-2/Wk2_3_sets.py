#Sets
your_colours = {"red", "white", "orange", "blue"}
my_colours = {"red", "purple"}
their_colours = {"orange", "brown", "grey", "blue", "red"}
# all_colours = your_colours.intersection(my_colours.intersection(their_colours))
# all_colours2 = my_colours & their_colours & your_colours
# all_colours3 = your_colours.intersection(my_colours).intersection(their_colours)
# all_colours4 = your_colours.intersection(my_colours, their_colours)

combine_colours = my_colours | your_colours | their_colours #combines unique items
combine_colours2 = my_colours.union(your_colours, their_colours)

# my_tuple = "Holden", "Honda"
# print(type(my_tuple))
# my_tuple.count


#3 ways to do the same thing
#python likes one way