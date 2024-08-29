


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
freq_dict = {i:new_list.count(i) for i in unique_colors}



def variance():
    total = 0
    mean_frequency = sum(freq_dict.values())/len(unique_colors)
    total_number_colours = len(new_list)
    for i in freq_dict.values():
        freq_mean_square = (i - mean_frequency) ** 2 
        total += freq_mean_square
    variance = total/total_number_colours
    return variance


print(variance()) 
