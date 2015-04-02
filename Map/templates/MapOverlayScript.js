//function post(path, params, method) {
//    method = method || "post";
//    
//    var form = document.createElement("form");
//    form.setAttribute("method", method);
//    form.setAttribute("action", path);
//    
//    for (var key in params) {
//        if(params.hasOwnPropery(key)) {
//            var hiddenField = document.createElement("input");
//            hiddenField.setAttribute("type", "hidden");
//            hiddenField.setAttribute("name", key);
//            hiddenField.setAttribute("value", params[key]);
//            form.appendChild(hiddenField);
//        }
//    }
//    document.body.appendChild(form);
//    form.submit();
//}
        
function printmessage(message) {
    var node = document.createElement("li");
    var textnode = document.createTextNode(message);
    node.appendChild(textnode);
    
    document.getElementById("errorbox").appendChild(node);
}

function arrow(up) {
    if (up) {
        return "<img src=\"http://i.imgur.com/KC9vWSc.png\">"
    } else {
        return "<img src=\"http://i.imgur.com/qazLBjq.png\">"
    }
}
        
function initialize() {
    var json = $.getJSON("data.json").done(function () {showMap(json);});
map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}

var mapOptions = {
    zoom: 18
};
        
var map;
        
var prevupdate = null;

var beacon = new google.maps.Marker({
        position: null,
        title: 'True beacon position',
        icon: 'http://i.imgur.com/AOm4N8n.png'
    });
        
var beaconGuess = new google.maps.Marker({
        position: null,
        title: 'Guessed beacon position',
        icon: 'http://i.imgur.com/9wox1aO.png'
    });
        
var beaconPolygon = new google.maps.Polygon({
       paths: [],
        strokeColor: '#00FF00',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#00FF00',
        fillOpacity: 0.35
    });
        
var antenna1 = new google.maps.Marker({
        position: null,
        title: 'Tracker one position',
        icon: 'http://i.imgur.com/kN8u5cm.png'
    });
        
var antenna2 = new google.maps.Marker({
        position: null,
        title: 'Tracker two position',
        icon: 'http://i.imgur.com/kN8u5cm.png'
    });
        
var antenna3 = new google.maps.Marker({
        position: null,
        title: 'Tracker three position',
        icon: 'http://i.imgur.com/kN8u5cm.png'
    });

var t1ang = new google.maps.Polyline({
        path: [],
        strokeColor: '#FF0000',
        strokeOpacity: 0.5,
        strokeWeight: 2
    });

var t2ang = new google.maps.Polyline({
        path: [],
        strokeColor: '#FF0000',
        strokeOpacity: 0.5,
        strokeWeight: 2
    });

var t3ang = new google.maps.Polyline({
        path: [],
        strokeColor: '#FF0000',
        strokeOpacity: 0.5,
        strokeWeight: 2
    });
        
var beaconInfo = new google.maps.InfoWindow({
        content: "<font style=\"font-weight: bold\">True beacon position</font><br/>Loading"
    });
        
var beaconGuessInfo = new google.maps.InfoWindow({
        content: "<font style=\"font-weight: bold\">Guessed beacon position</font><br/>Loading"
});
        
var beaconPolygonInfo = new google.maps.InfoWindow({
       content: "<font style=\"font-weight: bold\">Approximate beacon area</font></br>"
    });
    
var antenna1Info = new google.maps.InfoWindow({
        content: "<font style=\"font-weight: bold\">Tracker one position</font><br/>Loading"
    });
    
var antenna2Info = new google.maps.InfoWindow({
        content: "<font style=\"font-weight: bold\">Tracker two position</font><br/>Loading"
    });

var antenna3Info = new google.maps.InfoWindow({
        content: "<font style=\"font-weight: bold\">Tracker three position</font><br/>Loading"
    });

var controlText = document.createElement('div');
        
function showMap(json) {
    //console.log(json);
    data = JSON.parse(json.responseText);
    //console.log(data);
    
    function DatasetTextbox(controlDiv, map) {
        controlDiv.style.padding = '5px';
        var controlUI = document.createElement('div');
        controlUI.style.backgroundColor = '#fff';
        controlUI.style.border = '2px solid #fff';
        controlUI.style.borderRadius = '3px';
        controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
        controlUI.style.cursor = 'pointer';
        controlUI.style.marginBottom = '5px';
        controlUI.title = 'Dataset';
        controlDiv.appendChild(controlUI);
        
        //var controlText = document.createElement('div');
        controlText.style.color = 'rgb(25,25,25)';
        controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
        controlText.style.fontSize = '16px';
        controlText.style.lineHeight = '18px';
        controlText.style.paddingLeft = '5px';
        controlText.style.paddingRight = '5px';
        controlText.innerHTML = '<center><strong>WIPLS Locator Map<br /> <font style="font-size:80%">Last Update:</strong> ' + data.lastupdate + '</center>';
        controlUI.appendChild(controlText);
        
        updateMap(data, true);
        
        google.maps.event.addDomListener(controlUI, 'click', function() {
            window.open("data.json");
        });
    }

    var datasetTextboxDiv = document.createElement('div');
    var datasetTextbox = new DatasetTextbox(datasetTextboxDiv, map);
    
    datasetTextbox.index = 1;
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(datasetTextboxDiv);
    
    if(data.showbeacon == "false") {
        //printmessage("hiding beacon");
        beacon.setMap(null);
    } else {
        //printmessage("showing beacon");
        beacon.setMap(map);
    }
    if(data.showangles == "false") {
        t1ang.setMap(null);
        t2ang.setMap(null);
        t3ang.setMap(null);
    } else {
        t1ang.setMap(map);
        t2ang.setMap(map);
        t3ang.setMap(map);
    }
    //beacon.setMap(map);
    beaconGuess.setMap(map);
    beaconPolygon.setMap(map);
    antenna1.setMap(map);
    antenna2.setMap(map);
    antenna3.setMap(map);
    
    
    google.maps.event.addListener(beacon, 'click', function() {
        beaconInfo.open(map, beacon); 
    });
    google.maps.event.addListener(beaconGuess, 'click', function() {
        beaconGuessInfo.open(map, beaconGuess); 
    });
    google.maps.event.addListener(beaconPolygon, 'click', function() {
        beaconPolygonInfo.open(map, beaconGuess);
    });
    google.maps.event.addListener(antenna1, 'click', function() {
        antenna1Info.open(map, antenna1); 
    });
    google.maps.event.addListener(antenna2, 'click', function() {
        antenna2Info.open(map, antenna2); 
    });
    google.maps.event.addListener(antenna3, 'click', function() {
        antenna3Info.open(map, antenna3); 
    });
    
}
        
setInterval(refreshData, 5000);
function refreshData() {
    var data = {};
    var json = $.getJSON("data.json").done(function () {
        //showMap(json);
        data = JSON.parse(json.responseText);
        
        //console.log(prevupdate);
        //console.log(data.lastupdate);
        //console.log(prevupdate == data.lastupdate);
        
        if(prevupdate == data.lastupdate) {
            return;
            //Don't refresh unless there is new data
        } else {
            updateMap(data, false);
        }
            
    });
}
        
function updateMap(data, center) {
    beacon.setPosition(new google.maps.LatLng(data.beaconCoords.lat, data.beaconCoords.long));
    beaconGuess.setPosition(new google.maps.LatLng(data.beaconGuessCoords.lat, data.beaconGuessCoords.long));
    antenna1.setPosition(new google.maps.LatLng(data.antenna1Coords.lat, data.antenna1Coords.long));
    antenna2.setPosition(new google.maps.LatLng(data.antenna2Coords.lat, data.antenna2Coords.long));
    antenna3.setPosition(new google.maps.LatLng(data.antenna3Coords.lat, data.antenna3Coords.long));
    if (center) {
        map.setCenter(new google.maps.LatLng(data.beaconGuessCoords.lat, data.beaconGuessCoords.long));
    }
    beaconPolygon.setPath(
        [new google.maps.LatLng(data.guessVector[0].lat, data.guessVector[0].long),
         new google.maps.LatLng(data.guessVector[1].lat, data.guessVector[1].long),
         new google.maps.LatLng(data.guessVector[2].lat, data.guessVector[2].long)]);
    
    var smallConstant = 0.0005
    
    function toRadians(angle) {
        return angle * (Math.PI / 180);
    }
    
    t1ang.setPath(
        [new google.maps.LatLng(data.antenna1Coords.lat, data.antenna1Coords.long),
         new google.maps.LatLng(
             data.antenna1Coords.lat + smallConstant * Math.sin(toRadians(data.antenna1Coords.phi)),
             data.antenna1Coords.long + smallConstant * Math.cos(toRadians(data.antenna1Coords.phi))
         )]);
    t2ang.setPath(
        [new google.maps.LatLng(data.antenna2Coords.lat, data.antenna2Coords.long),
         new google.maps.LatLng(
             data.antenna2Coords.lat + smallConstant * Math.sin(toRadians(data.antenna2Coords.phi)),
             data.antenna2Coords.long + smallConstant * Math.cos(toRadians(data.antenna2Coords.phi))
         )]);
    t3ang.setPath(
        [new google.maps.LatLng(data.antenna3Coords.lat, data.antenna3Coords.long),
         new google.maps.LatLng(
             data.antenna3Coords.lat + smallConstant * Math.sin(toRadians(data.antenna3Coords.phi)),
             data.antenna3Coords.long + smallConstant * Math.cos(toRadians(data.antenna3Coords.phi))
         )]);
    
    beaconCoords = new google.maps.LatLng(data.beaconCoords.lat, data.beaconCoords.long);
    var beaconGuessCoords = new google.maps.LatLng(data.beaconGuessCoords.lat, data.beaconGuessCoords.long);
    var beaconPolygonCoords = [
        new google.maps.LatLng(data.guessVector[0].lat, data.guessVector[0].long),
        new google.maps.LatLng(data.guessVector[1].lat, data.guessVector[1].long),
        new google.maps.LatLng(data.guessVector[2].lat, data.guessVector[2].long)
    ];
    var antenna1Coords = new google.maps.LatLng(data.antenna1Coords.lat, data.antenna1Coords.long);
    var antenna2Coords = new google.maps.LatLng(data.antenna2Coords.lat, data.antenna2Coords.long);
    var antenna3Coords = new google.maps.LatLng(data.antenna3Coords.lat, data.antenna3Coords.long);
    
    beaconInfo.setContent("<font style=\"font-weight: bold\">True beacon position</font><br/>"+
        beaconCoords.lat().toFixed(4) + ", " + beaconCoords.lng().toFixed(4));
    beaconGuessInfo.setContent("<font style=\"font-weight: bold\">Guessed beacon position</font><br/>" +
        beaconGuessCoords.lat().toFixed(4) + ", " + beaconGuessCoords.lng().toFixed(4));
    antenna1Info.setContent("<font style=\"font-weight: bold\">Tracker one position</font><br/>"+
        antenna1Coords.lat().toFixed(4) + ", " + antenna1Coords.lng().toFixed(4));
    antenna2Info.setContent("<font style=\"font-weight: bold\">Tracker two position</font><br/>"+
        antenna2Coords.lat().toFixed(4) + ", " + antenna2Coords.lng().toFixed(4));
    antenna3Info.setContent("<font style=\"font-weight: bold\">Tracker three position</font><br/>"+
        antenna3Coords.lat().toFixed(4) + ", " + antenna3Coords.lng().toFixed(4));
    controlText.innerHTML = '<center><strong>WIPLS Locator Map<br /> <font style="font-size:80%">Last Update:</strong> ' + data.lastupdate + '</center>';
    
    document.getElementById("t1lat").innerHTML = antenna1Coords.lat().toFixed(6);
    document.getElementById("t1lng").innerHTML = antenna1Coords.lng().toFixed(6);
    document.getElementById("t1ele").innerHTML = data.antenna1Coords.ele.toFixed(6);
    document.getElementById("t2lat").innerHTML = antenna2Coords.lat().toFixed(6);
    document.getElementById("t2lng").innerHTML = antenna2Coords.lng().toFixed(6);
    document.getElementById("t2ele").innerHTML = data.antenna2Coords.ele.toFixed(6);
    document.getElementById("t3lat").innerHTML = antenna3Coords.lat().toFixed(6);
    document.getElementById("t3lng").innerHTML = antenna3Coords.lng().toFixed(6);
    document.getElementById("t3ele").innerHTML = data.antenna3Coords.ele.toFixed(6);
    document.getElementById("blat").innerHTML = beaconGuessCoords.lat().toFixed(6);
    document.getElementById("blng").innerHTML = beaconGuessCoords.lng().toFixed(6);
    document.getElementById("bele").innerHTML = data.beaconGuessCoords.ele.toFixed(6);
    
    document.getElementById("t1status").innerHTML = data.antenna1Coords.status == 1 ? arrow(true) : arrow(false);
    document.getElementById("t2status").innerHTML = data.antenna2Coords.status == 1 ? arrow(true) : arrow(false);
    document.getElementById("t3status").innerHTML = data.antenna3Coords.status == 1 ? arrow(true) : arrow(false);
    
    if(data.showbeacon == "false") {
        //printmessage("hiding beacon");
        beacon.setMap(null);
    }
    else {
        //printmessage("showing beacon");
        beacon.setMap(map);
    }
    
    printmessage(data.lastupdate + ": Map Updated");
    prevupdate = data.lastupdate;

    // print error messages
    /*if (data.error != "") {
        errors = data.error.split("!");
        for (var i = 0; i < errors.length; i++) {
            printmessage(errors[i]);
        }
    }*/
}

google.maps.event.addDomListener(window, 'load', initialize);
