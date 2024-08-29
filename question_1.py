"""module for calculating the
mean of a given set of colours 
"""


colours = """
      GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE,\
      CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN, ASH,\
      BROWN, GREEN, BROWN, BLUE, BLUE, BLUE, PINK, PINK, ORANGE, ORANGE, RED,\
      WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE, GREEN, YELLOW, GREEN, BROWN,\
      BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE,\
      BLUE, WHITE, WHITE, BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW,\
      ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN,\
      GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED,\
      WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
      """

# converting the string to a list of colours
splitted = colours.split(',') 

# creating a new list of stripped strings
new_list = []
for i in splitted:
    new_list.append(i.strip())

unique_colors = set(new_list)


# determining the mean colour
def mean():
    freq_dict = {i:new_list.count(i) for i in unique_colors}
    mean_index = (sum(freq_dict.values())) // 2
    return f"the mean is {sorted(new_list)[mean_index]}"


print(mean())


    

