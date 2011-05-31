//create a content iterator for a grid
function createGridContent(){
	var that={};

	var tomb = Array();
	for(x=1;x<500;x+=5){
		tmp=Array();
		for(y=1;y<500;y+=5){
			tmp.push([x,y]);
		}
		tomb.push(tmp);
	}
	for(x=1;x<500;x+=5){
		tmp=Array();
		for(y=1;y<500;y+=5){
			tmp.push([y,x]);
		}
		tomb.push(tmp);
	}

    // transformation function, you may overide it outside of this function
    that.transform=function(pont){
        return [pont[0],pont[1]];
    }
    that.calculateBoundary=function(){
        var boundary={};
        var first=true;
        var leng=tomb.length;
        for(x=0;x<leng;x++){
			for(y=0;y<tomb[x].length;y++){
                pont=that.transform(tomb[x][y]);
				if(first){
                    boundary.minx=pont[0];
                    boundary.maxx=pont[0];
                    boundary.miny=pont[1];
                    boundary.maxy=pont[1];
                    first=false;
                }else{
                   boundary.minx=Math.min(pont[0],boundary.minx);
                   boundary.maxx=Math.max(pont[0],boundary.maxx);
                   boundary.miny=Math.min(pont[1],boundary.miny);
                   boundary.maxy=Math.max(pont[1],boundary.maxy);
                }
			}
		}
        return boundary;
    }

	var cursor=0;
	that.reset=function(){
		cursor=0;
	};
	that.eof=function(){
		return (cursor==tomb.length);
	};
	that.next=function(ctx){
		if(cursor==0){
			ctx.fillStyle = "rgba(255, 0, 0,1)";  
			ctx.fillRect (0, 0, 650, 530);
		}
		var leng=Math.min(tomb.length,cursor+100);
		var x;
		ctx.beginPath();
		for(x=cursor;x<leng;x++){
            pont=that.transform(tomb[x][0]);
			ctx.moveTo(pont[0],pont[1]);
			for(y=1;y<tomb[x].length;y++){
                pont=that.transform(tomb[x][y]);
				ctx.lineTo(pont[0],pont[1]);
			}
		}
		ctx.stroke();
		cursor=x;
	};
	return that;
}
