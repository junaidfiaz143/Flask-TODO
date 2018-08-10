$(document).ready(function(){

	$('form').on('submit', function(event){
		$.ajax({
			data : {
				title : $('#titleInput').val(),
				description : $('#descriptionInput').val() 
			}, 
			type : 'POST',
			url: '/process'
		}).done(function(data){
				if(data.error){
					$('#errorAlert').text(data.error).show();
					$('#successAlert').hide();
				}else{
					$('#successAlert').text(data.title).show();
					$('#errorAlert').hide();
				}
			});
	event.preventDefault();
	});

});