$(function() {

    // Content Section Change "System Info"
    $("#system-info-selector-button").click(function(){

        let ids = ["edit-profile-section"]
        let button_ids = ["edit-profile-selector-button"]

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

        let ids = ["system-info-section"]
        let button_ids = ["system-info-selector-button"]

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

    $("#edit-profile-button").click(function(){
        window.location.href = '/users/profile/edit/'
    })

    // $("#test-button").click(function(){
    //     console.log("button test")
    //     $('#username-input').prop('disabled', (i, v) => !v);
    // })

})
