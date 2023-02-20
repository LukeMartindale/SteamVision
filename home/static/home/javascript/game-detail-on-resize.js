$(function(){

    let resizeTimer;

    $(window).resize(function () { 

        clearTimeout(resizeTimer)
        resizeTimer = setTimeout(function() {
            review_all_time_year(game_id)
            sentiment_graph()
            console.log("RESIZE")
        }, 100)
    
    });

})

