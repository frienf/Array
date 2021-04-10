import ctype

class Array:
	def __init__(self,size):
		assert size >0 ,"Array size must be zero"
		self._size = size
		PyArrayType = ctype.py_object * size
		self._elements = PyArrayType()
		self.clear(None)


	def __len__(self):
	    return self._size

	def __getitem__(self,index):
	    assert index >= 0 and index <len(self),"Array subscript out fo range"
	    return self._elements[index]

	def __clear__(self,value):
	    for i in range(len(self)):
	        self._elements = value     

	def __iter__(self):
	    return _ArrayIterator(self.elements)

class _ArrayIterator :
	def __init__(self,theArray) :
		self._arrayRef = theArray
		self._curNdx = 0

	def __iter__(self):
	   return self

	def __next__(self):
	    if self._curNdx <len(self._arrayRef):
	       entry = self._arrayRef[self.curNdx]
	       self.curNdx += 1
	       return entry
	    else:
	       raise StopIteration
	             	

