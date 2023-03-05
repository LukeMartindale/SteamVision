$(function(){

    let draw_state = false

    // When user widegt click open dropdown menu
    $(".user-widget").click(function(){

        if($(".dropdown").hasClass("show-dropdown")){
            $(".dropdown").removeClass("show-dropdown")
        } else {
            $(".dropdown").addClass("show-dropdown")
        };

    })

    // Open Sidebar Functionality
    $(".sidebar-widget-highlight").click(function(){

        // Remove mini sidebar from tabindex
        $(".sidebar-mini-option-highlight").attr("tabindex", "-1")
        // Add big sidebar to tab index
        $(".sidebar-option-highlight").attr("tabindex", "0")

        $(".sidebar").toggleClass("hidden")
        $(".display-draw").toggleClass("hidden-none")
        $('body').toggleClass("stop-scrolling")

    })

    //Close sidebar when display-drawer is clicked
    $(".display-draw").click(function(){

        // Add mini sidebar from tabindex
        $(".sidebar-mini-option-highlight").attr("tabindex", "0")
        // Remove big sidebar to tab index
        $(".sidebar-option-highlight").attr("tabindex", "-1")

        $(".sidebar").toggleClass("hidden")
        $(".display-draw").toggleClass("hidden-none")
        $('body').toggleClass("stop-scrolling")

    })

    // Close Dropdown & Sidebar when document clicked
    document.addEventListener('click', event => {
        if (event.target.closest(".dropdown") === null) {
            if(!event.target.classList.contains("user-widget")){
                $(".dropdown").removeClass("show-dropdown")
            }
        }
    })


})

function disableScroll() {

  }
  
  // call this to Enable
  function enableScroll() {
    window.removeEventListener('DOMMouseScroll', preventDefault, false);
    window.removeEventListener(wheelEvent, preventDefault, wheelOpt); 
    window.removeEventListener('touchmove', preventDefault, wheelOpt);
    window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
  }