import time
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
    port=3306,
    user='root',
    passwd='292215',
    db='watermelon',
    charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
while True:
    print(time.strftime('%Y.%m.%d', time.localtime(time.time())))
    right_time = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    #当前时间的时间戳
    rt = time.mktime(time.strptime(str(right_time), '%Y.%m.%d'))
    #rt = time.mktime(time.strptime('2018.12.25', '%Y.%m.%d'))
    print(time.mktime(time.strptime(str(right_time), '%Y.%m.%d')))
    sql = "SELECT * FROM `analyse_plantdata` LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchone()
    hms = time.mktime(time.strptime(str(result[2]), '%Y-%m-%d'))#缓苗期开始时间戳
    hme = time.mktime(time.strptime(str(result[3]), '%Y-%m-%d'))#缓苗期结束时间戳
    sms = time.mktime(time.strptime(str(result[4]), '%Y-%m-%d'))  # 伸蔓期开始时间戳
    sme = time.mktime(time.strptime(str(result[5]), '%Y-%m-%d'))  # 伸蔓期结束时间戳
    zgs = time.mktime(time.strptime(str(result[6]), '%Y-%m-%d'))  # 坐果期开始时间戳
    zge = time.mktime(time.strptime(str(result[7]), '%Y-%m-%d'))  # 坐果期结束时间戳
    pgs = time.mktime(time.strptime(str(result[8]), '%Y-%m-%d'))  # 澎瓜期开始时间戳
    pge = time.mktime(time.strptime(str(result[9]), '%Y-%m-%d'))  # 澎瓜期结束时间戳
    css = time.mktime(time.strptime(str(result[10]), '%Y-%m-%d'))  # 成熟期开始时间戳
    cse = time.mktime(time.strptime(str(result[11]), '%Y-%m-%d'))  # 成熟期结束时间戳
    #判断当前日期处于哪个时期
    if hms<=rt<=hme:
        hmsql = "SELECT * FROM `analyse_plantrange`;"
        cursor.execute(hmsql)
        results = cursor.fetchall()
        hm_light_h = results[0][2] #缓苗期光照最高值
        hm_light_l = results[0][3] #缓苗期光照最低值
        hm_airtemperture_h = results[1][2]  # 缓苗期空气温度最高值
        hm_airtemperture_l = results[1][3]  # 缓苗期空气温度最低值
        hm_airshidu_h = results[2][2]  # 缓苗期空气湿度最高值
        hm_airshidu_l = results[2][3]  # 缓苗期空气湿度最低值
        hm_earthshidu_h = results[3][2]  # 缓苗期土壤湿度最高值
        hm_earthshidu_l = results[3][3]  # 缓苗期土壤湿度最低值
        hm_earthtem_h = results[4][2]  # 缓苗期土壤温度最高值
        hm_earthtem_l = results[4][3]  # 缓苗期土壤温度最低值
        #获取当前传感器数据，和上述信息进行比较，控制相应设备
    else:
        if sms<=rt<=sme:
            smsql = "SELECT * FROM `analyse_plantrange`;"
            cursor.execute(smsql)
            results = cursor.fetchall()
            sm_light_h = results[0][4]  # 伸蔓期光照最高值
            sm_light_l = results[0][5]  # 伸蔓期光照最低值
            sm_airtemperture_h = results[1][4]  # 伸蔓期空气温度最高值
            sm_airtemperture_l = results[1][5]  # 伸蔓期空气温度最低值
            sm_airshidu_h = results[2][4]  # 伸蔓期空气湿度最高值
            sm_airshidu_l = results[2][5]  # 伸蔓期空气湿度最低值
            sm_earthshidu_h = results[3][4]  # 伸蔓期土壤湿度最高值
            sm_earthshidu_l = results[3][5]  # 伸蔓期土壤湿度最低值
            sm_earthtem_h = results[4][4]  # 伸蔓期土壤温度最高值
            sm_earthtem_l = results[4][5]  # 伸蔓期土壤温度最低值
            # 获取当前传感器数据，和上述信息进行比较，控制相应设备
        else:
            if zgs<=rt<=zge:
                zgsql = "SELECT * FROM `analyse_plantrange`;"
                cursor.execute(zgsql)
                results = cursor.fetchall()
                zg_light_h = results[0][6]  # 坐果期光照最高值
                zg_light_l = results[0][7]  # 坐果期光照最低值
                zg_airtemperture_h = results[1][6]  # 坐果期空气温度最高值
                zg_airtemperture_l = results[1][7]  # 坐果期空气温度最低值
                zg_airshidu_h = results[2][6]  # 坐果期空气湿度最高值
                zg_airshidu_l = results[2][7]  # 坐果期空气湿度最低值
                zg_earthshidu_h = results[3][6]  # 坐果期土壤湿度最高值
                zg_earthshidu_l = results[3][7]  # 坐果期土壤湿度最低值
                zg_earthtem_h = results[4][6]  # 坐果期土壤温度最高值
                zg_earthtem_l = results[4][7]  # 坐果期土壤温度最低值
                # 获取当前传感器数据，和上述信息进行比较，控制相应设备
            else:
                if pgs<=rt<=pge:
                    pgsql = "SELECT * FROM `analyse_plantrange`;"
                    cursor.execute(pgsql)
                    results = cursor.fetchall()
                    pg_light_h = results[0][8]  # 澎瓜期光照最高值
                    pg_light_l = results[0][9]  # 澎瓜期光照最低值
                    pg_airtemperture_h = results[1][8]  # 澎瓜期空气温度最高值
                    pg_airtemperture_l = results[1][9]  # 澎瓜期空气温度最低值
                    pg_airshidu_h = results[2][8]  # 澎瓜期空气湿度最高值
                    pg_airshidu_l = results[2][9]  # 澎瓜期空气湿度最低值
                    pg_earthshidu_h = results[3][8]  # 澎瓜期土壤湿度最高值
                    pg_earthshidu_l = results[3][9]  # 澎瓜期土壤湿度最低值
                    pg_earthtem_h = results[4][8]  # 澎瓜期土壤温度最高值
                    pg_earthtem_l = results[4][9]  # 澎瓜期土壤温度最低值
                    # 获取当前传感器数据，和上述信息进行比较，控制相应设备
                else:
                    if css<=rt<=cse:
                        cssql = "SELECT * FROM `analyse_plantrange`;"
                        cursor.execute(cssql)
                        results = cursor.fetchall()
                        cs_light_h = results[0][10]  # 成熟期光照最高值
                        cs_light_l = results[0][11]  # 成熟期光照最低值
                        cs_airtemperture_h = results[1][10]  # 成熟期空气温度最高值
                        cs_airtemperture_l = results[1][11]  # 成熟期空气温度最低值
                        cs_airshidu_h = results[2][10]  # 成熟期空气湿度最高值
                        cs_airshidu_l = results[2][11]  # 成熟期空气湿度最低值
                        cs_earthshidu_h = results[3][10]  # 成熟期土壤湿度最高值
                        cs_earthshidu_l = results[3][11]  # 成熟期土壤湿度最低值
                        cs_earthtem_h = results[4][10]  # 成熟期土壤温度最高值
                        cs_earthtem_l = results[4][11]  # 成熟期土壤温度最低值
                        # 获取当前传感器数据，和上述信息进行比较，控制相应设备
                    else:
                        print("当前日期未处于设置的西瓜生长阶段时间中")


    time.sleep(60)