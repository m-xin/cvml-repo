import matplotlib.pyplot as plt

def show_rgb_color(r, g, b):
    plt.imshow([[(r/255, g/255, b/255)]])
    plt.axis("off")
    plt.show()

# Example usage
plt.figure(1)
# This will show a red color
show_rgb_color(241.77900904, 202.98700802, 85.6465843)

plt.figure(2)
# This will show a red color
show_rgb_color(245.74124926, 104.56301381, 76.81672176)

plt.figure(3)
# This will show a red color
show_rgb_color(170.20968169, 84.33118773, 83.11736178)

plt.figure(4)
# This will show a red color
show_rgb_color(103.80543855, 54.25129299, 58.20453212)
