$(document).read(function(){

	$('form').on('submit', function(event){
		$.ajax({
			data : {
				title : $('#titleInput'),
				description : $('#descriptionInput'): 
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