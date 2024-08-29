"""Modele for calculating the probabilty of 
a colour being red if red is chosen at random
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

def prob_red():
    """function that returns the probabilty of
     red colour outcome 
     """
    freq_dict = {i:new_list.count(i) for i in unique_colors}
    sum_red = freq_dict['RED']
    total_frequencies = sum(freq_dict.values())
    probability_red = sum_red/total_frequencies
    
    return probability_red

print(prob_red())
    
