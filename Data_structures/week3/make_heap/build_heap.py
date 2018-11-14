# python3

class HeapBuilder:
  def __init__(self):
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def LeftChild(self, i):
    return 2 * i + 1
  
  def RightChild(self, i):
    return 2 * (i + 1)

  def siftdown(self, i):
    MinIndex = i
    l = self.LeftChild(i)
    if l <= len(self._data) and self._data[MinIndex] > self._data[l]:
      MinIndex = l
    r = self.RightChild(i)
    if r <= len(self._data) and self._data[r] < self._data[MinIndex]:
      MinIndex = r
    if i != MinIndex:
      self._data[i], self._data[MinIndex] = self._data[MinIndex], self._data[i]
      print(i, MinIndex)
    