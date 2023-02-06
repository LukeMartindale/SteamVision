$(function(){

    $(".more-info-button-highlight").click(function(){
        $(this).parents(".game-tab-wrapper").find(".game-tab-more-info-wrapper").toggleClass("hide-none")
    })

    $(".game-tab").click(function(e){
        if(e.target.id != 'more-game-tab' && e.target.id != 'more-game-tab-img'){
            window.location.href = '/games/' + $(this).attr('id')
        }
    })

})
