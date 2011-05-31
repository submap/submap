#!/usr/bin/env python
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import struct
import sys

INPUT = 'finland.osm'
OUTPUT = 'fin_raw.dat'

nodes = {}
ways = {}

class osmHandler(ContentHandler):
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
		elif name == 'way':
			self.way_id = attrs['id']
			self.highway = False
		elif name == 'nd':
			node_id = attrs['ref']
			if self.way_id in ways:
				ways[self.way_id].append(node_id)
			else:
				ways[self.way_id] = [node_id]
	def endElement(self, name):
		if name == 'way':
			if not self.highway and self.way_id in ways:
				del ways[self.way_id]

parser = make_parser()
curHandler = osmHandler()
parser.setContentHandler(curHandler) 
print 'parsing', INPUT
sys.stdout.flush()
parser.parse(INPUT)

print 'writing', OUTPUT
sys.stdout.flush()
f = open(OUTPUT, 'w')

for way in ways.values():
	f.write(struct.pack('i', len(way)))
	for nid in way:
		ncoords = nodes[nid]
		f.write(struct.pack('ff', ncoords[0], ncoords[1]))

f.close()

