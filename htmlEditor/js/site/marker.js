/**
    Creates a new Marker.
    @constructor 
    @param {GMap2} map The map, wich the marker will be attached
    @param {function} callback Function used as an even handler for drag-end event.
*/ 
function createMarker(map,callback){
    /**
      returned value from the constructor
      @public
      @constant
    */
    var that={};
    var startpoint = new GLatLng(47.49859, 19.064369);
    var orangeIcon = new GIcon(G_DEFAULT_ICON);
    orangeIcon.image = "http://www.google.com/intl/en_us/mapfiles/ms/micons/orange-dot.png";
	  orangeIcon.iconSize = new GSize(35, 35);		
	  var marker = new GMarker(startpoint, { icon:orangeIcon, draggable: true } );
    map.addOverlay(marker);
    GEvent.addListener(marker,"dragend",callback);
    /**
       Get the lattitude of the marker.
       @public
    */
    that.lat = function(){
        return marker.getLatLng().lat();
    };
    that.lng = function(){
        return marker.getLatLng().lng();
    };
    that.point = function(){
        return [marker.getLatLng().lat(),marker.getLatLng().lng()];
    };
    return that;
}
