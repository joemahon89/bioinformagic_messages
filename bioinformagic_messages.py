
import random


class Message:
	def __init__(self):
		self.verbs = [
			"Generating", "Uploading", "Downloading", "Parsing",
			"Heating", "Cooling", "Slicing", "Moulding", "Fixing",
			"Inspecting", "Interrogating", "Shaking", "Shifting", 
			"Reticulating", "Synthesizing", "Splurging", "BLASTing",
			"Inserting", "Hand-crafting", "Aligning", "Twiddling",
			"Sorting", "Downsampling"
		]
		self.nouns = [
			"data", "the cloud", "DNA", "nucleotides", "RAM",
			"AI", "algorithms", "sequences", "pipettes", "00010111001",
			"Python", "CSV", "files", "computer", "extensions", "URLs",
			"domains", "IP addresses", "equations", "user-interface",
			"FASTQs", "cores", "syntax", "bits and bytes", "ALL THE THINGS",
			"Excel", "mongoDB", "blockchain"
		]


	def random_message(self):
		error = " ".join([random.choice(self.verbs), random.choice(self.nouns)])
		return error

