import sys

class CommandLineHandler:
	#Output function for the progress in a python script
	def getProgressString(self,done,total):
		nHashes = int(done/float(total)*80)
		progressbar = '[%s%s] %6.2f%% done.\r' % (nHashes*'#',(80-nHashes)*' ',done*100/float(total))
		return progressbar

	#Output function for the progress in a python script
	def printProgress(self,done,total):
		s = self.getProgressString(done, total)
		sys.stdout.write(s)
		sys.stdout.flush()
		if done == total:
			sys.stdout.write(' '*96 + '\r')
			sys.stdout.flush()
		return

	#Automatically add prefix to output
	def output(self,outString):
		print self.prefix,outString

	def warning(self,outString):
		print CliColors.WARNING,self.prefix,outString,CliColors.ENDC
		
	def error(self,outString):
		print CliColors.FAIL,self.prefix,outString,CliColors.ENDC

	def debug(self,outString):
		print CliColors.OKBLUE,self.prefix,outString,CliColors.ENDC
		
	def __init__(self,outputPrefix):
		self.prefix = outputPrefix
		
class CliColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'