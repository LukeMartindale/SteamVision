$(function(){

    $("#search-input").focusin(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 5px white")

    })

    $("#search-input").focusout(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 0px white")

    })

})

// Links to developer detail page
$(function(){

    $(".developer-widget-wrapper").click(function(){
        window.location.href = '/developer/' + $(this).attr('id').split("-")[2]
    })

    $(".developer-widget-wrapper").on("keydown", ".developer-widget-wrapper", function(e) {

        if(e.key === "Enter") {
            alert("TEST ALERT")
        }

    })

})
