$(document).ready(function(){
    let submit_btn = $("#url-submit");
    let url_ipt = $("#sticker_url");

    let dot = $(".dot");
    function dotAnimation() {
        dot.toggleClass("bigger");
    }

    submit_btn.click(function(){
        let dot_box = $(".dot-box");
        dot_box.css("display", "flex");
        let dot_animation = setInterval(dotAnimation, 3000);
        let url = url_ipt.val();
        let img_container = $(".imgs");
        img_container.empty();
        let info_box = $(".info-box");
        info_box.empty();
        info_box.append("<p class='info-text'></p>")
        console.log(url);
        if (url.startsWith("https://store.line.me/stickershop/product")) {
            console.log("True");
            let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            let progress_bar_url = "get_stickers";
            let progress_bg = $(".progress-bg");
            let progress_bar = $(".progress-bar");
            let info_text = $(".info-text");
            info_text.text("載入中 - 0%");
            progress_bg.css("visibility", "visible");
            progress_bar.css("visibility", "visible");
            let progress_itv = setInterval(() => {
                $.getJSON(progress_bar_url, (pct) => {
                    console.log(pct);
                    info_text.text("載入中 - " + pct + "%");
                    progress_bar.css("width", pct + "%");
                    if (pct >= 100) clearInterval(progress_itv);
                });
            }, 500);
            $.ajax({
                type: "POST",
                url: "./get_stickers",
                data: { 
                    name: url,
                    "csrfmiddlewaretoken": csrf_token
                },
                success: function(response) {
                    info_box.empty();
                    dot_box.css("display", "none");
                    clearInterval(dot_animation);
                    progress_bar.css("width", "100%");
                    dot.removeClass("bigger");
                    if ("msg" in response) {
                        info_box.append("<p>載入失敗</p>")
                    }
                    else {
                        clearInterval(progress_itv);
                        progress_bg.css("visibility", "hidden");
                        progress_bar.css("visibility", "hidden");
                        let imgs = response.names;
                        let img_elements = "";
                        for (i=0;i<imgs.length;i++){
                            img_elements += "<a class='img-box' href='" + imgs[i] + "' download><img src='" + imgs[i] + "' class='preview'><div class='download-icon-box'><i class='download-icon bi bi-arrow-down-circle'></i></div></a>"
                        }
                        img_container.append(img_elements);
                        let title = response.title;
                        info_box.append("<p>貼圖名稱：" + title + "</p>")
                        let author = response.author;
                        info_box.append("<p>作者：" + author + "</p>")
    
                        let imgs_container = $(".imgs-container");
                        let zip = response.zip;
                        imgs_container.append("<a class='download-all' href='" + zip + "' download>下載全部</a>");
                    }
                },
                error: function(error) {
                    console.log("Error:", error);
                }
            });
        }
        else {
            console.log("False");
        }
    });
});