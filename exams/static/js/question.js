$(function () {
    $("#frm-answers input[type=radio]").click(function () {
        var answer = $(this).val();
        $.ajax({
            url: '/prova/enviar-resposta/',
            data: $('#frm-answers').serialize(),
            type: 'post',
            cache: false
        });
    });
});