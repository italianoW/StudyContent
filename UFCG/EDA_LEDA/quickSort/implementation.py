def partition(array,left,right):
  pivot = (right+left/2)
  array[0],array[pivot] = array[pivot],array[0]
  helperPointer = 0
  for i in range(1,len(array)):
    if array[i] < array[pivot]:
      array[helperPointer],array[i] = array[i],array[++helperPointer]
  array[0],array[helperPointer] = array[helperPointer],array[0]
