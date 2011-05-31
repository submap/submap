#!/usr/bin/env python
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import struct
import sys
import math

INPUT = 'bp2.osm'

nodes = {}
ways = {}
names = {}

class osmHandler(ContentHandler):
	def __init__(self):
		self.way_id = None
	def startElement(self, name, attrs):
		if name == 'node':
			nodes[attrs['id']] = (float(attrs['lat']), float(attrs['lon']))
		elif name == 'tag':
			if attrs['k'] == "highway":
				self.highway = True
			elif attrs['k'] == "waterway":
				if attrs['v'] in ["riverbank","stream"]:
					self.highway = True
			elif attrs['k'] == "natural":
				if attrs['v'] == "water":
					self.highway = True
			elif attrs['k'] == "name":
				if self.way_id:
					names[self.way_id] = attrs['v']
		elif name == 'way':
			self.way_id = attrs['id']
			
			self.highway = False
		elif name == 'nd':
			node_id = attrs['ref']
			if self.way_id in ways:
				ways[self.way_id].append(node_id)
			else:
				ways[self.way_id] = [node_id]
		elif name== 'relation':
			self.way_id = None
	def endElement(self, name):
		if name == 'way':
			if not self.highway and self.way_id in ways:
				del ways[self.way_id]

parser = make_parser()
curHandler = osmHandler()
parser.setContentHandler(curHandler)
parser.parse(INPUT)
	
def lat2point(y):
	y=(y-47.3)*3000
	return y
	
def lon2point(x):
	x=(x-19)*3000
	return x
	
stroke(0)
strokewidth(.5)
autoclosepath(False)

font("Verdana",2)

def betweenpoints(x1,y1,x2,y2,str):

    #stroke(0)
    #line(x1, y1, x2, y2)

    d=distance(x1,y1,x2,y2)
    n=0
    str2=""
    while textwidth(str2)<d:
        str2 += str[n%len(str)]
        n+=1
    rotation = 0
    offsetX = 0
    offsetY = 0
    if((y2-y1)!=0):
        alfa = math.pi/2+math.atan2((x1-x2),(y1-y2))
        '''
        probaltam kiszamoltni, de aztan talaltam egyszerubb megoldast
        c = math.sqrt(2*(d/2)*(d/2)+d*math.cos(alfa))
        print c
        beta = math.fabs((math.pi-alfa)/2)
        offsetX = math.cos(beta)*c
        
        print offsetX
        offsetY = math.sin(beta)*c
        '''
    push()
    
   # translate(x1-offsetX, y1-offsetY)
    translate((x1+x2)/2-d/2, (y1+y2)/2)
    rotate(radians=alfa)
    text(str2,0,0)
    pop()

def distance(xi,yi,xj,yj):
    return math.sqrt((xi-xj)*(xi-xj)+(yi-yj)*(yi-yj))
    


for (wid, way) in ways.items():
	ncoords = nodes[way[0]]
	
	#beginpath(lon2point(ncoords[1]),lat2point(ncoords[0]))
	oldx=lon2point(ncoords[1])
	oldy=lat2point(ncoords[0])
	#if wid in names:
	#	fill(0)
	#	text(names[wid], lon2point(ncoords[1]),lat2point(ncoords[0]))
	#	nofill()
		
	for nid in way[1:]:
		ncoords = nodes[nid]
		
		betweenpoints(oldx, oldy,ncoords[1],ncoords[0],"str")
		oldx=lon2point(ncoords[1])
		oldy=lat2point(ncoords[0])
		#lineto(lon2point(ncoords[1]),lat2point(ncoords[0]))
	#endpath()

print "ready"


