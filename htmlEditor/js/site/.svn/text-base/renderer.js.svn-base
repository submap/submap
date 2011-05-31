//render the transformed object on the canvas, in a non blocking way
//implemented with inner timer
// canvasContext: 2d canvas context to draw into it
// loader: loader gif, the renderer sign it's working with it to the ui
// content: iterator over the content, must implement reset, next, and eof functions
function createRenderer(canvasContext,showLoader,content){
	var that={};

	// true if we are drawing actualy
	var duringRender=false;

	//inner timer for the drawing loop
	var timer;

	//inner loop
	function loop(){
		if(!content.eof()){
			//there is more to draw
			content.next(canvasContext);
			if(!content.eof()){
				showLoader(true);
			}
		}else{
			//drawing is over
			stopLoop();
			showLoader(false);
		}
	}

	//stop the inner loops timer
	function stopLoop(){
		if(duringRender){
			clearInterval(timer);
			duringRender=false;
		}
	}
	//start the inner loops timer
	function startLoop(){
		if(!duringRender){
			timer=setInterval(loop,20);
			duringRender=true;
		}
	}
	
	//starting the rendering
	that.startRender = function(a){
		content.reset();
		startLoop();
	}
	return that;
}
