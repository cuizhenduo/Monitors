//1.定义长连接
var conn = null;
//进度条变化
function progress_status(val) {
    var data = "";
    if (val>=0&&val<25){
        data = " bg-success ";
    }else if (val>=25&&val<50){
        data = "";
    }else if (val>=50&&val<75){
        data = " bg-warning ";
    }else if (val>=75){
        data = " bg-danger ";
    }
    return data;
}
//实时更新信息
function update_ui(e) {
    var data = e.data;
    data = JSON.parse(data);  //把json转化为对象
    //CPU平均使用率
    option_cpu_avg.series[0].data[0] = (data['cpu']['percent_avg']/100).toFixed(4);
    option_cpu_avg.title[0].text = data['dt']+"-温度";
    myChart_cpu_avg.setOption(option_cpu_avg);
    //cpu每个使用率
    var cpu_per = '';
    for (var k in  data['cpu']['percent_per']){
        var num = parseInt(k);
        cpu_per += "<tr><td class=\"text-primary\" style=\"width: 30%\">CPU"+num+"</td>";
        cpu_per += "<td><div class=\"progress\"><div class=\"progress-bar progress-bar-striped progress-bar-animated"+progress_status(data['cpu']['percent_per'][k])+"\" role=\"progressbar\" aria-valuenow=\""+data['cpu']['percent_per'][k]+"\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: "+data['cpu']['percent_per'][k]+"%\">"+data['cpu']['percent_per'][k]+"%</div></div></td></tr>";
    }
    document.getElementById("tb_cpu_per").innerHTML = cpu_per;
    //磁盘使用率
    var disk = "";
    for (var k in data['disk']){
        var cd = data['disk'][k];
        disk += "<tr><td>"+cd['device']+"</td>";
        disk += "<td>"+cd['mountpoint']+"</td>";
        disk += "<td>"+cd['fstype']+"</td>";
        disk += "<td>"+cd['opts']+"</td>";
        disk += "<td class=\"text-danger\">"+cd['used']['total']+"</td>";
        disk += "<td class=\"text-danger\">"+cd['used']['used']+"</td>";
        disk += "<td class=\"text-danger\">"+cd['used']['free']+"</td>";
        disk += "<td><div class=\"progress\"><div class=\"progress-bar progress-bar-striped progress-bar-animated"+progress_status(cd['used']['percent'])+"\" role=\"progressbar\" aria-valuenow=\""+cd['used']['percent']+"\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: "+cd['used']['percent']+"%\">"+cd['used']['percent']+"%</div></div></td></tr>";
    }
    document.getElementById("tb_disk").innerHTML = disk;
    //内存使用率
    option_mem.series[0].data[0] = data['mem']['percent'];
    option_mem.title[0].text = data['dt']+"-湿度";
    myChart_mem.setOption(option_mem);
    var mem_percent = data['mem']['percent'];
    var mem_total = data['mem']['total'];
    var mem_used = data['mem']['used'];
    var mem_free = data['mem']['free'];
    document.getElementById("mem_percent").innerHTML = mem_percent;
    document.getElementById("mem_total").innerHTML = mem_total;
    document.getElementById("mem_used").innerHTML = mem_used;
    document.getElementById("mem_free").innerHTML = mem_free;
    //交换分区使用率
    option_swap .series[0].data[0] = data['swap']['percent'];
    option_swap .title[0].text = data['dt']+"-光照";
    myChart_swap.setOption(option_swap);
    var mem_percent = data['swap']['percent'];
    var mem_total = data['swap']['total'];
    var mem_used = data['swap']['used'];
    var mem_free = data['swap']['free'];
    document.getElementById("swap_percent").innerHTML = mem_percent;
    document.getElementById("swap_total").innerHTML = mem_total;
    document.getElementById("swap_used").innerHTML = mem_used;
    document.getElementById("swap_free").innerHTML = mem_free;
    //网络信息更新
    var net = "";
    for(var k in data['net']){
        var cd = data['net'][k];
        if(parseInt(cd['bytes_sent'])!=0 && parseInt(cd["bytes_recv"])!=0){
            var index = parseInt(k)+1;
            var op = eval("option_net"+index);
            var ch = eval("myChart_net"+index);
            op.title[0].text = data["dt"]+"-"+cd["name"]+"网卡信息";
            op.series[0].data=[
                {"name":"收包数","value":cd['packets_recv']},
                {"name":"发包数","value":cd['packets_sent']}
            ];
            op.series[1].data=[
                {"name":"收字节","value":cd['bytes_recv']},
                {"name":"发字节","value":cd['bytes_sent']}
            ];
            ch.setOption(op);
        }
        net +="<tr><td>"+cd['name']+"</td>";
        net +="<td class=\"text-danger\">"+cd['bytes_sent']+"</td>";
        net +="<td class=\"text-danger\">"+cd['bytes_recv']+"</td>";
        net +="<td class=\"text-danger\">"+cd['packets_sent']+"</td>";
        net +="<td class=\"text-danger\">"+cd['packets_recv']+"</td>";
        net +="<td>"+cd['family']+"</td>";
        net +="<td>"+cd['address']+"</td>";
        net +="<td>"+cd['netmask']+"</td>";
        if(cd['broadcast']){
            net +="<td>"+cd['broadcast']+"</td></tr>";
        }else {
            net +="<td>无</td></tr>";
        }
    }
    document.getElementById('tb_net').innerHTML = net;
}

//2定义连接函数
function connect() {
    disconnect();//把之前没关闭的链接关闭再创建新的链接
    //定义协议
    var transports = ["websocket"];
    //创建连接对象
    conn = new SockJS("http://"+window.location.host+"/real/time",transports);//window.location.host获取主机地址，transports把http协议转成ws协议
    //建立连接
    conn.onopen = function () {
        console.log("连接成功！");
    };
    //建立接收消息
    conn.onmessage = function (e) {
        console.log(e.data);
        update_ui(e);
    };
    //建立关闭连接
    conn.onclose = function () {
        console.log("断开连接！");
    };
    //每个几秒触发一个事件
    setInterval(function () {
        conn.send("system");
    },1000);
}
//3定义断开连接函数
function disconnect() {
    if (conn!=null){
        conn.close(); //关闭连接
        conn = null;
    }
}
//4刷新断线重连判断
if(conn == null){
    connect();
}else {
    disconnect();
}