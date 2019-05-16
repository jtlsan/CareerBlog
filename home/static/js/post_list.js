(function(win, $){
    $(document).ready(function() {
        $(".grid-post li").on("click", function(){
            var next_url = $(this).children().eq(1).attr("href");
            location.href = next_url;
        })
        $.each($(".grid-post li"), function(){
            var txt = $(this).children("#category").text();
            if (txt == "Study") {
                $(this).children("#category").css("background-color", "#D5FBCC");
            }
            else if (txt == "Projects") {
                $(this).children("#category").css("background-color", "#CCD5FB");
            }
            else {
                $(this).children("#category").css("background-color", "#FBCCD5");
            }
        });
    })
}(window, jQuery));