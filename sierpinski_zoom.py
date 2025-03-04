import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

maxnodescale = 6   # Maximum X or Y size of the node 
minnodescale = -1  # Minimum X or Y size of the node 

# Function to draw the Sierpiński Triangle
def sierpinski_triangle(order, vertices):
    """Recursively generate the Sierpiński Triangle."""
    if order == 0:
        triangle = np.array(vertices + [vertices[0]])  # Close the triangle
        plt.plot(triangle[:, 0], triangle[:, 1], 'k')
    else:
        midpoints = [(vertices[i] + vertices[(i+1) % 3]) / 2 for i in range(3)]

        if minnodescale <= midpoints[0][0] <= maxnodescale or minnodescale <= midpoints[2][0] <= maxnodescale :
            sierpinski_triangle(order - 1, [vertices[0], midpoints[0], midpoints[2]])
        if minnodescale <= midpoints[0][0] <= maxnodescale or minnodescale <= midpoints[1][0] <= maxnodescale :
            sierpinski_triangle(order - 1, [vertices[1], midpoints[1], midpoints[0]])
        if minnodescale <= midpoints[1][0] <= maxnodescale or minnodescale <= midpoints[2][0] <= maxnodescale :
            sierpinski_triangle(order - 1, [vertices[2], midpoints[2], midpoints[1]])

# Set the initial triangle vertices
initial_vertices = np.array([[0, 0], [1, 0], [0.5, 1]])

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))

frames = 100  # Number of frames
zoom_factor = 1.05  # Multiplicative zoom-in factor (should be >1 for zoom-in)

# Function to update the plot for animation
def update(frame):
    ax.clear()
    scale = zoom_factor ** frame  # Shrinking the view for zoom-in effect
    new_vertices = initial_vertices * scale + [0 * (1 - scale), 0 * (1 - scale)]
    sierpinski_triangle(order=8, vertices=new_vertices)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.axis("off")

ani = animation.FuncAnimation(fig, update, frames=frames, interval=200)

# Try using FFmpeg first, fallback to GIF if unavailable
try:
    ani.save("sierpinski_zoom_in.mp4", writer="ffmpeg", fps=30)
    print("Animation saved as sierpinski_zoom_in.mp4")
except Exception as e:
    print(f"FFmpeg not available, saving as GIF instead. Error: {e}")
    ani.save("sierpinski_zoom_in.gif", writer="pillow", fps=30)
    print("Animation saved as sierpinski_zoom_in.gif")
