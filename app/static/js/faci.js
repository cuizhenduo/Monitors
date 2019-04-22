/**
 * Created by czd on 2019/4/3.
 */

function myOpen(id) {
    var text1 = document.getElementById(id).innerText;
    document.getElementById(id).innerText = "打开";
    //stat.innerText = "打开";
    $.ajax({
        url:"http://127.0.0.1:8000/ah/",
        async:true,
        data:{"zt":text1,"id":id},
        dataType:"json",
        success:function(data){
            console.log(data.states);
            },
        error:function(){alert("请求错误");},
        type:"GET"
        });
}
function myClose(id) {
    var text1 = document.getElementById(id).innerText;
    var stat = document.getElementById(id);
    stat.innerText = "关闭";
    $.ajax({
        url:"http://127.0.0.1:8000/ahc/",
        async:true,
        data:{"zt":text1,"id":id},
        dataType:"json",
        success:function(data){
            console.log(data.states);
            },
        error:function(){alert("请求错误");},
        type:"GET"
        });
}