
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

class ModuleName:
	def __init__(self):
		self.prefixes = ["Introduction to", "Advanced", "IT for", 
						"Whole systems", "Applied"]
		self.adjectives = ["clinical", "research", "health", "advanced",
							"professional"]
		self.subjects = ["bioinformatics", "genetics", "informatics",
						"healthcare", "science", "IT", "practice", 
						"leadership"]

	def random_module(self):
		# Core messages
		message_1 = " ".join([random.choice(self.prefixes), 
							random.choice(self.adjectives),
							random.choice(self.subjects),])

		message_2 = " ".join([random.choice(self.prefixes), 
							random.choice(self.subjects),])
		# Extra messages
		message_a = " ".join([random.choice(self.adjectives), 
							random.choice(self.subjects),])
		message_b = " ".join([random.choice(self.subjects),])


		extras = ["yes", "no"]
		add_extras = random.choice(extras)
		initials = [message_1, message_2]
		message_joiners = ["and", "with"]
		extras = [message_a, message_b]


		if add_extras == "yes":
			module_name = " ".join([random.choice(initials),
									random.choice(message_joiners),
									random.choice(extras),])
		else:
			module_name = " ".join([random.choice(initials),
									random.choice(message_joiners),
									random.choice(extras),])
		return module_name		




if __name__ == "__main__":
	pass