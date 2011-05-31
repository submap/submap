    function initialize() {
      if (GBrowserIsCompatible()) {
	    var canvas = document.getElementById('canvas');  
       	var ctx = canvas.getContext('2d');  
	    var cont=createBPContent();
	    function showLoader(bool){
		    if(bool)
		    {
			    $("#loader").show();
		    }
		    else
		    {
          $("#loader").hide();
		    }
	    }
	    var rend=createRenderer(ctx,showLoader,cont);
	    rend.startRender();

	    var map = new GMap2(document.getElementById("mapcanvas"));
      var center = new GLatLng(47.49859, 19.064369);
	    map.setCenter(center, 12);
	    map.setMapType(G_HYBRID_MAP);
        var transform=createTransformer(cont);
        transform.width=$("#canvas").width();
        transform.height=$("#canvas").height();
        function markerDragEnd(){
            transform.recalculate();
            rend.startRender();
        };
      $("#addmarker").click(function(){
  	    transform.pushMarker( createMarker(map,markerDragEnd) );        
        markerDragEnd();
      });
      transform.recalculate();
      cont.transform=transform.trans;
      }
      $
    }

