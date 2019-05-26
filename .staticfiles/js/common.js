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
        
        $(".category-list").slideUp(0);
        $("#nav-list>li:eq(2) a").on("click", function(e) {
            e.preventDefault();
            if ($(this).parent().hasClass('on')){
                location.href = $(this).attr('href');
            }
        })    
        $("#nav-list>li:eq(3) a").on("click", function(e) {
            e.preventDefault();
            if ($(this).parent().hasClass('on')){
                location.href = $(this).attr('href');
            }
        }) 
        $(document).on("click", "#nav-list li.on li a", function() {
            location.href = $(this).attr('href');
        })    
        $("#nav-list>li").eq(2).on("click", function(e) {
            e.preventDefault();
                $(this).children('.category-list').slideDown(300);
                $(this).addClass("on");
                $(this).siblings('.on').children('.category-list').slideUp(300);
                $(this).siblings('.on').removeClass('on');
        })
        $("#nav-list>li").eq(3).on("click", function(e) {
            e.preventDefault();
            $(this).children('.category-list').slideDown(300);
            $(this).addClass('on');
            $(this).siblings('.on').children('.category-list').slideUp(300);
            $(this).siblings('.on').removeClass('on');
        })
        /*
        $("#nav-list li").eq(2).on("mouseleave", function() {
            $(this).children('.category-list').slideUp(300);
            $(this).toggleClass("on");
        })
        $("#nav-list li").eq(3).on("mouseleave", function() {
            $(this).children('.category-list').slideUp(300);
            $(this).toggleClass("on");
        })
        */
    });

}(window, jQuery));