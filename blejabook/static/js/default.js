$(document).ready(function(){

	$('#edit_profile_btn').click(function() {

		var username = $('#username').text();
		var url_destination = '/accounts/edit_profile/' + username + '/'
		
		$.ajax({
			type: 'GET',
			url: url_destination,
			data: {
				'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#profile').html(data);
}

