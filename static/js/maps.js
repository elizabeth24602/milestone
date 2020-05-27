function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: {lat: 52.0559, lng: -2.7175}
    });
    let labels = "ABCDEFGHIJKLMONPQRSTUVWXYZ";
    let locations = [new google.maps.LatLng(52.0339, -2.4236)];
    let markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            map: map,
            label: labels[i % labels.length]
        });
    });
    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}