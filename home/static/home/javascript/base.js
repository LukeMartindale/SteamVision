$(function(){

    let count = 0

    // Does something when sidebar item is clicked
    $(".sidebar-menu-item").click(function(){
        alert(this.id)
    });

    // Changes sidebart item background colour when hovering over it.
    $(".sidebar-menu-item").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

    // Do something when sidebar toggle is clicked
    $("#sidebar-toggle").click(function(){
        // alert(this.id)
        // $("#nav-title").addClass("nav-short")
        switch(count){
            case 0:
                $(".sidebar").addClass("short-sidebar")
                $(".content").addClass("short-content")
                count = 1
                break;
            case 1:
                $(".sidebar").removeClass("short-sidebar")
                $(".content").removeClass("short-content")
                count = 0
                break;
        }

    });

    $("#sidebar-toggle").hover(function(){
        $(this).addClass("active");
        }, function(){
            $(this).removeClass("active")
        }
    );

});