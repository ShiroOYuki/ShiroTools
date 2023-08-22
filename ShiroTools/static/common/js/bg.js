$(document).ready(function(){
    let neko = $('.bg');
    neko.toggleClass('light dark');

    function toggleOpacity() {
        neko.toggleClass('light dark');
    }
      
    // 每 3 秒自動切換透明度
    setInterval(toggleOpacity, 5000); // 3000 毫秒 = 3 秒
});