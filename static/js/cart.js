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
                total()
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
                total()
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


    //计算总数
    function total() {
        var sum = 0
        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')

            if ($confirm.find('.glyphicon-ok').length){
                var num = $content.find('.num').attr('num')
                var price = $content.find('.price').attr('price')
                ap = num * price
                sum += num * price
            }
        })
    }

        //设置显示金额

    // $('.bill .total').html(parseFloat(sum))


    // 下单
    $('.bill-right #generateorder').click(function () {
        console.log('123')
        $.get('/mei/generateorder/', function (response) {
            console.log(response)
            if (response.status == 1) {  // 订单详情页
                window.open('/mei/orderdetail/' + response.identifier + '/', target = '_self')
            }
        })
    })


    //     $('.btn3').click(function () {
    //         console.log('13')
    //     var identifier = $(this).attr('identifier')
    //     data = {
    //         'identifier':identifier
    //     }
    //     $.get('/mei/pay/', data, function (response) {
    //         console.log(response)
    //         if (response.status == 1){
    //             window.open(response.alipayurl, target='_self')
    //         }
    //     })
    // })

})