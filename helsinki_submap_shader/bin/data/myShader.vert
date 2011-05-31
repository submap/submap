uniform vec3 mouse;
uniform vec3 hels;

uniform vec3 points[36];
void main() {
    vec4 vertex =gl_Vertex;
	gl_PointSize=1.0;

	for (int i=0; i<36; i++) {
	
		float dist=distance(vertex.xy,points[i].xy);
		float dmax = 200.0 * (points[i].z);
		
		float f = 0.0;
		if (dist < dmax)
		{
			vec2 vektor=points[i].xy-vertex.xy;
			
			float dpi = 1.5707963268 * dist / dmax ;
			
			float c = cos(dpi + 3.14159265  );
			f = c*c*c*points[i].z;
			vertex.xy=vertex.xy+vektor*f;
		}
	}
		
			
    gl_Position = gl_ModelViewProjectionMatrix * vertex;
} 
