$(function(){

    // Open filters section
    $(".filter-dropdown-wrapper").click(function(){

        let time = 0

        //Close any open dropdowns when filter box closes
        $(this).parents(".filter-form").find(".dropdown-menu").map(function(){
            if(!$(this).hasClass("hide")){
                time = 1000
                $(this).addClass("hide")
                $(this).children().toggleClass("hide-none")
                $(this).parent().children(".dropdown-button").children(".dropdown-button-arrow-wrapper").children().toggleClass("filter-icon-down")
            }
        })

        setTimeout(function(){
            $(".bottom-filter").toggleClass("hide");
            $(".filter-break").toggleClass("hide-none");
            $("#filter-dropdown-icon").toggleClass("filter-icon-down");
        }, time)

    })

    //Open dropdown on filter options
    $(".dropdown-button").click(function(){

        let temp = $(this).parent().children(".dropdown-menu").attr('id')

        //Close any open dropdowns when another dropdown is opened
        $(".dropdown-menu").map(function(){
            if($(this).attr('id') != temp && !$(this).hasClass("hide")){
                $(this).addClass("hide")
                $(this).parent().children().children().children(".filter-icon").toggleClass("filter-icon-down")
                $(this).children().toggleClass("hide-none")
            }
        })

        $(this).children().children(".filter-icon").toggleClass("filter-icon-down")
        $(this).parent().children(".dropdown-menu").toggleClass("hide")
        $(this).parent().children(".dropdown-menu").children(".dropdown-menu-item-wrapper").toggleClass("hide-none")

    })

    $(".dropdown-menu-item").click(function(){
        console.log("TEST")
    })

    $(".select-widget").click(function(){
        $(".tag-input").val("test,test,test")
    })

})