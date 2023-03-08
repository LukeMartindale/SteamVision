$(function(){

    $(".more-info-button-highlight").click(function(){
        $(this).parents(".game-tab-wrapper").find(".game-tab-more-info-wrapper").toggleClass("hide-none")
    })

    $(".game-tab").click(function(e){
        if(e.target.id != 'more-game-tab' && e.target.id != 'more-game-tab-img'){
            window.location.href = '/games/' + $(this).attr('id')
        }
    })

    $("#search-input").focusin(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 5px white")

    })

    $("#search-input").focusout(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 0px white")

    })

})
