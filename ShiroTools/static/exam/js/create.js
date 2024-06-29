$(document).ready(() => {
    $(".dropdown-box").click(function(e) {
        $(this).toggleClass("hide");
        $(this).toggleClass("show");
    });
    
    $(".dropdown-item").click(function(e) {
        $(this).parents(".dropdown-box").find(".selected-item").text($(this).find("p").text());
    });

});