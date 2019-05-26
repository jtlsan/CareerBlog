(function(win, $){
    $.categoryColor = function() {
        $.each($("li.list-raw"), function() {
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
            $(this).removeClass("list-raw");
        });
    }
    $.listCenter = function() {
        if (screen.availWidth < 768) {
            $(".infinite-item:nth-child(3n+1)").css("margin-left", '0px');
            $(".infinite-item:nth-child(3n)").css("margin-right", '0px');
        }
        else if (screen.availWidth >= 768 && screen.availWidth < 1024){
            var margin = (screen.availWidth - $(".infinite-item").outerWidth()*3 - 30)/2 -5;
            $(".infinite-item:nth-child(3n+1)").css("margin-left", margin);
            $(".infinite-item:nth-child(3n)").css("margin-right", margin);
        }
    }
    $(function() {
        $.categoryColor();
        $.listCenter();
        $(window).on("resize", $.listCenter)
        $(document).on("mouseover focus", ".infinite-item", function() {
            $(".infinite-item").css("cursor", "pointer");
        })
    })
    $(document).on('click', ".grid-post li", function() {
        var next_url = $(this).children().eq(1).attr("href");
        location.href = next_url;
    });
    $(document).on("DOMNodeInserted", ".grid-post", function() {
        $.categoryColor();
        $.listCenter();
        /*
        $(".unwraped")
        .wrapAll("<div class='3n-list-container' />")
        .removeClass("unwraped");
        */
    });
    



    
    /*
    $("li.list").ready(function() {
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
                $(this).children("#category").addClass("Projects");
            }
            else {
                $(this).children("#category").addClass("Articles");
            }
        }); 
    });
    */
}(window, jQuery));