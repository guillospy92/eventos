$(function(){
		

		jQuery("#slider").backstretch([
        "http://princzz.galeon.com/fc.jpg",
         "http://www.informatico-madrid.com/bundles/joaoimweb/img/carousel/fondoOfertaWeb3.jpg",
          "http://ipadbooks.contrataweb.com/wp-content/uploads/2012/08/Hechizo.jpg"

    ], {duration: 3000, fade: 1000});
		});


$(function(){
		

		jQuery("#sliders").backstretch([

         "http://www.informatico-madrid.com/bundles/joaoimweb/img/carousel/fondoOfertaWeb3.jpg",
          "http://ipadbooks.contrataweb.com/wp-content/uploads/2012/08/Hechizo.jpg"

    ], {duration: 3000, fade: 1000});
		});




$('select').on('change', cambiar);
function cambiar(){

var id = $(this).val()
console.log(id);

}





