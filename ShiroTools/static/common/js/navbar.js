$(document).ready(function(){
    let expand_btn = $(".bar-btn");
    let navbar = $(".navbar");
    
    expand_btn.click(function(){
        navbar.toggleClass("expanded closed");
        if (navbar.hasClass('closed')) {
            navbar.find('.nav-items').css('overflow-x', 'hidden');
        }
    });

    navbar.on('transitionend', function() {
        if (navbar.hasClass('expanded')) {
            navbar.find('.nav-items').css('overflow-x', 'auto');
        } 
    });
});