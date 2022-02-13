from constants import *
from pieces import *
from board import *

if __name__ == "__main__":
	#put tests here
	assert UP("a2")=="a3"
	assert all(UP(c+"6") is None for c in "abcdef")
	assert all(UP(c+r) is not None for c in "abcdef" for r in "12345")
	print("All tests passed")
else:
	raise ValueError("Test file was imported.  That is bad.")