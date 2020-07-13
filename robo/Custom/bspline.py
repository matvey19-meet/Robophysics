
import numpy as np
from scipy import interpolate
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt
x = np.array([10.0, 14.915802661707126, 21.82640091725616, 27.522139992881073, 39.82086149224408, 58])
y = np.array([2, 12.396388035810952, 26.270595463639122, 30.339816074812664, 37.028721028622925, 39.5])
plt.plot(x, y)


x_new = np.linspace(min(x), max(x), 300)
a_BSpline = interpolate.make_interp_spline(x, y)
y_new = a_BSpline(x_new)

spl = make_interp_spline(x, y, k=2)  # type: BSpline
power_smooth = spl(x_new)


plt.plot(x_new, power_smooth)

plt.show()