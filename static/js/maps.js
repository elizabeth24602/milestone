function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3,
        center: {
            lat: 55.3781,
            lng: 3.4360
        }
    });
    let labels = "ABCDEFGHIJKLMONPQRSTUVWXYZ";
    let locations = [{
        lat: 52.0339,
        lng: -2.4236
    }];
    let markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });
    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}