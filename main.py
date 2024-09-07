import json
import matplotlib.pyplot as plt
import math


def load_json(path: str) -> dict:
	"""
  Loads the json at the specified path.
  """
	with open(path, "r") as data:
		tier_lists = json.load(data)
	return tier_lists


def find_metas(data: dict) -> dict:
	"""
  Using every month's tierlist given by AshBS, returns two dictionaries:
  - One containing the sum of the stars got by the brawler in every tier list (meta_points).
  - Another containing the stars got per brawler (raw_values).
  """
	meta_points = {}
	raw_values = {}
	for month, tier_list in data.items():
		for score, brawlers in tier_list.items():
			for brawler in brawlers:
				previous_score, months = meta_points.get(brawler, (0, 0))
				new_score = previous_score + int(score)
				new_months = months + 1
				meta_points[brawler] = (new_score, new_months)
				raw_values.setdefault(brawler, []).append(int(score))

	return (meta_points, raw_values)


def sort_split_list(data: list) -> tuple:
	"""
  Takes a list as an argument and then sorts and splits it in order to prepare the data to be plotted.
  Returns a tuple with two lists, the keys and the values.
  """
	sorted_data = sorted(data, key=lambda x: x[1])
	x = [elem[0] for elem in sorted_data]
	y = [elem[1] for elem in sorted_data]
	return (x, y)


def plot_data(x: list, y: list, title: str, name: str) -> None:
	"""
  Plots in an horizontal bar graph the given data and stores it an image with the specified name.
  """
	plt.figure(figsize=(13, 25))
	plt.barh(x, y)
	plt.title(title)
	plt.tight_layout()
	plt.xlabel("values")
	plt.ylabel('brawlers')
	for index, value in enumerate(y):
		plt.text(value, index, f"{round(value, 2)}", va='center')
	plt.savefig(f"{name}.jpg")


def represent_meta_points(data: dict) -> None:
	"""
  Prepares the meta_points dict to be plotted, and plots it using the function plot_data
  """
	prepared_data = [(elem[0], elem[1][0]) for elem in data.items()]
	x, y = sort_split_list(prepared_data)
	plot_data(x, y, "Stars got per brawler", "meta_points")


def represent_meta_percentage(data: dict) -> None:
	"""
  Prepares a percentage list relative to the maximum number of stars a brawler can get and plots it using the plot_data function.
  """
	percentages = []
	for i in data.items():
		brawler = i[0]
		meta_points = i[1][0]
		months_since_release = i[1][1]
		percentage = (100 * meta_points) / (5 * months_since_release
																																						)  # calculating the meta percentage
		percentage_tuple = (brawler, percentage)
		percentages.append(percentage_tuple)

	x, y = sort_split_list(percentages)
	plot_data(x, y, 'Percentage of stars relative to the max possible',
											'percentages')


def mean_per_brawler(data: dict) -> dict:
	"""
  Calculates the stars mean per brawler and plots it using the plot_data function.
  """
	means = []
	for brawler, (meta_points, months_since_release) in data.items():
		mean = round(meta_points / months_since_release, 2)
		means.append((brawler, mean, months_since_release))

	means = sorted(means, key=lambda x: x[1])
	x = [elem[0] for elem in means]
	y = [elem[1] for elem in means]
	plot_data(x, y, 'Stars mean per brawler', 'stars_mean')
	return means


def standard_deviation(means: dict, values: dict):
	"""
  Calculates the standard deviation related to the stars mean per brawler, and then plots it using the plot_data function.
  """
	deviations = []
	for brawler, mean, months in means:
		deviation = math.sqrt(sum([(x - mean)**2 for x in values[brawler]]) / months)
		deviations.append((brawler, deviation))

	x, y = sort_split_list(deviations)
	plot_data(x, y, 'Standard deviation related to the stars mean per brawler',
											'standard_deviation_per_brawler')


def main():
	tier_lists = load_json("tier_lists.json")
	meta_points, raw_values = find_metas(tier_lists)
	represent_meta_points(meta_points)
	represent_meta_percentage(meta_points)
	mean_list = mean_per_brawler(meta_points)
	standard_deviation(mean_list, raw_values)


if __name__ == '__main__':
	main()
