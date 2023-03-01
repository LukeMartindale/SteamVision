$(function(){

    // Make textarea submit on enter not go to newline
    $("#reviews-text-search").keypress(function (e) {
        if(e.which === 13 && !e.shiftKey) {
            e.preventDefault();
            $(this).closest("form").submit();
        }
    });

})
