//1.定义长连接
var conn = null;

//实时更新信息
function update_ui(e) {
    var data = e.data;
    data = JSON.parse(data);  //把json转化为对象
    //空气温度
    option_kongqiwen.series[0].data[0] = (data['kongqiwendu']);
    option_kongqiwen.series[0].detail = ({"formatter": "{value}"});
    option_kongqiwen.title[0].text = data['nt']+"-温度(单位 ℃)";
    myChart_kongqiwen.setOption(option_kongqiwen);

    //空气湿度
    option_kongqishi.series[0].data[0] = (data['kongqishidu']);
    option_kongqishi.series[0].detail = ({"formatter": "{value}"});
    option_kongqishi.title[0].text = data['nt']+"-湿度(单位 vol%)";
    myChart_kongqishi.setOption(option_kongqishi);

    //土壤温度
    option_turangwen.series[0].data[0] = data['turangwendu'];
    option_turangwen.series[0].detail = ({"formatter": "{value}"});
    option_turangwen.title[0].text = data['nt']+"-温度(单位 ℃)";
    myChart_turangwen.setOption(option_turangwen);

    //土壤湿度
    option_turangshi.series[0].data[0] = data['turangshidu'];
    option_turangshi.series[0].detail = ({"formatter": "{value}"});
    option_turangshi.title[0].text = data['nt']+"-湿度(单位 vol%)";
    myChart_turangshi.setOption(option_turangshi);

    //光照强度
    option_guangzhao.series[0].data[0] = data['guangzhao'];
    option_guangzhao.series[0].detail = ({"formatter": "{value}"});
    option_guangzhao.title[0].text = data['nt']+"-光照(单位 lux(勒克斯）)";
    myChart_guangzhao.setOption(option_guangzhao);


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
    },10000);
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