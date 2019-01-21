$(function () {
    // $('.orderdetail').width(innerWidth)

    $('.bill #pay').click(function () {
        console.log('123')
        var identifier = $(this).attr('identifier')
        data = {
            'identifier':identifier
        }
        $.get('/mei/pay/', data, function (response) {
            console.log(response)
            if (response.status == 1){
                window.open(response.alipayurl, target='_self')
            }
        })
    })
})