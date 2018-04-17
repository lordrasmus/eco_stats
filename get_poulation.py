import requests, json, sys

from pprint import pprint

base_url = "http://gameserver.tangotanzen.de:28401"

def get_data( path, payload=None ):
	global base_url
	url = base_url + path
	headers = {'content-type': 'application/json'}

	if payload:
		r = requests.post( url, data=json.dumps(payload,separators=(',',':')), headers=headers)
	else:
		r = requests.get( url )

	#pprint( r.json() )
	return r.json()


def get_population( name , time=None):
	global end_time
	t = end_time
	if not time == None:
		t = time
	tmp = get_data( "/datasets/get?time_start=" + t + "&time_end=" + t , payload=["World","Population",name + " Population"] )
	value = tmp[0]["Value"]
	return value

def get_timerange( ):
	global end_time
	timerange = get_data( "/datasets/timerange" )
	end_time = str( timerange[1] - 0.01 ) # genau die endzeit ergibt immer 0
	timestamps = []
	t = 0
	while t < timerange[1]:
		timestamps.append(str(t))
		t+=1

	timestamps.append(end_time)
	return timestamps

def print_pops( liste ):
	
	pops= []
	for tmp in liste:
		pops.append( {"NAME":tmp,"VALUES": {}})
		
	
	for p in pops:
		sys.stdout.write("\r\033[2Kfetch: " + p["NAME"] + "")
		for t in timestamps:
			sys.stdout.write("   t: " + t)
			sys.stdout.flush()
			p["VALUES"][t] =  get_population( p["NAME"] , time=t)
		
		#pprint( p )
		#print("{0:8}  {1:6}".format( p + ":", ))

	sys.stdout.write("\r\033[2K")
	txt = "          "
	for t in timestamps:
		if t == end_time:
			txt += "{0:>8}".format( "now" )
		else:
			txt += "{0:>8}".format( t )
	print( txt )


	for p in pops:
		txt = ""
		txt += "{0:8}  ".format( p["NAME"] + ":" )
		for t in timestamps:
			txt += "{0:>8}".format( p["VALUES"][t] )
		print( txt )

print("")

timestamps = get_timerange()


#print("Bison:  {0:6}".format( get_population( "Bison" ) ))
pops = [{"NAME":"Elk"},{"NAME":"Hare"},{"NAME":"Turkey"},{"NAME":"Wolf"},{"NAME":"Fox"},{"NAME":"Wheat"}, {"NAME":"Beets"} ]

print_pops( ["Elk","Hare","Turkey","Wolf","Fox"] )

print("-------------------------")

print_pops( ["Wheat","Beets","Beans","Corn","Camas","Tomatoes"] )
