$(function(){

    $("#search-input").focusin(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 5px white")

    })

    $("#search-input").focusout(function(){

        $(".search-bar-wrapper").css("box-shadow", "0px 0px 0px white")

    })

    let timeout

    $("#search-input").on('input', function(){

        clearTimeout(timeout)

        timeout = setTimeout(function(){
            console.log("INPUT DETECTED")
        }, 1000)
    })

})