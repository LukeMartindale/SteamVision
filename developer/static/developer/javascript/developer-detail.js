$(function(){

    console.log("DEVELOPER DETAIL LOAD TEST")
    $("#developer-game-list-button").click(function(){

        if($(".developer-games-list-section-wrapper").hasClass("hide-section")){

            $(".developer-section").each(function(){
                if(!$(this).hasClass("hide-section")){
                    $(this).addClass("hide-section")
                }
            })

            $(".selector-button").each(function(){
                $(this).removeClass("selected-button")
            })

            $(".developer-games-list-section-wrapper").removeClass("hide-section")
            $(this).addClass("selected-button")

        }
    })

    $("#developer-reviews-about-button").click(function(){

        if($(".developer-reviews-about-section-wrapper").hasClass("hide-section")){
            $(".developer-section").each(function(){
                if(!$(this).hasClass("hide-section")){
                    $(this).addClass("hide-section")
                }
            }) 
        }

        $(".selector-button").each(function(){
            $(this).removeClass("selected-button")
        })

        $(".developer-reviews-about-section-wrapper").removeClass("hide-section")
        $(this).addClass("selected-button")
    })


})

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
