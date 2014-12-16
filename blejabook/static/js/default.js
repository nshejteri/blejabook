$(document).ready(function(){

	$('#edit_profile_btn').click(function(){

		var username = $('#username').text();
		var url_destination = '/accounts/edit_profile/' + username + '/'
		
		$.ajax({
			type: 'GET',
			url: url_destination,
			data: {
				'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
			},
			dataType: 'html'
		}).done( function(data, textStatus, jqXHR) {
			$('#profile').html(data);
      	}).fail(function() {
        	alert("FAIL");
      	});
	});

	$('#update_profile_frm').submit(function(event) {
		var form = $(this);
		console.log(form.attr('method'));
		
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			dataType: 'html'	
		}).done( function(data, textStatus, jqXHR) {
			$('#profile').html(data);
        	///if (data.redirect) {
            ///	window.location.href = data.redirect;
       		///}
      	}).fail(function() {
        	alert("FAIL");
      	});
		event.preventDefault();	
	});
});




