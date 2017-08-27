from random import randint

class ChatBot(object): 
	
	default_cfg={
				"announce": "Hello I am a chatbot but I can't do much yet...",
				"ack": ["ok","got it!","sure","no problem"],
				"greet": ["hi","yo","hello","hey"],
				"help": "We all need a little help sometimes :)",	
				"nack": ["sorry, I didn't get that", "I don't understand that command","!?"],
				"oops": ["oops", "oh oh", "ergh"]
				}

	
	def __init__(self, cfg=None):		

		self.__greets = None
		self.__acks = None
		self.__nacks = None
		self.__help = None
		self.__announce = None
		self.__oops = None

		if cfg is None:			
			self.__load_cfg(ChatBot.default_cfg)
		else:			
			self.__load_cfg(cfg)

	def __load_cfg(self, cfg):
		"""
			Load ChatBot configuration. Any 
			cfg: dictionary with the following fields: greetings, acks, nacks, help
		"""

		# values not present in the config dictionary will be replaced with default values 
		try:
			self.__greets = cfg["greet"]
		except KeyError:
			self.__greets = ChatBot.default_cfg["greet"]

		try:
			self.__acks = cfg["ack"]
		except KeyError:
			self.__acks = ChatBot.default_cfg["ack"]
		
		try:
			self.__nacks = cfg["nack"]
		except KeyError:
			self.__nacks = ChatBot.default_cfg["nack"]

		try:
			self.__help = cfg["help"]
		except KeyError:
			self.__help = ChatBot.default_cfg["help"]

		try:
			self.__announce = cfg["announce"]
		except KeyError:
			self.__announce = ChatBot.default_cfg["announce"]

		try:
			self.__oops = cfg["oops"]
		except KeyError:
			self.__oops = ChatBot.default_cfg["oops"]

	def __get_rand(self, obj):
		"""
			return a random element from a list
		"""		
		r = randint(0, len(obj)-1)
		return obj[r]		

	def ack(self):
		return self.__get_rand(self.__acks)

	def announce(self, name):
		return self.__announce.format(name)

	def greet(self):
		return self.__get_rand(self.__greets)

	def help(self):
		return self.__help

	def nack(self):
		return self.__get_rand(self.__nacks)

	def oops(self):
		return self.__get_rand(self.__oops)

	def chat(self, tokens, context):				
		if tokens[0] in self.__greets:		
			return [self.greet()]
		elif "help" in tokens:
			return [self.help()]
		else:
			return [self.nack()]
			
