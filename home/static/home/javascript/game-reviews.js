$(function(){

    // Make textarea submit on enter not go to newline
    $("#reviews-text-search").keypress(function (e) {
        if(e.which === 13 && !e.shiftKey) {
            e.preventDefault();
            $(this).closest("form").submit();
        }
    });

})

// make reviews collapse if they are too big
$(function(){

    $(".review-text-section").each(function(){

        if($(this).height() > 350){
            $(this).append('<button class="more-review-button">Show More</button>')
            $(this).find(".more-review-button").css(
                {
                    "background-color": "#4169E1",
                    "border-radius": "6px",
                    "border": "0",
                    "color": "#bec5cb",
                    "cursor": "pointer",
                    "width": "90px",
                    "height": "25px",
                    "margin-top": "10px"
                }
            )
        }

    })

    $(".more-review-button").click(function(){

        $(this)
            .parent(".review-text-section")
            .children(".review-text-pre")
            .toggleClass("review-expanded")

    })

})

// Clear page button
$(function(){

    $(".clear-button").click(function(){
        window.location.href = `/games/${game_id}/reviews/`
    })

})

