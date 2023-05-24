import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
   #  print("hi")
   #  print(matplotlib.__version__)
   #  xpoints = np.array([0, 6])
   #  ypoints = np.array([0, 250])
   #  #ypoints = np.array([3, 8, 1, 10])
   #
   #  plt.plot(ypoints, marker='o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
   #  y1 = np.array([3, 5, 1, 10])
   #  y2 = np.array([6, 2, 7, 11])
   #  #plt.subplot(1, 2,2)
   #  #plt.plot(y1)
   #  #plt.plot(y2)
   #  plt.title("Sports Watch Data")
   #  plt.xlabel("Average Pulse")
   #  plt.ylabel("Calorie Burnage")
   #  plt.grid()
   #  plt.show()
   #
   #  plt.plot(xpoints, ypoints)
   # # plt.show()
   # plot 1:
   x = np.array([0, 1, 2, 3])
   y = np.array([3, 8, 1, 10])

   plt.subplot(2, 1, 1)
   plt.plot(x, y)

   # plot 2:
   x = np.array([0, 1, 2, 3])
   y = np.array([10, 20, 30, 40])

   plt.subplot(2, 1, 2)
   plt.plot(x, y)

   plt.show()
if __name__ == '__main__':
    main()


