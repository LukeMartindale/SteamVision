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
    // Add selected item to relevant input
    $(".dropdown-menu-item").click(function(){

        let selected = $(this).closest(".dropdown-wrapper").children("#genres-input").val()

        // let values = selected.split(",")
        // console.log(values)
        // console.log(values[0])

        if($(this).hasClass("dropdown-menu-item-selected")){
            //If item  selected, unselect and remove value from input
            let values = selected.split(",")
            values.splice($.inArray($(this).attr('id'), values), 1)

            selected = values

        } else {
            //If item not selected, select and add value to input
            if($(this).closest(".dropdown-wrapper").children("input").val()){
                selected = selected + ',' + $(this).attr('id')
            } else {
                selected = $(this).attr('id')
            }
        }



        $(this).closest(".dropdown-wrapper").children("input").val(selected)
        $(this).toggleClass("dropdown-menu-item-selected")

    })

    $(".select-widget").click(function(){
        $(".tag-input").val("test,test,test")
    })

})