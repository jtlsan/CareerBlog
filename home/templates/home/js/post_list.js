(function(win, $){
    $(document).ready(function() {
        $(".grid-post li").on("click", function(){
            var next_url = $(this).children().eq(1).attr("href");
            location.href = next_url;
        })
    })
}(window, jQuery));