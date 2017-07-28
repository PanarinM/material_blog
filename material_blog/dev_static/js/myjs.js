$(document).ready(function() {
    $('select').material_select();
    $('.dropdown-button').dropdown({ hover: false });
    $('.chips').material_chip();

    $('#like').click(function(){
            var this_ =  $(this);
            var url_ = this_.attr("data-href");
        $.ajax({
            type: "get",
            url: url_,
            data: {'post_id': $(this).attr('name')},
            dataType: "json",
            success: function(response) {
                alert(response.message);
                alert('Post likes count is now ' + response.likes_count);
            },
            error: function(rs, e) {
                alert(rs.responseText);
            }
        });
    })
});