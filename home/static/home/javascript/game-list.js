$(function(){

    $(".filter-dropdown-wrapper").click(function(){

        $(".bottom-filter").toggleClass("hide");
        $(".filter-break").toggleClass("hide-none");
        $("#filter-dropdown-icon").toggleClass("filter-icon-down");

    })

    $(".select-widget").click(function(){
        $(".tag-input").val("test,test,test")
    })

})