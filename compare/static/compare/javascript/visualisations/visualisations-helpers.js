let compare_review_colours = [
    "#4169e1", //blue
    "#66cc33", //green
    "#f4ff50", //yellow
    "#f89c3c", //orange
    "#9300ff", //purple
    "#FF00FF", //pink
    "#6F4E37", //brown
    "#000000", //black
    "#FAF9F6", //white
]

let compare_sentiment_colours = [
    "#4169e1", //blue
    "#66cc33", //green
    "#f4ff50", //yellow
    "#f89c3c", //orange
    "#f03424", //red
    "#9300ff", //purple
    "#FF00FF", //pink
    "#6F4E37", //brown
    "#000000", //black
    "#FAF9F6", //white
]

let compare_players_colours = [
    "#4169e1", //blue
    "#66cc33", //green
    "#f4ff50", //yellow
    "#f89c3c", //orange
    "#f03424", //red
    "#9300ff", //purple
    "#FF00FF", //pink
    "#6F4E37", //brown
    "#000000", //black
    "#FAF9F6", //white
]

let compare_alternate_colours = [

]

function no_reviews_neutral_bar(){

    $(".neg-bar").each(function(){

        if($(this).val() == 0){
            $(this).css("fill", "rgba(217, 217, 217, 0.3)")
        }

    })

}
