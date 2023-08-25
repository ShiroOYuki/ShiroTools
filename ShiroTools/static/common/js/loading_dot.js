$(document).ready(function(){
    let dot = $(".dot");
    function dotAnimation() {
        dot.toggleClass("bigger");
    }
    setInterval(dotAnimation, 3000);
});