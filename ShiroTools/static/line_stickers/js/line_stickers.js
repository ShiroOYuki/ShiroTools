$(document).ready(function(){
    let submit_btn = $("#url-submit");
    let url_ipt = $("#sticker_url");

    submit_btn.click(function(){
        let url = url_ipt.val();
        console.log(url);
        if (url.startsWith("https://store.line.me/stickershop/product")) {
            console.log("True");
            let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: "POST",
                url: "./get_stickers",
                data: { 
                    name: url,
                    "csrfmiddlewaretoken": csrf_token
                },
                success: function(response) {
                    let imgs = response.names;
                    let img_container = $(".imgs");
                    img_container.empty();
                    for (i=0;i<imgs.length;i++){
                        img_container.append(
                            "<a class='img-box' href='" + imgs[i] + "' download><img src='" + imgs[i] + "' class='preview'><div class='download-icon-box'><i class='download-icon bi bi-arrow-down-circle'></i></div></a>"
                        );
                    }

                    let info_box = $(".info-box");
                    info_box.empty();
                    let title = response.title;
                    info_box.append("<p>貼圖名稱：" + title + "</p>")
                    let author = response.author;
                    info_box.append("<p>作者：" + author + "</p>")

                    let imgs_container = $(".imgs-container");
                    let zip = response.zip;
                    imgs_container.append("<a class='download-all' href='" + zip + "' download>下載全部</a>");
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