function createTransformer(content){
    var that={};
    var markers=Array();
    var points=Array();
    function transform(mihez,pont){
            var d=Math.sqrt((pont[0]-mihez[0])*(pont[0]-mihez[0])+(pont[1]-mihez[1])*(pont[1]-mihez[1]));
            /*
            var f=0;
            if(d<200){
                f= (-1*Math.abs(d-100)+100)*0.005;
            }*/
            //bujat's transformation
            var dmax=5000;
            var dpi=Math.PI*d/2/dmax;
            var f=0;
            if(d<dmax){
				f=Math.cos(dpi)*Math.cos(dpi)*Math.cos(dpi);
            }
            //end of bujat's transformation
            pont[0]=pont[0]+f*(pont[0]-mihez[0]);
            pont[1]=pont[1]+f*(pont[1]-mihez[1]);
            return pont;
    }
    function fromGeoToScreen(pont){
        return [(pont[1]-18.926844)/(19.333912-18.926844)*(16043.822-20.834)+20.834,
                (pont[0]-47.612461)/(47.351501-47.612461)*(15266.775-74.981)+74.981];
        
//		boundarybox.push([20.834,74.981]);
//		boundarybox.push([16043.822,15266.775]);

//        return [(pont[1]-18.929443359375)/(19.331817626953125-18.929443359375)*500,
//                (pont[0]-47.60894068308017)/(47.35091945348443-47.60894068308017)*500];
    }
    function refreshPoints(){
        points=Array();
        for(var i=0;i<markers.length;i++){
            pont=fromGeoToScreen(markers[i].point());
            for(var j=0;j<i;j++){
                pont=transform(points[j],pont);
            }
            points.push(pont);
        }
    }
    that.recalculate=function(){
        scale=1;
        ofsx=0;
        ofsy=0;
        refreshPoints();
        that.trans=function(rpont){
            tpont=Array();
            tpont[0]=rpont[0];
            tpont[1]=rpont[1];
            jQuery.each(points,function(index,transpont){
                tpont=transform(transpont,tpont);
            });
            return [tpont[0]*scale+ofsx,tpont[1]*scale+ofsy];
        };
        var boundary=content.calculateBoundary();
        
        boundary.xdif=boundary.maxx-boundary.minx;
        boundary.ydif=boundary.maxy-boundary.miny;
        scale=Math.min(that.width/boundary.xdif,that.height/boundary.ydif);
        ofsy=(that.height-boundary.ydif*scale)/2-boundary.miny*scale;
        ofsx=(that.width-boundary.xdif*scale)/2-boundary.minx*scale;
    };
    that.resetMarker=function(){
        makers=Array();
    };
    that.pushMarker=function(marker){
        markers.push(marker);
    };
    that.trans=function(pont){
        return [pont[0],pont[1]];
    };
    return that;
};
