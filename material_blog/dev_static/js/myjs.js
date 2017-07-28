$(document).ready(function() {
    $('select').material_select();
    $('.dropdown-button').dropdown({ hover: false });
    $('.chips').material_chip();
    $('#like').click(function(){
        console.log('random message');
        $.ajax({
            type: "POST",
            url: "{% url 'like' %}",
            data: {'slug': $(this).attr('name'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
            dataType: "json",
            success: function(response) {
                alert(response.message);
                alert('Company likes count is now ' + response.likes_count);
            },
            error: function(rs, e) {
                alert(rs.responseText);
            }
        });
    });
});