$(function(){

    $(".search-display-wrapper").width($(".search-bar-wrapper").width())

    $("#search-input").focusin(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 5px white")

        if($("#search-input").val()){
            $(".search-display-wrapper").removeClass("hide")
        }
    })

    $("#search-input").focusout(function(){

        setTimeout(() => {
            $(".search-bar-wrapper").css("box-shadow", "0px 0px 0px white")
            $(".search-display-wrapper").addClass("hide")
        }, 250);

    })

    let timeout

    $("#search-input").on('input', function(){

        clearTimeout(timeout)

        // Wait 1 second before 
        timeout = setTimeout(function(){
            if($("#search-input").val()){
                $(".search-display-wrapper").removeClass("hide")
                let games = searchApiCall()
                searched_game_data = games

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

                        item
                            .append('<div class="search-item-title-wrapper"></div>')

                        item
                            .find(".search-item-title-wrapper")
                            .append(`<div class="search-item-title-text">${game.name}</div>`)

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
        // Add selcted game data to selected_game_data
        let selected_data
        console.log("Search Game Data: ", searched_game_data)
        for (let i = 0; i < searched_game_data.length; i++){
            if(searched_game_data[i]["app_id"] == id){
                selected_data = searched_game_data[i]
                console.log(i)
                break
            }
        }
        if(!compare_game_data.includes(selected_data)){
            // Add data to compare_game_data
            compare_game_data.push(selected_data)
            // Add selected item to selected items display
            selectedItemDisplayAppend(selected_data)
            // Draw Graphs
            drawGraphs()
        }

    })
}

function selectedItemDisplayAppend(game){

    // Get game data from selcetd_game_data

    $(".selected-games-wrapper").append(`<div class="selected-game-widget-wrapper" id="selected-game-${game.app_id}"><div>`)

    let selected_wrapper = $(`#selected-game-${game.app_id}`)

    selected_wrapper.append('<div class="selected-game-image-wrapper"></div>')
    selected_wrapper
        .find(".selected-game-image-wrapper")
        .append(`<img class="selected-game-image" src="${game.header_image}"></img>`)

    selected_wrapper.append('<div class="selected-game-button-wrapper"></div>')
    selected_wrapper
        .find(".selected-game-button-wrapper")
        .append(`<div class="game-button-widget" id="remove-button-${game.app_id}"></div>`)

    selected_wrapper
        .find(".game-button-widget")
        .append('<i class="bi bi-x-lg remove-icon"></i>')

    deleteItemClickEvent()

}

function deleteItemClickEvent(){
    $(".game-button-widget").click(function(){
        let id = this.id.split("-")[2]

        $(`#selected-game-${id}`).remove()

        console.log("Before: ", compare_game_data)
        console.log("Before: ", compare_game_ids)

        // remove game data from selected game data
        let filtered_games = compare_game_data.filter(function(value, index){
            return value.app_id !=  id
        })

        // remove game id from selected game ids
        let filtered_ids = compare_game_ids.filter(function(value, index){
            return value != id
        })

        compare_game_data = filtered_games
        compare_game_ids = filtered_ids

        drawGraphs()

        console.log("After: ", compare_game_data)
        console.log("ids: ", compare_game_ids)

        console.log(id)
    })

}
