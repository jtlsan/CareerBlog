(function(win, $){
    $(document).ready(function() {
        alert("dd");
        var txt = $("section p:first label").text();
        alert(txt);
    });
}(window, jQuery));