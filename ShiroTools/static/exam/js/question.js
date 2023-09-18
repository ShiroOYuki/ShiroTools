$(document).ready(function(){
    $(".radio").click(function(){
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        target.addClass("done");
    });

    $(".question-link").click(function(){
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        $(".col").animate({
            scrollTop: target.offset().top
        }, 1000);
    });

    $(".ans-ipt").on("input", function(){
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        if ($(this).val() != "") {
            target.addClass("done");
        } 
        else {
            target.removeClass("done");
        }
    });
});