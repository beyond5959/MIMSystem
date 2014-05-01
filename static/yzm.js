window.onload=createCode;
document.getElementById("checkCode1").onclick=createCode;
document.getElementById("checkCode2").onclick=createCode;
document.getElementById("yzm").onblur=validateCode;
var code;
function createCode() {
            code = "";
            var codeLength = 4;
            var checkCode = document.getElementById("checkCode1");
            var codeChars = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'); 
            for (var i = 0; i < codeLength; i++) 
            {
                var charNum = Math.floor(Math.random() * 26);
                code += codeChars[charNum];
            }
            if (checkCode) 
            {
                checkCode.className = "code";
                checkCode.innerHTML = code;
            }
        }
function validateCode() 
        {
            var inputCode =$("#yzm").val();
            if (inputCode.toUpperCase()=="") {
                $("#yanzm").html(" &nbsp;验证码不能为空！");
            }
            else if (inputCode.toUpperCase()!="" && inputCode.toUpperCase() != code.toUpperCase()) 
            {
                $("#yanzm").html(" &nbsp;验证码输入有误！");
                $("#yzm").val("");
                createCode();
            }
            else 
            {
                $("#yanzm").html("^_^");
            }        
        } 
 