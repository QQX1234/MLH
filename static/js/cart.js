$(function () {
    // 选择
    $('.list_content .confirm-wrapper').click(function () {
        // 谁， 购物车（哪条记录）
        var cartid = $(this).attr('cartid')
        var $span = $(this).find('span')

        data = {
            'cartid':cartid
        }

        // 发起ajax
        $.get('/mei/changecartstatus/', data, function (response) {
            console.log(response)
            if (response.status){
                if (response.isselect){ // 选中
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {    // 未选中
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }
            }
        })
    })




	      // 获取订单详情
    // 商品加操作
    $('.number .add').click(function () {
        console.log('加操作')

        var goodsid = $(this).attr('goodsid')
        var $that = $(this)

        data = {
            'goodsid': goodsid
        }
        //发起ａｊａｘ
        $.get('/mei/addcart/', data, function (response) {
            // console.log(response)
            if (response.status == 0){
                window.open('/mei/login',target='_self')

            } else if (response.status == 1) {

                var count = (response.number)
                $that.prev().show().html(count)
                if (count >= 1) {
                    $that.prev().prev().css('color', 'black')
                    $that.prev().show()
                    $that.prev().prev().show()
                } else {
                    $that.prev().prev().hide()
                    $that.prev().hide()
                }


            }

        })
    })

    //商品减操作
    $('.number .reduce').click(function () {
        // console.log('nihao')
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)

        data = {
            'goodsid': goodsid
        }


        $.get('/mei/subcart/', data, function (response) {
            // console.log(response)
            if (response.status == 1) {
                var count = (response.number)
                if (count <1) {
                    $that.hide()
                    $that.next().hide()
                } else {
                    $that.next().show().html(count)
                    $that.show()
                    $that.next().show()
                }

            }

        })
    })





    // 全选操作
    $('.bill .all').click(function () {
        // 获取
        var isall = $(this).attr('isall')
        // 转换
        isall = (isall=='true') ? true : false
        // 取反
        isall = !isall
        // 设置回去
        $(this).attr('isall', isall)

        if (isall){
            $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }

        // true/false
        data = {
            'isall':isall
        }

        $.get('/mei/changecartall/', data, function (response) {
            console.log(response)
            if (response.status == 1){
                $('.confirm-wrapper').each(function () {
                    if (isall){ // 选中
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {    // 取消选中
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                })
            }
        })
    })
})