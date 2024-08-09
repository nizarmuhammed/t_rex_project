$(document).ready(function(){
    $("#loginbtn").click(function(){
        $Email = $('#emailfield').val();
        $Password = $('#passwordfield').val();
        $.ajax({
            url: 'logining',
            data: {'email': $Email, 'password': $Password},
            type: 'get',
            datatype: 'json',
            success: function(d){
                if(d.sts)
                {
                    alert(d.msg);
                    // Redirect to a dashboard or home page upon successful login
                    window.location.href = 'index';
                }
                else
                {
                    alert(d.msg);
                }
            },
            error: function(d)
            {
                console.log(d);
            }
        });
    });
});
