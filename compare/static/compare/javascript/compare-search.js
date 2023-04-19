$(function(){

    $(".search-display-wrapper").width($(".search-bar-wrapper").width())

    $("#search-input").focusin(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 5px white")

        if($("#search-input").val()){
            $(".search-display-wrapper").toggleClass("hide")
        }
    })

    $("#search-input").focusout(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 0px white")
        // $(".search-display-wrapper").addClass("hide")

    })

    let timeout

    $("#search-input").on('input', function(){

        clearTimeout(timeout)

        // Wait 1 second before 
        timeout = setTimeout(function(){
            if($("#search-input").val()){
                $(".search-display-wrapper").removeClass("hide")
                let games = searchApiCall()

                // Check if search has returned any games
                if(games.length){

                    $(".search-display-wrapper").empty()
                    let wrapper = $(".search-display-wrapper")

                    games.forEach(function(game, index){

                        wrapper
                            .append(`<div class="search-item-wrapper" id="game-id-${game.app_id}"></div>`)

                        let item = wrapper.find(`#game-id-${game.app_id}`)

                        item
                            .append(`<div class="search-item-image-wrapper"></div>`)

                        item
                            .find(".search-item-image-wrapper")
                            .append(`<img class="search-item-image" src="${game.header_image}"></img>`)
                    })

                    searchItemClickEvent()

                } else {
                    $(".search-display-wrapper").empty()
                }
            } else {
                console.log("Search Empty")
            }
        }, 1000)
    })

    // Set size of search display
    $(window).resize(function(){
        $(".search-display-wrapper").width($(".search-bar-wrapper").width())
    })

})

function searchApiCall(){

    let search_value = $("#search-input").val()

    let api_url = `/api/get-games-search/${search_value}/`

    let games = function(){
        let data = null;
        $.ajax({
            async: false,
            type: 'GET',
            dataType: 'json',
            url: api_url,
            success: function(result){
                data = result
            }
        });
        return data
    }();

    return games.games

}

function searchItemClickEvent(){
    $(".search-item-wrapper").click(function(){
        let id = this.id.split("-")[2]
        // Check id is not already in list
        if(!compare_game_ids.includes(id)){
            compare_game_ids.push(id)
        }
        // Add selected item to selected items display
        selectedItemDisplayAppend("test")
        // Draw Graphs
        drawGraphs()
    })
}

function selectedItemDisplayAppend(game_id){

    $(".selected-games-wrapper").append(`<div class="selected-game-widget-wrapper" id="selected-game-${game_id}"><div>`)

    $(`#selected-game-${game_id}`).append('<div class="selected-game-image-wrapper"></div>')

    $(`#selected-game-${game_id}`).append('<div class="selected-game-button-wrapper"></div>')

}
