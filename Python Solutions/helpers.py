def read_file(file_name, split='\n'):
	with open(file_name, 'r') as file:
		array = file.read().split(split)
	return array


def read_file_numbers(file_name, split='\n'):
	with open(file_name, 'r') as file:
		array = file.read().split(split)
	return [int(x) for x in array]
