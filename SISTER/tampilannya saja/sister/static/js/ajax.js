//window.alert("yuhuuu");
function create_vm() {
  //window.location.href = 'hasil.php';
	//window.alert("yuhuu");

	$.ajax({
		url: '/create',
		data: $('form').serialize(),
		type: 'POST',
		success: function(response){
			window.alert("sukses");
			window.location.href = 'app.py'
			console.log(response);
			//window.location

		},
		error: function(error){
			console.log(error);
		}
	 });
 };

 /*$(function create_vm(){
	 window.alert("test");
 	$('#btnSignUp').click(function(){

 		$.ajax({
 			url: '/signUp',
 			data: $('form').serialize(),
 			type: 'POST',
 			success: function(response){
 				console.log(response);
 			},
 			error: function(error){
 				console.log(error);
 			}
 		});
 	});
});*/
