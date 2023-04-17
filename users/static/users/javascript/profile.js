$(function() {

    //Content Section Chnage "Followed Games"
    $("#followed-games-selector-button").click(function(){

        let ids = ["system-info-section", "edit-profile-section"]
        let button_ids = ["system-info-selector-button", "edit-profile-selector-button"]

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

        $("#followed-games-section").removeClass("hide-section")
        $("#followed-games-selector-button").addClass("content-selected")

    })

    // Content Section Change "System Info"
    $("#system-info-selector-button").click(function(){

        let ids = ["followed-games-section", "edit-profile-section"]
        let button_ids = ["followed-games-selector-button", "edit-profile-selector-button"]

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

        $("#system-info-section").removeClass("hide-section")
        $("#system-info-selector-button").addClass("content-selected")

    })

    // Content Section Change "Edit Profile"
    $("#edit-profile-selector-button").click(function(){

        let ids = ["followed-games-section", "system-info-section"]
        let button_ids = ["followed-games-selector-button", "system-info-selector-button"]

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

        $("#edit-profile-section").removeClass("hide-section")
        $("#edit-profile-selector-button").addClass("content-selected")

    })

    // Go to page to edit profile info
    $("#edit-profile-button").click(function(){
        window.location.href = '/users/profile/edit/'
    })

    // Go to game page on followed game click
    $(".game-widget-wrapper").click(function(event){
        window.location.href = `/games/${this.id.split("-")[2]}`
    })

    // Go to game page on followed game enter pressed
    $(".game-widget-wrapper").on('keypress', function(event){
        if(event.which == 13){
            window.location.href = `/games/${this.id.split("-")[2]}`
        }
    })

    $(".unfollow-button").click(function(event){
        event.stopPropagation()

        let api_url = `/api/user/unfollowgame/${$(this).attr("id").split("-")[2]}/`

        console.log(api_url)

        console.log(this.id)

        let id = this.id

        let response = function(){
            let data = null;
            $.ajax({
                async: false,
                type: 'GET',
                dataType: 'json',
                url: api_url,
                success: function(result){
                    data = result
                    console.log("success")
                    $(`#${id}`).closest(".game-widget-wrapper").remove()
                }
            });
            return data
        }();
        
    })

})
