// $(document).ready(function(){

// document.getElementById('id_transakcja_1').addEventListener('click', function() {alert(x);});
// document.getElementById('klik').addEventListener('click', function() {document.getElementById('rodzaj').innerHTML = "działa";});
// });

// function Wyznacz() {
	// var x = $('#id_transakcja_1').is(':checked');
	// $('#id_transakcja_1').click(function() {alert(x);})
// }

function Dodaj_pole() {
	var x = $('#id_rodzaj').val();
	if (x == 'M') {
		$('label[for="id_rodzaj_zabudowy"]').css('display', 'inline-block');
		$('#id_rodzaj_zabudowy').css('display', 'inline-block');

		$('label[for="id_typ_domu"]').css('display', 'none');
		$('#id_typ_domu').css('display', 'none');
		$('#id_typ_domu').val('D');

		$('label[for="id_komercyjne"]').css('display', 'none');
		$('#id_komercyjne').css('display', 'none');
		$('#id_komercyjne').val('D');

		$('label[for="id_typ_dzialki"]').css('display', 'none');
		$('#id_typ_dzialki').css('display', 'none');
		$('#id_typ_dzialki').val('D');
	
	} else if (x == 'Domy') {
			$('label[for="id_typ_domu"]').css('display', 'inline-block');
			$('#id_typ_domu').css('display', 'inline-block');

			$('label[for="id_rodzaj_zabudowy"]').css('display', 'none');
			$('#id_rodzaj_zabudowy').css('display', 'none');
			$('#id_rodzaj_zabudowy').val('d');

			$('label[for="id_komercyjne"]').css('display', 'none');
			$('#id_komercyjne').css('display', 'none');
			$('#id_komercyjne').val('D');	

			$('label[for="id_typ_dzialki"]').css('display', 'none');
			$('#id_typ_dzialki').css('display', 'none');
			$('#id_typ_dzialki').val('D');
	
	}
	
	  else if(x == 'K') {
			$('label[for="id_komercyjne"]').css('display', 'inline-block');
			$('#id_komercyjne').css('display', 'inline-block');

			$('label[for="id_rodzaj_zabudowy"]').css('display', 'none');
			$('#id_rodzaj_zabudowy').css('display', 'none');
			$('#id_rodzaj_zabudowy').val('d');

			$('label[for="id_typ_domu"]').css('display', 'none');
			$('#id_typ_domu').css('display', 'none');
			$('#id_typ_domu').val('D');	

			$('label[for="id_typ_dzialki"]').css('display', 'none');
			$('#id_typ_dzialki').css('display', 'none');
			$('#id_typ_dzialki').val('D');
	}

	  else if (x == 'Dz') {
			$('label[for="id_typ_dzialki"]').css('display', 'inline-block');
			$('#id_typ_dzialki').css('display', 'inline-block');

			$('label[for="id_rodzaj_zabudowy"]').css('display', 'none');
			$('#id_rodzaj_zabudowy').css('display', 'none');
			$('#id_rodzaj_zabudowy').val('d');

			$('label[for="id_typ_domu"]').css('display', 'none');
			$('#id_typ_domu').css('display', 'none');
			$('#id_typ_domu').val('D');

			$('label[for="id_komercyjne"]').css('display', 'none');
			$('#id_komercyjne').css('display', 'none');
			$('#id_komercyjne').val('D');	
	}
	  else {
	  		$('label[for="id_rodzaj_zabudowy"]').css('display', 'none');
			$('#id_rodzaj_zabudowy').css('display', 'none');
			$('#id_rodzaj_zabudowy').val('d');

			$('label[for="id_typ_domu"]').css('display', 'none');
			$('#id_typ_domu').css('display', 'none');
			$('#id_typ_domu').val('D');

			$('label[for="id_komercyjne"]').css('display', 'none');
			$('#id_komercyjne').css('display', 'none');
			$('#id_komercyjne').val('D');		

			$('label[for="id_typ_dzialki"]').css('display', 'none');
			$('#id_typ_dzialki').css('display', 'none');
			$('#id_typ_dzialki').val('D');
	  }
}

$('#id_rodzaj').on('change', Dodaj_pole);
$(document).ready(Dodaj_pole);

// $.prettyLoader();
// $(document).ready(function() {
// 	// Po poprawnym załadowaniu strony wyłącza przyciemnienie
// 	$("#przyciemnienie").fadeOut('normal');
// 	$("#przyciemnienie").css('display', 'none');
// 	// Po poprawnym załadowaniu strony wyłącza loading
// 	$("#loading").fadeOut('normal');
// 	$("#loading").css('display', 'none');
// });
               
    //Po kliknięciu w link z clasą loadingOn uruchamia loading
$('#submit').click(function() {
	// $('h2').fadeOut('normal');
	// $('#imglowny').fadeOut('normal');
	$('.stopka').fadeOut('normal');
	$('.stopka2').fadeOut('normal');
	// $('#atrapa').fadeIn('normal');
	$("#imglowny").css('display', 'none');
	$("#atrapa").css('display', 'block');
	$("#przyciemnienie").fadeIn('normal');
	$("#loading").fadeIn('normal');
});

// $(window).on('unload', function() {
// 	// $("#przyciemnienie").css('display', 'none');
// 	// $("#loading").css('display', 'none');
// 	$("#przyciemnienie").fadeOut('normal');
// 	$("#loading").fadeOut('normal');
// });

// $('body').attr('onunload', 'my_function_unload()');

// function my_function_unload() {
//     alert("blah");
//     $("#przyciemnienie").fadeOut('normal');
//     $("#loading").fadeOut('normal');
// }
