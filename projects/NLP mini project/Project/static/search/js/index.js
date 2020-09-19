$(document).ready(function () {

    function get_search(variable) {
        $.ajax('search_json', { method: 'GET', data: { 'keyword': variable } }).done(function (result) {
            console.log(result);
            for (var i = result.length - 1; i >= 0; i--) {
                $("#url_list").append('<tr><td><a href="' + result[i] + '"> ' + result[i] + '</a></td><tr>');
            };

            var size = parseInt(document.getElementById("count").value);
            size = size - 1;
            console.log(size);
            if (size == 0) {
                document.getElementById("loading").style.display = "none";
            }
            else {
                document.getElementById("count").value = size;
            }
        }).fail(function () {
            alert('Server down');
        });
    }

    get_search($("#email").text());
    get_search($("#aadhar").text());
    get_search($("#name").text());
    get_search($("#phone").text());

});
