$(function(){

    // Does something when sidebar item is clicked
    // $(".sidebar-menu-item").click(function(){
    //     alert(this.id)
    // });

    // Changes sidebart item background colour when hovering over it.
    $(".sidebar-menu-item").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

    // Do something when sidebar toggle is clicked
    $("#sidebar-toggle").click(function(){
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

    $("#sidebar-toggle").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

});