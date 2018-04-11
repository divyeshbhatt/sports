$(function(){
	$('button').click(function(){
		$('h1').toggle();
	});
});

$(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    alert(value);
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})

$(document).on('submit', '#new_user_form', function(e){

      e.preventDefault();
      $.ajax({
          type : 'POST',
          url : '/create/',
          data : {
            code: $('#code').val(),
            first_name: $('#first_name').val(),
            last_name : $('#last_name').val(),
            birth_date : $('#date_of_birth').val(),
          },
          success: function({

          })
      })
})