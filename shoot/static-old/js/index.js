$(function(){
	$('button').click(function(){
		$('h1').toggle();
	});
});

$(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})