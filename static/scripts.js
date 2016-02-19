function ShowModal(lat, long, logo, amount, description, address){
  $(".modal-header img").attr("src", "https://maps.googleapis.com/maps/api/staticmap?center=" + lat + "," + long + "&zoom=18&size=600x400&maptype=roadmap&markers=" + lat + "," + long + "&key=AIzaSyCUyBouO49GjpyX_gDI8FyZma6qA33f7qU");
  $(".modal-body img").attr("src", logo);
  $(".modal-body h3").html("&pound;" + amount);
  $(".modal-body h1").text(description);
  $(".modal-body p").text(address);
  $('#myModal').modal('show');
}
