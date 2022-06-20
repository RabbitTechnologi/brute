import brute
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('/sdcard/CP')
	except:pass
	try:os.mkdir('/sdcard/OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP')
	except:pass
brute.login()
