from tests.test_accuracy import TestAccuracy

def main():
	ta = TestAccuracy()
	ta.test_word_accuracy()

def show_statistics():
	ta = TestAccuracy()
	ta.statistics()

if __name__ == "__main__":
	import sys

	if sys.argv[1] is 1:
		main()
	else:
		show_statistics()