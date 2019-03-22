$(document).ready(() => {
    $("#button-json").click(() => {
        $.post('http://3.51.55.92:8086/', { "json_data": "aloha!" }, function (data) {
            $("#json-response").html(data);
            succ();
        });
    });
});

let succ = () => {
    $("#json-success").removeClass('uk-hidden');
}