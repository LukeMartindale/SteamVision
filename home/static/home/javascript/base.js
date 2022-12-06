$(function(){

    // Changes sidebart item background colour when hovering over it.
    $(".sidebar-menu-item").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

    // Do something when sidebar toggle is clicked
    $("#sidebar-toggle").click(function(e){
        e.preventDefault()
        if($(".sidebar").hasClass("short-sidebar") && $(".content-wrapper").hasClass("short-content")){
            $(".sidebar").removeClass("short-sidebar")
            $(".content-wrapper").removeClass("short-content")
            localStorage.removeItem("sidebar-status", "collapsed")
        } else {
            $(".sidebar").addClass("short-sidebar")
            $(".content-wrapper").addClass("short-content")
            localStorage.setItem("sidebar-status", "closed")
        }
        sentiment_graph()
    });

    //On hover chnage the colour of sidebar toggle button when hovered
    $("#sidebar-toggle").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

});