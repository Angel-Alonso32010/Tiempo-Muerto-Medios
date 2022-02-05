$(document).ready(function() {
 
    $(".paises li").click(cambiarColor);
   
  });
   
  function cambiarColor(){
     $(this).addClass("rojo");
  }