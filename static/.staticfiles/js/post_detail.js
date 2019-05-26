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
        var disqus_config = function () {
            this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
            this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
        };
        $(function() { // DON'T EDIT BELOW THIS LINE
            var d = document, s = d.createElement('script');
            s.src = 'https://san-kim.disqus.com/embed.js';
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
        })();
    });
}(window, jQuery));