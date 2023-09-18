import copy

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

# Global user variables
START_CHORD = 'I'
GOAL_CHORD = 'I'

class Node:
	chord: str
	children: list
	finished: bool
	history: list
	is_root: bool
	
	def __init__(self, chord: str, history: list):
		self.chord = chord
		self.children = []
		self.history = history
		self.history.append(self.chord)
		self.finished = (self.chord == GOAL_CHORD)
		if self.finished and self.chord != 'I':
			self.history.append(GOAL_CHORD)

	def print_node(self):
		output = ""
		for i, chord in enumerate(self.history):
			if i == len(self.history)-1:
				output += chord
			else:
				output += chord + " "
		print(output)

	def print_progressions(self):
		if self.finished: self.print_node()
		for child in self.children:
			child.print_progressions()
		
	def evaluate(self):
		# Find all possible chords
		steps = [-2, -1, 0, 1, 2]
		for i in steps:
			for j in steps:
				for k in steps:
					# New chord
					chord = list(symbol_to_notes[self.chord])
					n1 = note_step(chord[0], i)
					n2 = note_step(chord[1], j)
					n3 = note_step(chord[2], k)
					new = frozenset({n1, n2, n3})
					
					# Is it diatonic and not in 'history' (excluding starting chord)? 
					if new in symbol_to_notes.values() and notes_to_symbol[new] not in self.history[1:]:
						# Yes, add as new child
						child = Node(notes_to_symbol[new], copy.deepcopy(self.history))
						self.children.append(child)

		# (Recursively) Evaluate all new children if they are not self.finished
		for child in self.children:
			if child.finished == False:
				child.evaluate()
		
def note_step(note: int, s: int) -> int:
	new = note+s
	if new > 12:
		new = new-12
	elif new < 1:
		new = new+12
	return new


def main():
	# Create root node
	root = Node(START_CHORD, [])

	# Evaluate tree
	root.evaluate()

	# Print tree
	root.print_progressions()

if __name__ == "__main__":
	main()
