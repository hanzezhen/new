$(document).ready(function () {
    $('#uname').focusout(function () {

        var a = $.trim($('#uname').val());
        if (a == '') {
            $('#che').text('请输入用户名')
        }
        else {
            $.ajax({
                    url: '/ajax1get/',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({
                        'username': a
                    }),
                    headers: {'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()},

                    success: function (data) {
                        var dataObj = JSON.parse(data);
                        if (dataObj['sttr'] == 'yes') {
                            $('#che').text('用户名已存在,请重新输入!');
                            $('#uname').val('')
                        }
                        else if (dataObj['sttr'] == 'no') {
                            $('#che').text('用户名可以使用!');
                        }
                    }
                }
            )

        }
    })

    $('#uname').focus(function () {
        $('#che').text('')
    })
})