$(document).ready(function(){
    let expand_btn = $(".bar-btn");
    let navbar = $(".navbar");
    
    expand_btn.click(function(){
        if (navbar.hasClass("closed")) {
            navbar.removeClass("closed");
            navbar.animate({ width: '98vw' }, 1000, 'swing').promise().done(function() {
                navbar.addClass("expanded");
            }); 
        }
        else {
            navbar.removeClass("expanded");
            navbar.animate({ width: '200px' }, 1000, 'swing').promise().done(function() {
                navbar.addClass('closed');
            }); 
        }
    });
});