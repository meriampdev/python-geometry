import matplotlib.pyplot as plt

# REFERENCES 
# https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
# https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.html
#

# CONSTANT
PIE=3.14
UNIT='cm'

# Squared
def squared(x):
  return x * x

def draw():
  Radius=int(input("Enter Radius:"))
  Circumference = 2 * PIE * Radius
  Area = PIE * squared(Radius)
  Diameter = 2 * Radius

  radiusLabel = 'Given Radius: {}{}'.format(Radius, UNIT)
  circumferenceLabel = 'Circumference: {}{}'.format(Circumference, UNIT)
  areaLabel = 'Area: {}{}²'.format(Area, UNIT)
  diameterLabel = 'Diameter: {}{}'.format(Diameter, UNIT)

  plt.axes()

  lineX = (Radius) * (-1)
  radiusLine = plt.Line2D((lineX, 0), (0.25, 0.25), lw=2)
  diameterLine = plt.Line2D((lineX, Radius), (0, 0), lw=2)
  diameterLine.set_color("#FF8C00") # hex for orange

  plt.gca().add_line(radiusLine)
  plt.gca().add_line(diameterLine)

  plt.text((lineX + 1), 1, radiusLabel, family="monospace")
  plt.text(1.5, -2, diameterLabel, family="monospace")
  plt.text(0, Radius, circumferenceLabel, family="monospace")
  plt.text(0, (Radius/2), areaLabel, family="monospace")

  circle = plt.Circle((0, 0), radius=Radius, fc='y')
  plt.gca().add_patch(circle)

  plt.axis('scaled')
  plt.show()