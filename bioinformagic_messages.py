
import random


class Message:
	def __init__(self):
		self.verbs = [
			"Generating", "Uploading", "Downloading", "Parsing",
			"Heating", "Cooling", "Slicing", "Moulding", "Fixing",
			"Inspecting", "Interrogating", "Shaking", "Shifting", 
			"Reticulating", "Synthesizing", "Splurging", "BLASTing",
			"Inserting", "Hand-crafting", "Aligning", "Twiddling",
			"Sorting", "Downsampling", "Compressing", "Normalising",
			"Refreshing", "Salting", "Transposing", "Hashing", 
			"Building", "Yeeting", "Calculating"
		]
		self.nouns = [
			"data", "the cloud", "DNA", "nucleotides", "RAM",
			"AI", "algorithms", "sequences", "00010111001", "Firewall"
			"Python", "CSV", "files", "computer", "extensions", "URLs",
			"domains", "IP addresses", "equations", "user-interface",
			"FASTQs", "cores", "syntax", "bits and bytes", "ALL THE THINGS",
			"Excel", "mongoDB", "blockchain", "Dockers", "Flask", "codons",
			"hashes", "JSON", "Cryptography", 
		]


	def random_message(self):
		error = " ".join([random.choice(self.verbs), random.choice(self.nouns)])
		return error


if __name__ == "__main__":
	pass