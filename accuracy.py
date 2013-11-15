from tests.accuracy_statistics import AccuracyStatistics

def main():
	ta = AccuracyStatistics()
	ta.word_accuracy()

def show_statistics():
	ta = AccuracyStatistics()
	ta.statistics()

if __name__ == "__main__":
	import sys

	if sys.argv[1] == "1":
		main()
	else:
		show_statistics()