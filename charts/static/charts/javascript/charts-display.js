// Get the data for Current Players
function GetPlayerCountCurrent() {

    let api_url = `/api/charts/get-player-count-current/`

    let players = function(){
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

    return players

}

// Get the data for Reviews Percentage
function GetReviewsPercentageCurrent(){

    let api_url = `/api/charts/get-reviews-percentage-current/`

    let reviews = function(){
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

    return reviews

}

function getGameDescriptors(){

    let api_url = `/api/get-descriptors`

    let descriptors = function(){
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

    return descriptors

}

// Games with the current highest number of players online
function DisplayPlayerCountCurrent() {

    let players = GetPlayerCountCurrent()
    let descriptors = getGameDescriptors()

    $(".game-list-wrapper").empty()

    HeaderSectionAppend("Player Count")

    players.forEach(function(game, index){

        // GAME BAR SECTION
        $(".game-list-wrapper").append(`<div class="game-tab-wrapper" id="game-tab-wrapper-${game.app.app_id}"></div>`)
        $(`#game-tab-wrapper-${game.app.app_id}`).append(`<div class="game-tab" id=${game.app.app_id}></div>`)
        $(`#${game.app.app_id}`)
            .append('<div class="game-tab-block-short-1 rank-tab-block"></div>')
            .append('<div class="game-tab-block name-tab-block"></div>')
            .append('<div class="game-tab-block genre-tab-block"></div>')
            .append('<div class="game-tab-block player-count-tab-block"></div>')
            .append('<div class="game-tab-block-short-2 more-tab-block"></div>')

        //Append Game Ranking
        $(`#${game.app.app_id}`)
            .children(".rank-tab-block")
            .append(index + 1)

        //Append Game Name
        $(`#${game.app.app_id}`)
            .children(".name-tab-block")
            .append(game.app.name)

        //Append the games Genres to the box
        game.app.genres.forEach(function(genre){
            $(`#${game.app.app_id}`)
            .children(".genre-tab-block")
            .append(`<div class="game-descriptor-box">${genre}</div>`)
        })

        $(`#${game.app.app_id}`)
            .children(".player-count-tab-block")
            .append(game.player_count)

        // Append more info button
        $(`#${game.app.app_id}`)
            .find(".more-tab-block")
            .append('<div class="more-info-button-wrapper">')

        $(`#${game.app.app_id}`)
            .find(".more-info-button-wrapper")
            .append('<div class="more-info-button-highlight">')

        $(`#${game.app.app_id}`)
            .find(".more-info-button-highlight")
            .append('<i class="bi bi-card-text more-info-button"></i>')

        MoreInfoSectionAppend(game, descriptors)

    })

    MoreInfoButtonFunction()

}

// Games with the biggest & increase in player count this month compared to avg of last month
function PlayerCountDisplayTrending() {
    console.log("Not Yet Implemented")
}

// Games with highest review counts of all time
function DisplayReviewsCurrent() {

    let reviews = GetReviewsPercentageCurrent()
    let descriptors = getGameDescriptors()

    $(".game-list-wrapper").empty()

    HeaderSectionAppend("Reviews Percentage")

    reviews.forEach(function(game, index){

        // GAME BAR SECTION
        $(".game-list-wrapper").append(`<div class="game-tab-wrapper" id="game-tab-wrapper-${game.app.app_id}"></div>`)
        $(`#game-tab-wrapper-${game.app.app_id}`).append(`<div class="game-tab" id=${game.app.app_id}></div>`)
        $(`#${game.app.app_id}`)
            .append('<div class="game-tab-block-short-1 rank-tab-block"></div>')
            .append('<div class="game-tab-block name-tab-block"></div>')
            .append('<div class="game-tab-block genre-tab-block"></div>')
            .append('<div class="game-tab-block player-count-tab-block"></div>')
            .append('<div class="game-tab-block-short-2 more-tab-block"></div>')

        //Append Game Ranking
        $(`#${game.app.app_id}`)
            .children(".rank-tab-block")
            .append(index + 1)

        //Append Game Name
        $(`#${game.app.app_id}`)
            .children(".name-tab-block")
            .append(game.app.name)

        //Append the games Genres to the box
        game.app.genres.forEach(function(genre){
            $(`#${game.app.app_id}`)
            .children(".genre-tab-block")
            .append(`<div class="game-descriptor-box">${genre}</div>`)
        })

        $(`#${game.app.app_id}`)
            .children(".player-count-tab-block")
            .append((game.reviews_percentage * 100).toFixed(1) + "%")

        // Append more info button
        $(`#${game.app.app_id}`)
            .find(".more-tab-block")
            .append('<div class="more-info-button-wrapper">')

        $(`#${game.app.app_id}`)
            .find(".more-info-button-wrapper")
            .append('<div class="more-info-button-highlight">')

        $(`#${game.app.app_id}`)
            .find(".more-info-button-highlight")
            .append('<i class="bi bi-card-text more-info-button"></i>')

        MoreInfoSectionAppend(game, descriptors)

    })

    MoreInfoButtonFunction()
}

// Games with the biggest increase in review score since last month comapred to this month
function DisplayReviewsTrending() {
    console.log("Not Yet Implemented")
}

// Functionality for the more info button
function MoreInfoButtonFunction() {

    $(".more-info-button-highlight").click(function(){
        $(this).parents(".game-tab-wrapper").find(".game-tab-more-info-wrapper").toggleClass("hide-none")
    })

    $(".game-tab").click(function(e){
        if(!$(e.target).hasClass('more-info-button-highlight') && !$(e.target).hasClass('more-info-button')){
            window.location.href = '/games/' + $(this).attr('id')
        }
    })

}

// Append the more info section for a specific game
function MoreInfoSectionAppend(game, descriptors) {
        // MORE INFO SECTION
        // Append more info section
        $(`#game-tab-wrapper-${game.app.app_id}`)
            .append(`<div class="game-tab-more-info-wrapper hide-none" id="game-tab-more-${game.app.app_id}"></div>`)

        $(`#game-tab-more-${game.app.app_id}`)
            .append('<div class="game-tab-more-info-section-wrapper"></div>')

        // Append first section
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".game-tab-more-info-section-wrapper")
            .append('<div class="game-tab-more-info-section-first"></div>')
        // Append game image
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".game-tab-more-info-section-first")
            .append(`<img class="more-info-image" src="${game.app.header_image}">`)

        // Append second section
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".game-tab-more-info-section-wrapper")
            .append('<div class="game-tab-more-info-section-second"></div>')

        //Append Description Section into second section
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".game-tab-more-info-section-second")
            .append('<header class="description-label">Description</header>')
            .append('<div class="description-box"></div>')
            .find(".description-box")
            .append(game.app.description)

        // Append descriptors label box
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".game-tab-more-info-section-second")
            .append('<div class="descriptors-box"></div>')
            .find(".descriptors-box")
            .append('<div class="descriptors-box-labels"></div>')

        // Append descriptor label to label box
        $(`#game-tab-more-${game.app.app_id}`)
            .find(".descriptors-box-labels")
            .append('<div class="descriptors-box-labels-text">Genres</div>')
            .append('<div class="descriptors-box-labels-text">Tags</div>')
            .append('<div class="descriptors-box-labels-text">Categories</div>')

        $(`#game-tab-more-${game.app.app_id}`)
            .find(".descriptors-box")
            .append('<div class="descriptors-box-content"></div>')

        $(`#game-tab-more-${game.app.app_id}`)
            .find(".descriptors-box-content")
            .append('<div class="descriptors-box-section genre-descriptors-box-section"></div>')

        $(`#game-tab-more-${game.app.app_id}`)
            .find(".descriptors-box-content")
            .append('<div class="descriptors-box-section tags-descriptors-box-section"></div>')

        $(`#game-tab-more-${game.app.app_id}`)
            .find(".descriptors-box-content")
            .append('<div class="descriptors-box-section categories-descriptors-box-section"></div>')

        game.app.genres.forEach(function(genre, index){
            if(index < 4){
                $(`#game-tab-more-${game.app.app_id}`)
                    .find(".genre-descriptors-box-section")
                    .append(`<div class="game-descriptor-box">${genre}</div>`)
            }
        })

        game.app.tags.forEach(function(tags, index){
            if(index < 5){
                $(`#game-tab-more-${game.app.app_id}`)
                    .find(".tags-descriptors-box-section")
                    .append(`<div class="game-descriptor-box">${tags}</div>`)
            }
        })

        game.app.categories.forEach(function(category, index){
            descriptors.forEach(function(descriptor, d_index){
                if(descriptor.name == category){
                    if(descriptor.type == 'Categories'){
                        $(`#game-tab-more-${game.app.app_id}`)
                            .find(".categories-descriptors-box-section")
                            .append(`<div class="category-widget" title="${descriptor.name}" id="descriptor-${index}-${game.app.app_id}"></div>`)
                            .find(`#descriptor-${index}-${game.app.app_id}`)
                            .append(`<i class="bi ${descriptor.symbol} category-widget-image"></i>`)
                    }
                }

            })

        })
}

// Append Header Section
function HeaderSectionAppend(type){

    $(".game-list-wrapper").append(`<div class="game-tabs-header"></div>`)
    $(".game-tabs-header")
        .append('<div class="game-tabs-header-rank rank-header">Rank</div>')
        .append('<div class="game-tabs-header-text name-header">Name</div>')
        .append('<div class="game-tabs-header-text genres-header">Genres</div>')
        .append(`<div class="game-tabs-header-text category-header">${type}</div>`)
        .append('<div class="game-tabs-header-more more-info-header">More Info</div>')

}
