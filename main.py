# Offset values for keys
key_offsets = {'C': 0,
			   'C#': 1,
			   'Db': 1,
			   'D': 2,
			   'D#': 3,
			   'Eb': 3,
			   'E': 4,
			   'F': 5,
			   'F#': 6,
			   'Gb': 6,
			   'G': 7,
			   'G#': 8,
			   'Ab': 8,
			   'A': 9,
			   'A#': 10,
			   'Bb': 10,
			   'B': 11}

# The diatonic chords and their notes' values
symbol_to_notes = {'I': 	{1,5,8},
				   'ii': 	{3,6,10},
				   'iii': 	{5,8,12},
				   'IV': 	{6,10,1},
				   'V': 	{8,12,3},
				   'vi': 	{10,1,5},
				   'viio':  {12,3,6}}

notes_to_symbol = {frozenset({1,5,8}):  'I',
				   frozenset({3,6,10}): 'ii',
				   frozenset({5,8,12}): 'iii',
				   frozenset({6,10,1}): 'IV',
				   frozenset({8,12,3}): 'V',
				   frozenset({10,1,5}): 'vi',
				   frozenset({12,3,6}): 'viio'}

class Node:
	chord: str
	children: list
	finished: bool
	
	def __init__(self, chord: str):
		self.chord = chord
		self.children = []
		# if self.chord == goal chord
			# self.finished = True
		# else:
			# self.finished = False

	def evaluate(self):
		# (Main work goes here)

		# Find all possible chords
			# Is it diatonic?
				# Yes, add as new child

		# (Recursively) Evaluate all new children if they are not self.finished
		pass

def note_step(note: int, s: int) -> int:
	new = note+s
	if new > 12:
		new = new-12
	elif new < 1:
		new = new+12
	return new


def main():
	print("Hello, world!");
	# Create root node

	# Evaluate tree
		# root.evaluate()

	# Print tree

if __name__ == "__main__":
	main()
