<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>지도 생성하기</title>

</head>
<body>

<div id="container">
<div id="mapWrapper">

<!-- 지도를 표시할 div 입니다 -->
<div id="map" style="width:100%;height:585px;"></div>

</div>
<!-- 로드뷰 -->
<!-- <div id="roadview" style="width:100%;height:350px;"></div>


</div> -->
<div id="result">

</div>
<div id="tmp_div"></div>
<div id="dataPool">
	<div id="map_center">
		<input type="hidden" id="center_lat" />
		<input type="hidden" id="center_lng" />
		<input type="hidden" id="tmp_value" />
	</div>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.1/jquery.validate.js"></script>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=034b088099b3f73d6f7a1df2f8d71f9a&libraries=services,clusterer,drawing"></script>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=034b088099b3f73d6f7a1df2f8d71f9a"></script>
<script>









var tmp_div = $("#tmp_div");
var go_py_result = "";
var go_py_result2 = "";

var center_lat = $('#center_lat');
var center_lng = $('#center_lng');

var geocoder = new kakao.maps.services.Geocoder();

// marker생성시 markerList에 담기. (마커 모두 삭제시 필요)
var markerList = new Array();
var infowindowList = new Array();
var infowindow = new kakao.maps.InfoWindow({
    content: '<div style="width:150px;text-align:center;padding:6px 0;">우리회사</div>'
});



function removeMarkers(){	//마커 전부 삭제하는 메소드
	for(var i=0; i < markerList.length; i++){
		markerList[i].setMap(null);
	}
	markerList = [];
};

//인포윈도우지우기
function removeInfowindows(){
	for(var i=0; i < infowindowList.length; i++){
		infowindowList[i].close();
	}
	infowindowList = [];
}




 var mapContainer = document.getElementById('map'), // 지도를 표시할 div
mapOption = {
    center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
    level: 3 // 지도의 확대 레벨
};

//지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

//일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도에 컨트롤을 추가해야 지도위에 표시됩니다
// kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

var iwContent = '<div style="padding:5px;">Hello World!</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
iwPosition = new kakao.maps.LatLng(33.450701, 126.570667), //인포윈도우 표시 위치입니다
iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

//인포윈도우를 생성하고 지도에 표시합니다
/* var infowindow = new kakao.maps.InfoWindow({
map: map, // 인포윈도우가 표시될 지도
position : iwPosition,
content : iwContent,
removable : iwRemoveable
}); */




//지도에 마커를 표시하는 함수입니다
function displayMarker(place) {

    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
    });



    //*** 마커 담기
    markerList.push(marker)




    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
}













//지도 중심 좌표
var center_latlng = map.getCenter();
var current_level = map.getLevel();






//지도가 이동, 확대, 축소로 인해 중심좌표가 변경되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'center_changed', function() {

    // 지도의  레벨을 얻어옵니다
    current_level = map.getLevel();

    // 지도의 중심좌표를 얻어옵니다
    center_latlng = map.getCenter();

    var message = '<p>지도 레벨은 ' + current_level + ' 이고</p>';
    message += '<p>중심 좌표는 위도 ' + center_latlng.getLat() + ', 경도 ' + center_latlng.getLng() + '입니다</p>';

    var resultDiv = document.getElementById('result');
    //resultDiv.innerHTML = message;
    center_lat.val(center_latlng.getLat());
    center_lng.val(center_latlng.getLng());
});



// var tmp_div = $('#tmp_div');
// tmp_div.appe




// 거리계산 활용? polyline.getlength?
/* const polyline = new window.daum.maps.Polyline({
	map : map,
	path : [
		new window.daum.maps.LatLng(center_latlng.getLat(), center_latlng.getLng()),
		new window.daum.maps.LatLng(center_latlng.getLat(), center_latlng.getLng())
	],
	strokeWeight : 0
}); */



















/*var overlayOn = true , // 지도 위에 로드뷰 오버레이가 추가된 상태를 가지고 있을 변수
container = document.getElementById('container'), // 지도와 로드뷰를 감싸고 있는 div 입니다
mapWrapper = document.getElementById('mapWrapper'), // 지도를 감싸고 있는 div 입니다
mapContainer = document.getElementById('map'), // 지도를 표시할 div 입니다
rvContainer = document.getElementById('roadview'); //로드뷰를 표시할 div 입니다

var mapCenter = new kakao.maps.LatLng(33.45042 , 126.57091), // 지도의 중심좌표
mapOption = {
    center: mapCenter, // 지도의 중심좌표
    level: 3 // 지도의 확대 레벨
};

//지도를 표시할 div와 지도 옵션으로 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);
















//마커를 표시할 위치와 title 객체 배열입니다
var positions = [
    {
        title: '카카오',
        latlng: new kakao.maps.LatLng(33.450705, 126.570677)
    },
    {
        title: '생태연못',
        latlng: new kakao.maps.LatLng(33.450936, 126.569477)
    },
    {
        title: '텃밭',
        latlng: new kakao.maps.LatLng(33.450879, 126.569940)
    },
    {
        title: '근린공원',
        latlng: new kakao.maps.LatLng(33.451393, 126.570738)
    }
];

// 마커 이미지의 이미지 주소입니다
var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

for (var i = 0; i < positions.length; i ++) {

    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);

    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });
}















//로드뷰 객체를 생성합니다
var rv = new kakao.maps.Roadview(rvContainer);

//좌표로부터 로드뷰 파노라마 ID를 가져올 로드뷰 클라이언트 객체를 생성합니다
var rvClient = new kakao.maps.RoadviewClient();

//로드뷰에 좌표가 바뀌었을 때 발생하는 이벤트를 등록합니다
kakao.maps.event.addListener(rv, 'position_changed', function() {

// 현재 로드뷰의 위치 좌표를 얻어옵니다
var rvPosition = rv.getPosition();

// 지도의 중심을 현재 로드뷰의 위치로 설정합니다
map.setCenter(rvPosition);

// 지도 위에 로드뷰 도로 오버레이가 추가된 상태이면
if(overlayOn) {
    // 마커의 위치를 현재 로드뷰의 위치로 설정합니다
    marker.setPosition(rvPosition);
}
});

//마커 이미지를 생성합니다
var markImage = new kakao.maps.MarkerImage(
'https://t1.daumcdn.net/localimg/localimages/07/2018/pc/roadview_minimap_wk_2018.png',
new kakao.maps.Size(26, 46),
{
    // 스프라이트 이미지를 사용합니다.
    // 스프라이트 이미지 전체의 크기를 지정하고
    spriteSize: new kakao.maps.Size(1666, 168),
    // 사용하고 싶은 영역의 좌상단 좌표를 입력합니다.
    // background-position으로 지정하는 값이며 부호는 반대입니다.
    spriteOrigin: new kakao.maps.Point(705, 114),
    offset: new kakao.maps.Point(13, 46)
}
);

//드래그가 가능한 마커를 생성합니다
var marker = new kakao.maps.Marker({
image : markImage,
position: mapCenter,
draggable: true
});

//마커에 dragend 이벤트를 등록합니다
kakao.maps.event.addListener(marker, 'dragend', function(mouseEvent) {

// 현재 마커가 놓인 자리의 좌표입니다
var position = marker.getPosition();

// 마커가 놓인 위치를 기준으로 로드뷰를 설정합니다
toggleRoadview(position);
});

//지도에 클릭 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'click', function(mouseEvent){

// 지도 위에 로드뷰 도로 오버레이가 추가된 상태가 아니면 클릭이벤트를 무시합니다
if(!overlayOn) {
    return;
}

// 클릭한 위치의 좌표입니다
var position = mouseEvent.latLng;

// 마커를 클릭한 위치로 옮깁니다
marker.setPosition(position);

// 클락한 위치를 기준으로 로드뷰를 설정합니다
toggleRoadview(position);
});

//전달받은 좌표(position)에 가까운 로드뷰의 파노라마 ID를 추출하여
//로드뷰를 설정하는 함수입니다
function toggleRoadview(position){
rvClient.getNearestPanoId(position, 50, function(panoId) {
    // 파노라마 ID가 null 이면 로드뷰를 숨깁니다
    if (panoId === null) {
        toggleMapWrapper(true, position);
    } else {
     toggleMapWrapper(false, position);

        // panoId로 로드뷰를 설정합니다
        rv.setPanoId(panoId, position);
    }
});
}

//지도를 감싸고 있는 div의 크기를 조정하는 함수입니다
function toggleMapWrapper(active, position) {
if (active) {

    // 지도를 감싸고 있는 div의 너비가 100%가 되도록 class를 변경합니다
    container.className = '';

    // 지도의 크기가 변경되었기 때문에 relayout 함수를 호출합니다
    map.relayout();

    // 지도의 너비가 변경될 때 지도중심을 입력받은 위치(position)로 설정합니다
    map.setCenter(position);
} else {

    // 지도만 보여지고 있는 상태이면 지도의 너비가 50%가 되도록 class를 변경하여
    // 로드뷰가 함께 표시되게 합니다
    if (container.className.indexOf('view_roadview') === -1) {
        container.className = 'view_roadview';

        // 지도의 크기가 변경되었기 때문에 relayout 함수를 호출합니다
        map.relayout();

        // 지도의 너비가 변경될 때 지도중심을 입력받은 위치(position)로 설정합니다
        map.setCenter(position);
    }
}
}

//지도 위의 로드뷰 도로 오버레이를 추가,제거하는 함수입니다
function toggleOverlay(active) {
if (active) {
    overlayOn = true;

    // 지도 위에 로드뷰 도로 오버레이를 추가합니다
    map.addOverlayMapTypeId(kakao.maps.MapTypeId.ROADVIEW);

    // 지도 위에 마커를 표시합니다
    marker.setMap(map);

    // 마커의 위치를 지도 중심으로 설정합니다
    marker.setPosition(map.getCenter());

    // 로드뷰의 위치를 지도 중심으로 설정합니다
    toggleRoadview(map.getCenter());
} else {
    overlayOn = false;

    // 지도 위의 로드뷰 도로 오버레이를 제거합니다
    map.removeOverlayMapTypeId(kakao.maps.MapTypeId.ROADVIEW);

    // 지도 위의 마커를 제거합니다
    marker.setMap(null);
}
}

//지도 위의 로드뷰 버튼을 눌렀을 때 호출되는 함수입니다
function setRoadviewRoad() {
var control = document.getElementById('roadviewControl');

// 버튼이 눌린 상태가 아니면
if (control.className.indexOf('active') === -1) {
    control.className = 'active';

    // 로드뷰 도로 오버레이가 보이게 합니다
    toggleOverlay(true);
} else {
    control.className = '';

    // 로드뷰 도로 오버레이를 제거합니다
    toggleOverlay(false);
}
}

//로드뷰에서 X버튼을 눌렀을 때 로드뷰를 지도 뒤로 숨기는 함수입니다
function closeRoadview() {
var position = marker.getPosition();
toggleMapWrapper(true, position);
} */
</script>
</body>
</html>
