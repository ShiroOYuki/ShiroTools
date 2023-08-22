$(document).ready(function(){
    let recent_btn = $(".recent-btn");
    let recent = $(".recent");
    let box = $(".col-box");
    let announcement_btn = $(".announcement-btn");
    let announcement_box = $(".announcement");
    let log_btn = $(".log-btn");
    let log_box = $(".log");

    recent_btn.click(function(){
        recent.toggleClass("expanded closed");
        if (box.hasClass("expanded")) {
            box.toggleClass("full");
        }
    });

    announcement_btn.click(function(){
        announcement_box.toggleClass("expanded closed");
    });

    log_btn.click(function(){
        log_box.toggleClass("expanded closed");
    });
});