import matplotlib.pyplot as plt
import math

# Define Differential Equation
def dydx(x, y):
  return math.cos(x)

def rksolve(f, x0, y0, x_final, dx):
  # Define Runge-Kutta Constants
  def T4(x, y, dx):
    k1 = f(x, y)
    k2 = f(x + (dx/2), y + ((dx/2)*k1))
    k3 = f(x + (dx/2), y + ((dx/2)*k2))
    k4 = f(x + dx, y + (dx*k3))
  
    return (1/6)*(k1 + (2*k2) + (2*k3) + k4)
  
  x = x0
  y = y0

  xvec = [x]
  yvec = [y]

  while x <= x_final:
    y = y + dx*T4(x, y, dx)
    x = x + dx

    xvec.append(round(x, 4))
    yvec.append(y)

  # Set Plot Parameters
  plt.title("[RK] Solution to dy/dx = cos(x)")
  plt.grid(True)
  plt.axis([x0, x_final, -1, 3])
  plt.plot(xvec, yvec)
  plt.savefig("graph.png")

rksolve(dydx, 0, 1, 2*math.pi, 0.01)
