(function(win, $){
    $(document).ready(function() {  
        $("#nav-icon").on("click", function() {
            $(this).toggleClass("open");
            $("nav").toggleClass("open");
        });
    });
}(window, jQuery));