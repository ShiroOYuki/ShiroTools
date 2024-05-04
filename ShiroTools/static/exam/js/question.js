$(document).ready(function(){
    $(".option").click(function(event){
        event.preventDefault();
        let target = $("#" + $(this).data("target"));
        console.log("#" + $(this).data("target"));
        let radio = $(this).children("input:first")[0];
        if (radio.checked) {
            console.log("A");
            radio.checked = false;
            target.removeClass("done");
            $(this).closest(".question-box").attr("data-ans", null);
        }
        else {
            radio.checked = true;
            target.addClass("done");
            $(this).closest(".question-box").attr("data-ans", $(this).find("input").val());
        }
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
        let curr_url = window.location.href;
        curr_url = curr_url.replace(/\/$/, "");
        $.ajax({
            type: "POST",
            url: curr_url + "/submit",
            data: { 
                "ans": ans,
                "csrfmiddlewaretoken": csrf_token
            },
            success: function(response) {
                window.location.href = curr_url + "/answer";
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });

    $(".multiple.option").click(function() {
        let target = $("#" + $(this).data("target")); // 快速跳躍題目的按鈕
        let data = ""
        $(this).parent().children().map((i, option) => {
            checkbox = $(option).children("input:first")[0];
            if (checkbox.checked) {
                data += $(checkbox).val();
            }
        });
        console.log(data);
        if (data === "") {
            $(target).removeClass("done");
            $(this).closest(".question-box").attr("data-ans", null);
        }
        else {
            $(this).closest(".question-box").attr("data-ans", data);
        }
    })
});