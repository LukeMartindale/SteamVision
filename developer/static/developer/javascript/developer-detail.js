$(function(){

    console.log("DEVELOPER DETAIL LOAD TEST")
    $(".developer-game-widget-wrapper").click(function(){
        window.location.href = '/games/' + $(this).attr('id').split("-")[2]
    })
    
})
