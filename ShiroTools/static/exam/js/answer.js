$(document).ready(function(){
    $(".question-link").click(function(){
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        $(".col").animate({
            scrollTop: target.offset().top
        }, 1000);
    });
});