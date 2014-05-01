$('#password2').blur(function() {
				var a=$("#password1").val()
				var b=$("#password2").val()
				if (a!=b) {
				$('span:eq(1)').html("两次密码不一致，请重新输入。")
				$("#password1").val('')
				$("#password2").val('')
				$("#password1").focus()
				}
				else if (a==''|| b=='') {
				$('span:eq(1)').html("密码不能为空。")
				$("#password1").val('')
				$("#password2").val('')
				$("#password1").focus()
				}					
				else{
					$('span:eq(1)').html("^_^")
				}
});
$('#username').blur(function(){
         var obj1=$('#username').val();   
         var reg1=/\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/; 
         var reg2=/^0{0,1}(13[0-9]|15[7-9]|153|156|18[7-9])[0-9]{8}$/;
         if (obj1=='') {
         	$('#uname').html("用户名不能为空。");
         }
         else if(!reg2.test(obj1) && !reg1.test(obj1)){        
             $('#uname').html("邮箱地址或手机号码错误。");
             $('#username').val('');
         }
         else{   
             $("#uname").html("^_^");   
         }   
});
$(function(){
    var a=$('b').length
    var b=$('p').length
    if (a>0) {
      alert("登录失败，用户名或密码错误。")
    }
    if (b>0) {
      alert("注册成功！可以去登录啦！")
    }    
  });
