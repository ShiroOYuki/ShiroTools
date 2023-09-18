$(document).ready(function(){
    $(".radio").click(function(){
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        target.addClass("done");
        $(this).closest(".question-box").attr("data-ans", $(this).find("input").val());
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

    $(".ans-ipt").on("change", function(){
        if ($(this).val() != "") {
            $(this).closest(".question-box").attr("data-ans", $(this).val());
        } 
        else {
            $(this).closest(".question-box").attr("data-ans", "-1");
        }
    });

    $(".submit-btn").click(function(){
        let ans = [];
        $(".question-box").each(function(){
            ans.push($(this).data("ans"));
        });
        console.log(ans);
        let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: "POST",
                url: "./ans",
                data: { 
                    ans: ans,
                    "csrfmiddlewaretoken": csrf_token
                },
                success: function(response) {
                    
                },
                error: function(error) {
                    console.log("Error:", error);
                }
            });
    });
});