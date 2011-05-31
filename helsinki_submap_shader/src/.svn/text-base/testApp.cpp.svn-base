#include <cstdio>
#define numbCity 36
//#include <iostream>
//#include <fstream>
//#include <vector>

#include "testApp.h"

using namespace std;


float lat[numbCity] = {63.3833,62.7000,62.4000,63.8333,61.4667,61.1333,62.6833,61.4167,60.5167,63.0500,60.2167,61.0000,60.1667,60.8667,61.9667,61.0333,60.3167,63.5667,61.1833,62.6667,62.1000,63.0167,61.7333,61.9500,62.1667,68.3500,68.6167,65.7833,67.7000,66.8000,66.5667,67.3667,65.0333,64.2833,65.9667,64.9333};
float lon[numbCity] = {24.2167,22.8333,25.6833,23.1167,21.8000,21.5000,22.8167,23.5833,22.2667,21.7667,24.6667,24.4500,24.9333,26.7000,25.6667,28.1333,24.9667,27.1833,28.7667,29.6333,30.1333,27.8000,27.3000,28.9500,27.8667,23.4167,27.4167,24.5833,24.8500,24.0000,25.8333,26.6500,24.8000,27.6833,29.1833,25.3667};

float cdata[3*36];

/*
 Ahtari 	63.3833	24.2167
 Ilmajoki 	62.7000	22.8333
 JyvŠskylŠ 	62.4000	25.6833
 Kokkola (Karleby) 	63.8333	23.1167
 Pori 	61.4667	21.8000
 Rauma 	61.1333	21.5000
 SeinŠjoki 	62.6833	22.8167
 Tampere 	61.4167	23.5833
 Turku 	60.5167	22.2667
 Vaasa (Vasa) 	63.0500	21.7667
 
 
 Espoo 	60.2167	24.6667
 HŠmeenlinna 	61.0000	24.4500
 Helsinki 	60.1667	24.9333
 Kouvola 	60.8667	26.7000
 Lahti 	61.9667	25.6667
 Lappeenranta 	61.0333	28.1333
 Vantaa (Vaarala) 	60.3167	24.9667
 
 
 Iisalmi (Idensalmi) 	63.5667	27.1833
 Imatra 	61.1833	28.7667
 Joensuu 	62.6667	29.6333
 Kitee 	62.1000	30.1333
 Kuopio 	63.0167	27.8000
 Mikkeli 	61.7333	27.3000
 Savonlinna 	61.9500	28.9500
 Varkaus 	62.1667	27.8667
 
 Enontekiš 	68.3500	23.4167
 Ivalo 	68.6167	27.4167
 Kemi 	65.7833	24.5833
 KittilŠ 	67.7000	24.8500
 Pello 	66.8000	24.0000
 Rovaniemi 	66.5667	25.8333
 SodankylŠ 	67.3667	26.6500
 
 Hailuoto 	65.0333	24.8000
 Kajaani 	64.2833	27.6833
 Kuusamo 	65.9667	29.1833
 Oulu (UleŒborg) 	64.9333	25.3667
 
 */

void testApp::readRaw(string filename)
{
	FILE *f = fopen(ofToDataPath(filename).c_str(), "rb");
	if (f == NULL)
		ofLog(OF_LOG_ERROR, "cannot open " + filename);
	// read item count to variable i
	int i;
	int meszaros=0;
	while (fread(&i, sizeof(int), 1, f)  > 0)
	{
		float dist=0.0;
		Path2D pntpath;
		// read i points
		
		Vector2D pnt,opnt;
		for (int j = 0; j < i; j++)
		{
			fread(pnt.arr(), sizeof(float), 2, f);
			// transform point
			float t = pnt.y;
			pnt.y = pnt.x;
			pnt.x = t;
			pnt.x -= 19;
			pnt.y = 71 - pnt.y;
			dist+=sqrt((opnt.x-pnt.x)*(opnt.x-pnt.x)+(opnt.y-pnt.y)*(opnt.y-pnt.y));
			opnt=pnt;

			// add it to path
			pntpath.path.push_back(pnt);
		}
		// add path to object
		//meszaros=(meszaros+1)%1;
		//if(!meszaros){
			if(dist>2.0){
				object.push_back(pntpath);
			}
		//}
	}
	fclose(f);
}

//--------------------------------------------------------------
void testApp::setup()
{
	
	
	//osc
	receiver.setup( PORT );
	
	//ofSetFrameRate(.01);
	glDisable(GL_DEPTH_TEST);
	readRaw("fin_raw.dat");
 
    glEnable(GL_BLEND); // enable GL blending
	
	glBlendFunc(GL_SRC_COLOR, GL_ONE_MINUS_SRC_ALPHA);
	ofBackground(255, 255, 255);
	
	ofEnableAlphaBlending();
	
	genList = glGenLists(1);
	glNewList(genList, GL_COMPILE);
	glEnable(GL_VERTEX_PROGRAM_POINT_SIZE);
	
	/*
	 
	 ///90fok forgat
	glRotated(-90., 0.0, 0.0, 1.0);
	float x = -1000 -ofGetScreenHeight()/2.0 + 1000/2.0;
	float y = ofGetScreenWidth()/2.0 - 1200/2.0;
	glTranslated(x,y, 0.0);
	 
	 */
	
	float scale = 50;
	glLineWidth(1);
	ossz=0;
	
	for (int i = 0; i < object.size(); i++)
	{
		
		glBegin(GL_LINE_STRIP);
		for (int n = 0; n < object[i].path.size(); n++)
		{
			
			float x = object[i].path[n].x * scale;
			float y = object[i].path[n].y * scale * 2.2;
			
			
			/*
			for (int m = 0; m<1; m++) {
				int rnd1 = ofRandom(0,0);
				int rnd2 = ofRandom(0,0);
				float xx = mouseX+rnd1;//long2int(koord[m].lat,koord[m].longi)*scale;
				float yy = mouseY+rnd2;//lat2int(koord[m].lat,koord[m].longi)*scale*1.4;
				float d = sqrt((x - xx) * (x - xx) + (y - yy) * (y - yy));
				float dmax = 200;
				float dpi = M_PI * d / 2.0 / dmax;
				float f = 0;
				if (d < dmax)
				{
					float c = cos(dpi);
					f = c * c * c ;
				}
				glColor4f(0, 0, 0, (1-f)/2+.2);
				x=(x + f * (x - xx));
				y=(y + f * (y - yy));
			}
			//end of bujat's transformation
			
			*/
			
			
			glVertex2f(x,y);
			ossz+=1;
		}		
		glEnd();
		
	}
	
	
	
	for (int i = 0; i<36; i++) {
		
		lon[i];
		Vector2D point;
		point.x = lon[i];
		point.y = lat[i];
		point.x -= 19.0;
		point.y = 71.0 - lat[i];
		point.x *= scale;
		point.y *= scale*2.2;
		
		cdata[3*i]=point.x;
		cdata[3*i+1]=point.y;
		cdata[3*i+2]=0;
	}
	
	
	glEndList();
	
	myShader.setup("myShader");
	myShader.begin();
	
}

//--------------------------------------------------------------
void testApp::update(){
	
	//osc
	
	while( receiver.hasWaitingMessages() )
	{
		ofxOscMessage m;		
		receiver.getNextMessage( &m );
		cdata[m.getArgAsInt32( 0 ) * 3 + 2] += sqrt(m.getArgAsInt32( 1 )/15.0)*4.0;
	}
}


float lat2int(float lat, float longi){

	return 60-longi;
}
float long2int(float lat, float longi){
	
	return lat-19;
}
float sc=0.7;

void testApp::draw(){
	for (int i=0; i<36; i++) {
		cdata[i*3+2]=(100.0*cdata[i*3+2]+0)/101.0;
	}
	//cout << ofGetFrameRate() <<" "<<ossz<<" "<<object.size()<< endl;
	
		myShader.setUniform3f("mouse", mouseX/sc, mouseY/sc, 1.0);
	
		myShader.setUniform3fv("points", cdata, 36);
	
	
	
		glClear(GL_COLOR_BUFFER_BIT);
		glPushMatrix();
		glScalef(sc, sc, 1.0);
		glCallList(genList);
		glPopMatrix();
	
}

//--------------------------------------------------------------
void testApp::keyPressed(int key){
	cout << "saved";
	ofSaveFrame();
}

//--------------------------------------------------------------
void testApp::keyReleased(int key){

}

//--------------------------------------------------------------
void testApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void testApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void testApp::windowResized(int w, int h){

}
