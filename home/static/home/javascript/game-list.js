$(function(){

    let genres = sessionStorage.getItem("genres").split(",")
    let tags = sessionStorage.getItem("tags").split(",")
    let categories = sessionStorage.getItem("categories").split(",")

    console.log(genres, tags, categories)

    //Add data to hidden inputs
    $("#genres-input").val(genres)
    $("#tags-input").val(tags)
    $("#categories-input").val(categories)

    //Pre Input selected filters for genres
    genres.forEach(function(value, index, array){
        if(value){
            $("[id='" + value +"']").addClass("dropdown-menu-item-selected")
            $("#genres-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="' + value + '">' + value + '</div>')
        }
    })

    //Pre Input selected filters for tags
    tags.forEach(function(value, index, array){
        if(value){
            $("[id='" + value +"']").addClass("dropdown-menu-item-selected")
            $("#tags-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="' + value + '">' + value + '</div>')
        }
    })

    //Pre Input selected filters for categories
    categories.forEach(function(value, index, array){
        if(value){
            $("[id='" + value +"']").addClass("dropdown-menu-item-selected")
            $("#categories-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="' + value + '">' + value + '</div>')
        }
    })

})

$(function(){

    // Open filters section
    $(".filter-dropdown-wrapper").click(function(){

        let time = 0

        //Close any open dropdowns when filter box closes
        $(this).parents(".filter-form").find(".dropdown-menu").map(function(){
            if(!$(this).hasClass("hide")){
                time = 500
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

        let selected = $(this).closest(".dropdown-wrapper").children("input").val()

        if($(this).hasClass("dropdown-menu-item-selected")){
            //If item  selected, unselect and remove value from input
            let values = selected.split(",")
            values.splice($.inArray($(this).attr('id'), values), 1)

            selected = values

            //Add element to display
            $(this).closest('.dropdown-wrapper').children(".dropdown-button").children(".dropdown-button-display").children("[id='" + $(this).attr('id') + "']").remove()

        } else {
            //If item not selected, select and add value to input
            if($(this).closest(".dropdown-wrapper").children("input").val()){
                selected = selected + ',' + $(this).attr('id')
            } else {
                selected = $(this).attr('id')
            }

            //remove element from display
            $(this).closest('.dropdown-wrapper').children(".dropdown-button").children(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="' + $(this).attr('id') + '">' + $(this).attr('id') + '</div>')

        }

        $(this).closest(".dropdown-wrapper").children("input").val(selected)
        $(this).toggleClass("dropdown-menu-item-selected")

    })

})

function on_form_submit(){

    sessionStorage.clear()

    sessionStorage.setItem("genres", $("#genres-input").val())
    sessionStorage.setItem("tags", $("#tags-input").val())
    sessionStorage.setItem("categories", $("#categories-input").val())

}
