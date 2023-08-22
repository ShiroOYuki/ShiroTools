$(document).ready(function(){
    let h_text = $(".hours");
    let m_text = $(".minutes");
    let s_text = $(".seconds");

    function time_update() {
        let now = new Date()
        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();
        h_text.text(("0" + hours).slice(-2));
        m_text.text(("0" + minutes).slice(-2));
        s_text.text(("0" + seconds).slice(-2));
    }

    time_update();
    setInterval(time_update, 1000);

    $(".bg").click(function(){
        window.location = "/";
    });
});