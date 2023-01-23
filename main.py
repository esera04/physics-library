import numpy as np
import matplotlib.pylab as plt
class Oscillation_Calc:
    def __init__(self, amp, omeg, phaspt):
        self.amp = amp
        self.omg = omeg
        self.phaspt = phaspt
    
    def oscfuncplot(self):
        x = np.linspace(-np.pi, np.pi, 201)
        plt.plot(x, self.amp*np.sin((self.omeg*x) + self.phaspt))
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.show()

def main():
    print('type values in this order: amplitude, angular frequency, and phase point')
    amp = input()
    omeg = input()
    phaspt = input()
    func = Oscillation_Calc(amp, omeg, phaspt)
    func.oscfuncplot()