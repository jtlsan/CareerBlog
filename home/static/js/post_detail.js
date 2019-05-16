(function(win, $) {
    $(document).ready(function() {
        $("#delete_button").click(function(e) {
            e.preventDefault();
            var is_delete = confirm("해당 포스트를 삭제하시겠습니까?");
            if(is_delete) {
                var target = $("#delete_button").attr("href");
                location.href = target;
            }
        });
        $(function(){
            var txt = $("#category").text();
            if (txt == "Study") {
                $("#category").css("background-color", "#D5FBCC");
            }
            else if (txt == "Projects") {
                $("#category").css("background-color", "#CCD5FB");
            }
            else {
                $("#category").css("background-color", "#FBCCD5");
            }
        });
    });
}(window, jQuery));