(function(win, $){
    $(document).ready(function() {
        $("section p:eq(0) label").text("제목 : ");
        var txt = $("section p:eq(2) label").text("내용 : ");
        $("form .buttons").css("width", screen.width);
    });
}(window, jQuery));