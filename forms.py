import matplotlib.pyplot as plt

def triangle():
  x=[4,6,6,4]
  y=[3,4,3,3]
  plt.plot(x, y,)
  
def trapezium():
  x=[3,4,7,8,3]
  y=[2,5,5,2,2]
  plt.plot(x, y, 'g--s')

def parallelogram():
  x=[1,3,11,9,1]
  y=[1,7,7,1,1]
  plt.plot(x, y, 'b-p')



def run():
  triangle()
  trapezium()
  parallelogram()
  plt.show()
run()