from tests.accuracy_statistics import AccuracyStatistics

if __name__ == "__main__":
	import sys
	accur = AccuracyStatistics()
	try:
		accur.word_accuracy(sys.argv[1])
	except IndexError:
		accur.statistics()