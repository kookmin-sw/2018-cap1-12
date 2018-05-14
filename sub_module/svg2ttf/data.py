import os



def get_data_unicodes(path = "data"):
	unicodes = []
	for l in os.listdir(path):
		if l != ".DS_Store":
	 		unicodes.append(l.split(".")[0])
	return sorted(unicodes)



def get_data_address(path = "data"):
	address = []
	for l in os.listdir(path):
		if l != ".DS_Store":
			address.append(path + "/" + l)
	return sorted(address)