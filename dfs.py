"""

"""


################################################################################
# DFS
def dfs(visited_cities, city, graph):
	if len(visited_cities) == 4:
		return

	if city not in visited_cities:
		visited_cities[city] = True
		for adjacent_city in graph[city]:
			dfs(visited_cities, adjacent_city, graph)


################################################################################
# Main
if __name__ == "__main__":
	values = {
		"NY": 4,
		"SF": 1,
		"DAL": 5,
		"LAX": 1,
		"CHI": 3,
		"SJ": 4
	}

	graph = {
		"NY": ["SF", "LAX"],
		"SF": ["NY", "SJ"],
		"LAX": ["NY", "CHI"],
		"CHI": ["LAX", "SJ"],
		"SJ": ["SF", "CHI"],
		"DAL": []
	}

	max_value = 0
	flightpath = []

	for city in values:
		visited_cities = {}
		current_city = city  # start @ a new city

		dfs(visited_cities, current_city, graph)

		# calculate total from the 3-flight journey
		total = 0
		for vc in visited_cities:
			total += values[vc]

		if total > max_value:
			max_value = total
			flightpath = list(visited_cities.keys())  # update flightpath as well

	# output
	print(f'MAX VALUE: {max_value}')
	print(f'FLIGHTPATH: {flightpath}')
