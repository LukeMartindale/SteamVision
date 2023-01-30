$(function(){

    // When user widegt click open dropdown menu
    $(".user-widget").click(function(){

        if($(".dropdown").hasClass("show-dropdown")){
            $(".dropdown").removeClass("show-dropdown")
        } else {
            $(".dropdown").addClass("show-dropdown")
        };

        // Add functionality so when this is clicked close open sidebar

    })

    // Open Sidebar Functionality

    // Close Dropdown & Sidebar when document clicked
    document.addEventListener('click', event => {
        if (event.target.closest(".dropdown") === null) {
            if(!event.target.classList.contains("user-widget")){
                $(".dropdown").removeClass("show-dropdown")
            }
        }
    })


})