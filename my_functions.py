
import matplotlib.pyplot as plt
import textwrap

# Function for wrapping text on the x axis of some of the graphs
# Define the function with specific parameters: ax = axes object of the graph, width =  max width of text, break_long_words = boolean to determine whether or not long words should be broken up or not
def wrap_xticks(ax, width, break_long_words=False):
    # Initialize an empty list where the storelabels will go
    labels = []
   # Initiate the loop that will run through each tick label on the x-axis
    for label in ax.get_xticklabels():
        # Obtain the text of the tick label
        text = label.get_text()
        # Wrap the text to fit within the specified width using the textwrap.fill function and textwrap module, determine if long words should be broken, append wrapped text to the labels list
        labels.append(textwrap.fill(text, width=width, break_long_words=break_long_words))
    # Set the tick labels on the x-axis to the wrapped text labels and keep the text horizontally oriented
    ax.set_xticklabels(labels, rotation=0)

# Function for adding bar count labels in non-stacked bar graphs
# Define the function
def add_bar_value_counts():
    # Initiate a loop that goes through each bar in the current axis
    for p in plt.gca().patches:
        # Obtain the bar height and change it to an integer
        height = int(p.get_height())
        # Add the value count in the specified location (center of the bar) at half the height of the bar, center the font, make it white, in a specific fontsize and bold it
        plt.gca().text(p.get_x() + p.get_width()/2, height/2, str(height), ha = "center", color = "white", fontsize = 12, fontweight = "bold")

def add_bar_counts():
    # i = the index of each element in the series as an integer that starts at 0 and increments by 1 for each iteration 
    # v = the value of each element in the series as the actual count & is a numeric value
    # str(v) = converts the value of v to a string to be used in the bar plot
    for i, v in enumerate(top_apple_tv_genres["Count"]):
        plt.text(i, v/2, str(v), color = "white", ha = "center", fontsize = 14, fontweight = 600)
