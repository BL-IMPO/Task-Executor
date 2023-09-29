
def lab_3_task_12():
	x = float(input("Введите число x: "))
	y = float(input("Введите число y: "))

	if x >= 0 and y >= 0:
		print("Среднее геометрическое {:.2f} и {:.2f} равно {:.2f}".format(x, y, ((x * y) ** (0.5))))
	elif x <= 0 and y <= 0:
		print("Среднее геометрическое {:.2f} и {:.2f} равно {:.2f}".format(x, y, (x * y) ** (0.5)))
	else:
		print("Среднее арефметическое {:.2f} и {:.2f} равно {:.2f}".format(x, y, ((x + y) / 2)))

if __name__ == "__main__":
	lab_3_task_12()