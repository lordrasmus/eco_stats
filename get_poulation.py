import requests, json

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


def get_population( name ):
	value = get_data( "/datasets/get?time_start=" + end_time + "&time_end=" + end_time , payload=["World","Population",name + " Population"] )[0]["Value"]
	return value


timerange = get_data( "/datasets/timerange" )
end_time = str( timerange[1] - 0.01 ) # genau die endzeit ergibt immer 0



#print("Bison:  {0:6}".format( get_population( "Bison" ) ))
print("Elks:   {0:6}".format( get_population( "Elk" ) ))
print("Hare:   {0:6}".format( get_population( "Hare" ) ))
print("Turkey: {0:6}".format( get_population( "Turkey" ) ))
print("Wolf:   {0:6}".format( get_population( "Wolf" ) ))
print("Fox:    {0:6}".format( get_population( "Fox" ) ))

print("-------------------------")

print("Wheat:  {0:6}".format( get_population( "Wheat" ) ))


