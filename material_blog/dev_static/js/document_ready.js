$(document).ready(function() {
    $('select').material_select();
    $('.dropdown-button').dropdown({ hover: false });
    $('.chips').material_chip();

    $('.like').click(function () {
        var this_ = $(this);
        var url_ = $(this).attr("data-href");
        $.ajax({
            type: "get",
            url: url_,
            object: $(this).attr('name'),
            data: {'post_id': $(this).attr('name')},
            dataType: "json",
            success: function (response) {
                $("#like_count"+this.object).html(response.likes_count);
            },
            error: function (rs, e) {
                alert(rs.responseText);
            }
        });
    });

    $('.modal').modal();

    // $(".animated_modal_open").animatedModal();
});