$(document).ready(function() {
    $('select').material_select();
    $('.dropdown-button').dropdown({ hover: false });
    $('.chips').material_chip();

    $('#like').click(function(){
            var this_ =  $(this);
            var url_ = $(this).attr("data-href");
        $.ajax({
            type: "get",
            url: url_,
            data: {'post_id': $(this).attr('name')},
            dataType: "json",
            success: function(response) {
                $("#like_count").html(response.likes_count);
            },
            error: function(rs, e) {
                alert(rs.responseText);
            }
        });
    });
});