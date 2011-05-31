#ifndef _TEST_APP
#define _TEST_APP
#define PORT 1337

#include "ofMain.h"
#include "ofxShader.h"
#include "ofxSQLiteHeaders.h"
#include "ofxOsc.h"

#include <vector>
//#include "json.h"

struct COORD {
	double lat;
	double longi;
	int time1;
};

class testApp : public ofBaseApp{
	
public:
	void setup();
	void update();
	void draw();
	void drawMap();
	
	void keyPressed  (int key);
	void keyReleased(int key);
	void mouseMoved(int x, int y );
	void mouseDragged(int x, int y, int button);
	void mousePressed(int x, int y, int button);
	void mouseReleased(int x, int y, int button);
	void windowResized(int w, int h);
	
	ofxOscReceiver receiver;
	
private:

	GLuint genList;
	int ossz;
	
	
	class Vector2D
	{
	public:
		float x, y;
		
		float *arr() { return &x; }
	};
	
	Vector2D hels;
	
	class Path2D
	{
	public:
		vector<Vector2D> path;
	};
	
	/*
	void newError(string error);
	double parseJSON(string s), remoteResult, localResult;
	
	//double pontok[30000][1000][2];
	vector<vector<pair<double,double> > > pontok;	
	int pontokLength;
	vector<int> pontok2Length;
	float ko;
	Json::Value root;   // will contains the root value after parsing.
	Json::Reader reader;
	*/
	
	void readRaw(string filename);
	vector<Path2D> object;
	ofxShader myShader;
};

#endif
