import pickle

def storeData(dbDump):
	# Its important to use binary mode
	dbfile = open('pickleDB', 'ab')
	
	# source, destination
	pickle.dump(dbDump, dbfile)					
	dbfile.close()

def loadData():
	# for reading also binary mode is important
	dbfile = open('pickleDB', 'rb')	
	db = pickle.load(dbfile)
	# for keys in db:
	# 	print(keys, '=>', db[keys])
	dbfile.close()

if __name__ == '__main__':
	storeData()
	loadData()