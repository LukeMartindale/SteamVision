// SET Variables
let follow_status = "unknown"

// GENERAL PAGE FUNCTIONALITY
$(function(){

    // Content Section Change "Tab"
    $("#review-selector-button").click(function(){

        let ids = ["players-section", "recent-reviews-section"]
        let button_ids = ["players-selector-button", "recent-reviews-selector-button"]

        ids.forEach(function(id, index){
            if(!$("#" + id).hasClass("hide-section")){
                $("#" + id).addClass("hide-section")
            }
        })

        button_ids.forEach(function(id, index){
            if($("#" + id).hasClass("content-selected")){
                $("#" + id).removeClass("content-selected")
            }
        })

        $("#reviews-section").removeClass("hide-section")
        $("#review-selector-button").addClass("content-selected")

    })

    $("#recent-reviews-selector-button").click(function(){

        let ids = ["players-section", "reviews-section"]
        let button_ids = ["players-selector-button", "review-selector-button"]

        ids.forEach(function(id, index){
            if(!$("#" + id).hasClass("hide-section")){
                $("#" + id).addClass("hide-section")
            }
        })

        button_ids.forEach(function(id, index){
            if($("#" + id).hasClass("content-selected")){
                $("#" + id).removeClass("content-selected")
            }
        })

        $("#recent-reviews-section").removeClass("hide-section")
        $("#recent-reviews-selector-button").addClass("content-selected")

    })


    $("#players-selector-button").click(function(){

        let ids = ["reviews-section", "recent-reviews-section"]
        let button_ids = ["review-selector-button", "recent-reviews-selector-button"]

        ids.forEach(function(id, index){
            if(!$("#" + id).hasClass("hide-section")){
                $("#" + id).addClass("hide-section")
            }
        })

        button_ids.forEach(function(id, index){
            if($("#" + id).hasClass("content-selected")){
                $("#" + id).removeClass("content-selected")
            }
        })

        $("#players-section").removeClass("hide-section")
        $("#players-selector-button").addClass("content-selected")

    })

    // Content Section Widegt Dropdown
    $(".widgets-draw-icon-wrapper").click(function(){
        $(this).closest(".game-section").find(".visualisation-widgets-wrapper").toggleClass("hide-ani")
        $(this).children().toggleClass("widgets-icon-up")
    })

})

// CHECK IF USER IF FOLLOWING GAME
$(function(){

    let api_url = `/api/user/checkfollowgame/${game_id}`

    let response = function(){
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

    if(response.code == 1){
        follow_status = "following"
        $('#follow-game-button').text("Unfollow")
        $('#follow-game-button').addClass("alternate-detail-button")
    } else if (response.code == 2) {
        follow_status = "not following"
    }

    console.log(follow_status)

})

function FollowButton(){

    console.log("Follow Button")
    console.log(follow_status)

    if (follow_status == "not following") {
        console.log("TEST 1")
        let api_url = `/api/user/followgame/${game_id}/`

        let response = function(){
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

        console.log("1")

        follow_status = "following"

        $('#follow-game-button').text("Unfollow")
        $('#follow-game-button').addClass("alternate-detail-button")

    } else if (follow_status == "following") {
        console.log("TEST 2")
        let api_url = `/api/user/unfollowgame/${game_id}/`

        let response = function(){
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

        console.log("2")

        follow_status = "not following"
        
        $('#follow-game-button').text("Follow")
        $('#follow-game-button').removeClass("alternate-detail-button")
    }

}

function CompareButton(){

    console.log("Compare Button")

    let url = `/compare/?games=${game_id}`

    window.location.href = url
    
}
