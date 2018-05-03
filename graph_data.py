import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [3, 37, 317, 3167]
B_input_chars = [3, 37, 317, 3167]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00555137191915,0.024567603003,0.164614582318,1.712784416] 
B_time = [0.0117624683768,0.0144321558143,0.0176307133364,0.027552880594]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algorithm A') # red dots
ax.plot(B_input_chars, B_time, 'bo-',label='Algorithm B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Worst case execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left')
ax.margins(.1)
fig.set_facecolor('white')
fig.show()