
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
    # Set the x ticks and x tick labels on the x-axis to the wrapped text labels and keep the text horizontally oriented
    ax.xaxis.set_major_locator(plt.FixedLocator(range(len(labels))))
    ax.set_xticklabels(labels, rotation = 0, ha = "center")

# Function for wrapping text on the x axis of some of the graphs specific to right justified labels
# Define the function with specific parameters: ax = axes object of the graph, width =  max width of text, break_long_words = boolean to determine whether or not long words should be broken up or not
def wrap_xticks_rt(ax, width, break_long_words=False):
    # Initialize an empty list where the storelabels will go
    labels = []
   # Initiate the loop that will run through each tick label on the x-axis
    for label in ax.get_xticklabels():
        # Obtain the text of the tick label
        text = label.get_text()
        # Wrap the text to fit within the specified width using the textwrap.fill function and textwrap module, determine if long words should be broken, append wrapped text to the labels list
        labels.append(textwrap.fill(text, width=width, break_long_words=break_long_words))
    # Set the x ticks and x tick labels on the x-axis to the wrapped text labels and keep the text horizontally oriented
    ax.xaxis.set_major_locator(plt.FixedLocator(range(len(labels))))
    ax.set_xticklabels(labels, rotation = 45, ha = "right")

# Function for adding bar count labels in non-stacked bar graphs in large font size
# Define the function
def add_bar_value_counts_lg():
    # Initiate a loop that goes through each bar in the current axis
    for p in plt.gca().patches:
        # Obtain the bar height and change it to an integer
        height = int(p.get_height())
        # Add the value count in the specified location (center of the bar) at half the height of the bar, center the font, make it white, in a specific fontsize and bold it
        plt.gca().text(p.get_x() + p.get_width()/2, height/2, str(height), ha = "center", color = "white", fontsize = 12, fontweight = "bold")

# Function for adding bar count labels in non-stacked bar graphs in medium font size
# Define function
def add_bar_value_counts_md():
        # Initiate a loop that goes through each bar in the current axis
    for p in plt.gca().patches:
        # Obtain the bar height and change it to an integer
        height = int(p.get_height())
        # Add the value count in the specified location (center of the bar) at half the height of the bar, center the font, make it white, in a specific fontsize and bold it
        plt.gca().text(p.get_x() + p.get_width()/2, height/2, str(height), ha = "center", color = "white", fontsize = 9, fontweight = "bold")

# Function for adding bar count labels in non-stacked bar graphs in small font size
# Define function
def add_bar_value_counts_sm():
        # Initiate a loop that goes through each bar in the current axis
    for p in plt.gca().patches:
        # Obtain the bar height and change it to an integer
        height = int(p.get_height())
        # Add the value count in the specified location (center of the bar) at half the height of the bar, center the font, make it white, in a specific fontsize and bold it
        plt.gca().text(p.get_x() + p.get_width()/2, height/2, str(height), ha = "center", color = "white", fontsize = 8, fontweight = "bold", rotation = 90)

# Function for add labls to non-stacked bar, but with special parameters for short columns
# Define Function
def add_bar_value_counts_spec():
    # Creating a loop to put the value count of each genre count into the middle of its respective bar vertically in white font
    for i, p in enumerate(plt.gca().patches):
        height = p.get_height()
        # For all bars but last two, show the label inside the bar with white font
        if height < 10: 
            plt.gca().text(p.get_x() + p.get_width()/2, height + 10, str(height), ha = "center", color = "black")
        elif i < len(plt.gca().patches) - 2:
            plt.gca().text(p.get_x() + p.get_width()/2, height/2, str(height), ha = "center", color = "white", rotation = 90)
        else: 
            # For the last two columns, put label above the bar in black font
            plt.gca().text(p.get_x() + p.get_width()/2, height + 10, str(height), ha = "center", color = "black", rotation = 90)

# Function to enumerate value counts for specific graphs
# Define Function
def enum_val_cnts(series, ax, color = "white", ha = "center", fontsize = 12, fontweight = 600):
    # Plot the value counts of each genre inside the bar centered vertically in white font
    # i = the index of each element in the series as an integer that starts at 0 and increments by 1 for each iteration 
    # v = the value of each element in the series as the actual count & is a numeric value
    # str(v) = converts the value of v to a string to be used in the bar plot
    for i, v in enumerate(series):
        ax.text(i, v/2, str(v), color = color, ha = ha, fontsize = fontsize, fontweight = fontweight)