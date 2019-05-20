(function(win, $){
    $(document).ready(function() {  
        $("#nav-icon").on("click", function() {
            $(this).toggleClass("open");
            $("nav").toggleClass("open");
        });
        $("header img").on("click", function() {
            var link = $("header a").attr("href");
            location.href = link;
        })
    });
}(window, jQuery));