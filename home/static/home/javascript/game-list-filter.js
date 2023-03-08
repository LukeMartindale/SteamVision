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

        $(".dropdown-button").each(function(){
            if($(this).attr("tabindex") == -1){
                $(this).attr("tabindex", 0)
            } else {
                $(this).attr("tabindex", -1)
            }
        })

        setTimeout(function(){
            $(".bottom-filter").toggleClass("hide");
            $(".filter-break").toggleClass("hide-none");
            $("#filter-dropdown-icon").toggleClass("filter-icon-down");
        }, time)

    })

    // CLEAR filters button
    $(".clear-filters-wrapper").click(function(){
        window.location.href = "/games/"
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

        console.log("CLICK BUTTON TEST")

        let selected = $(this).closest(".dropdown-wrapper").children("input").val()

        if($(this).hasClass("dropdown-menu-item-selected")){
            //If item  selected, unselect and remove value from input
            let values = selected.split(",")
            values.splice($.inArray($(this).attr('id').split("-")[1], values), 1)

            selected = values

            //Add element to display
            $(this).closest('.dropdown-wrapper').children(".dropdown-button").children(".dropdown-button-display").children("[id='" + $(this).attr('id') + "']").remove()

        } else {
            //If item not selected, select and add value to input
            if($(this).closest(".dropdown-wrapper").children("input").val()){
                selected = selected + ',' + $(this).attr('id').split("-")[1]
            } else {
                selected = $(this).attr('id').split("-")[1]
            }

            //remove element from display
            $(this).closest('.dropdown-wrapper').children(".dropdown-button").children(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="' + $(this).attr('id') + '">' + $(this).attr('id').split("-")[1] + '</div>')

        }

        $(this).closest(".dropdown-wrapper").children("input").val(selected)
        $(this).toggleClass("dropdown-menu-item-selected")

        let action_input = `/games/?genres=${$("#genres-input").val()}&tags=${$("#tags-input").val()}&categories=${$("#categories-input").val()}`
        $("#filter-form").attr('action', action_input)
    })
})

$(function(){

    let searchParams = new URLSearchParams(window.location.search)
    let searchtextParams = ""
    let genresParams = ""
    let tagsParams = ""
    let categoriesParams = ""
    
    if(searchParams.has("genres")){
        console.log("Has Genres")
        $("#genres-input").val(searchParams.get("genres"))
        genresParams = searchParams.get("genres").split(",")

        if(!genresParams[0] == ""){
            genresParams.forEach(function(value, index, array){
                $("[id='genre-" + value +"']").addClass("dropdown-menu-item-selected")
                $("#genres-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="genre-' + value + '">' + value + '</div>')
            })
        }

        $("#genres-input").val(genresParams)

    }

    if(searchParams.has("tags")){
        console.log("Has Tags")
        $("#tags-input").val(searchParams.get("tags"))
        tagsParams = searchParams.get("tags").split(",")

        if(!tagsParams[0] == ""){
            tagsParams.forEach(function(value, index, array){
                $("[id='tag-" + value +"']").addClass("dropdown-menu-item-selected")
                $("#tags-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="tag-' + value + '">' + value + '</div>')
            })
        }

        $("#tags-input").val(tagsParams)

    }

    if(searchParams.has("categories")){
        console.log("Has Categories")
        $("#categories-input").val(searchParams.get("categories"))
        categoriesParams = searchParams.get("categories").split(",")

        if(!categoriesParams[0] == ""){
            categoriesParams.forEach(function(value, index, array){
                $("[id='category-" + value +"']").addClass("dropdown-menu-item-selected")
                $("#categories-dropdown-wrapper").find(".dropdown-button-display").append('<div class="dropdown-button-display-widget" id="category-' + value + '">' + value + '</div>')
            })
        }

        $("#categories-input").val(categoriesParams)

    }

    if($("#search-input").val()){
        console.log("SEARCH INPUT")
        searchtextParams = $("#search-input").val()
    } else if ($(".search-input-text-display").text()){
        console.log("SEARCH DISPLAY")
        console.log($(".search-input-text-display").text())
        searchtextParams = $(".search-input-text-display").text()
    } else if (searchParams.has("search_text")){
        console.log("SEARCH TEXT")
        console.log(searchParams.has("search_text"))
        searchtextParams = searchParams.get("search_text")
    } else {
        searchtextParams = searchtextParamConst
    }

    let action_input = `/games/?search_text=${searchtextParams}&genres=${genresParams}&tags=${tagsParams}&categories=${categoriesParams}`
    $("#filter-form").attr('action', action_input)

})

function on_form_submit(){

    let searchParams = new URLSearchParams(window.location.search)
    let searchtextParams = ""
    let genresParams = $("#genres-input").val()
    let tagsParams = $("#tags-input").val()
    let categoriesParams = $("#categories-input").val()

    if($("#search-input").val()){
        searchtextParams = $("#search-input").val()
    } else if ($(".search-input-text-display").text()){
        searchtextParams = $(".search-input-text-display").text()
        $("#search-input").val($(".search-input-text-display").text())
    } else if (searchParams.has("search_text")){
        searchtextParams = searchParams.get("search_text")
    }

    let action_input = `/games/?search_text=${searchtextParams}&genres=${genresParams}&tags=${tagsParams}&categories=${categoriesParams}`
    $("#filter-form").attr('action', action_input)

}
