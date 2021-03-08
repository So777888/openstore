# -*- coding: utf-8 -*-
import pymysql
import time

def update_store_status(userId,merchant_type):

    time01 = int(time.time())

    userId = int(userId)
    if (userId % 2) == 0:
        pp_store_num = 'pp_store_0'
    else:
        pp_store_num = 'pp_store_1'


    coon = pymysql.connect(
        host='192.168.0.100',
        port = 3306,
        user="root",
        password = "123",
        db = pp_store_num,
        charset = "utf8"
    )

    cursor = coon.cursor()

    # 判断对应的库，是否有该店铺
    sql = "select * from store where store_id = " + str(userId)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        if len(result) == 0:
            print("该店铺没有记录")
            return '该店铺没有记录'
    except:
        print("Error: store记录查询失败")

    # 修改store_subject表的状态为2301
    sql = "update store_subject set current_status = 2301 where store_id =" + str(userId)
    try:
        cursor.execute(sql)
        coon.commit()
    except:
        coon.rollback()
        print("Error: 修改store_subject表失败")

    #查询store_subject，该店铺的store_subject_id值
    sql = "select *  from store_subject where store_id =" + str(userId)
    try:
        cursor.execute(sql)
        store_subject_result = cursor.fetchall()
        print(store_subject_result)
        store_subject_id = store_subject_result[0][0]

        if len(store_subject_result) == 0:
            print("该店铺store_subject没有记录")
            return '该店铺没有记录'
    except:
        print("Error: 查询store_subject记录失败")


    #查询store_subject_init表
    sql = "select * from store_subject_init where store_id = " + str(userId)
    try:
        cursor.execute(sql)
        store_subject_init_result = cursor.fetchall()
        print(store_subject_init_result)
        store_subject_init_id = store_subject_init_result[0][0]
        print("store_subject_init_id:",store_subject_init_id)

        if len(store_subject_init_result) == 0:
            print("该店铺store_subject_init表没有记录")
            return '该店铺没有记录'
    except:
        print("Error: 查询store_subject_init表失败")

    #查询微信进件信息表，获取最后一条记录ID
    sql = "select * from store_subject_wechat ORDER BY id desc LIMIT 0,1;"
    try:
        cursor.execute(sql)
        store_wechat_id_result = cursor.fetchall()
        print(store_wechat_id_result)
        store_subject_wechat_id = store_wechat_id_result[0][0]
        print(store_subject_wechat_id)
        store_subject_wechat_id += 1
        print("第二次的值:",store_subject_wechat_id)

    except:
        print("Error: 查询store_subject_wechat表失败")

    # 新增store_subject_wechat表
    sql = "select * from store_subject_wechat where store_id = " + str(userId)
    try:
        cursor.execute(sql)
        store_subject_wechat_result = cursor.fetchall()
        print(store_subject_wechat_result)


        if len(store_subject_wechat_result) == 0:
            print("微信进件表没有数据，需要新增数据")

            sql = "INSERT INTO store_subject_wechat(`id`, `store_id`, `store_subject_id`, `store_subject_init_id`, `out_request_no`, `organization_type`, `business_license_copy`, `business_license_number`, `merchant_name`, `legal_person`, `id_doc_type`, `id_card_copy`, `id_card_national`, `id_card_name`, `id_card_number`, `id_card_valid_time`, `need_account_info`, `contact_type`, `contact_name`, `contact_id_card_number`, `mobile_phone`, `store_name`, `store_url`, `merchant_shortname`, `subject_status`, `content`, `organization_number`, `organization_copy`, `organization_time`, `legal_person_portrait`, `legal_person_national`, `business_license`, `organization_code`, `applyment_id`, `sub_mchid`, `deleted`, `create_time`, `update_time`) VALUES ('" + str(store_subject_wechat_id) +"','"+ str(userId) +"','"+  str(store_subject_id) + "','" + str(store_subject_init_id) + "','pp_964090_1608115567149', '2', '/storage/emulated/0/temp/img_3.png1603798684385.png', '91440101MA9UXA8L0X', '广州百通有限公司', '袁波', 'IDENTIFICATION_TYPE_MAINLAND_IDCARD', 'order/202011/03/5c820a99a6f46e85486dbe549ec24aee.jpg', 'order/202011/03/57ec9826ad939814ca11f8312e8f348d.jpg', '袁波', '410702197211052011', '2023-02-12', 'false', '65', '袁波', '410702197211052011', '13250252111', '10000店铺', 'https://test-wap.ppwang.com/store/964090.html?qd=wx', '10000店铺', 4, '原因', NULL, NULL, NULL, 'order/202011/03/5c820a99a6f46e85486dbe549ec24aee.jpg', 'order/202011/03/57ec9826ad939814ca11f8312e8f348d.jpg', '/storage/emulated/0/temp/img_3.png1603798684385.png', NULL, '2000002166046385', NULL, 0, '2020-12-16 18:46:14', '2020-12-17 15:37:40');"

            try:
                cursor.execute(sql)
                coon.commit()
            except:
                coon.rollback()

    except:
        print("Error: 新增store_subject_wechat表记录失败")


    # 查询支付宝进件信息表，获取最后一条记录ID
    sql = "select * from store_subject_alipay ORDER BY id desc LIMIT 0,1;"
    try:
        cursor.execute(sql)
        store_alipay_id_result = cursor.fetchall()
        print(store_alipay_id_result)
        store_subject_alipay_id = store_alipay_id_result[0][0]
        print(store_subject_alipay_id)
        store_subject_alipay_id += 1
        print("支付宝进件表第二次的值:",store_subject_alipay_id)

    except:
        print("Error: 查询支付宝进件信息表失败")



    sql = "select * from store_subject_alipay where store_id = " + str(userId)
    try:
        cursor.execute(sql)
        store_subject_alipay_result = cursor.fetchall()
        print(store_subject_alipay_result)


        if len(store_subject_alipay_result) == 0:
            print("支付宝进件表没有数据，需要新增数据")

            sql = "INSERT INTO store_subject_alipay(`id`, `store_id`, `store_subject_id`, `store_subject_init_id`, `external_id`, `name`, `alias_name`, `merchant_type`, `mcc`, `cert_type`, `cert_no`, `legal_name`, `legal_cert_no`, `province_code`, `city_code`, `district_code`, `address`, `cert_name`, `service_phone`, `contact_infos_name`, `contact_infos_tag`, `contact_infos_type`, `contack_infos_mobile`, `service`, `sign_time_with_isv`, `alipay_logon_id`, `binding_alipay_logon_id`, `site_type`, `site_name`, `subject_status`, `content`, `legal_person_portrait`, `legal_person_national`, `business_license`, `order_id`, `smid`, `deleted`, `create_time`, `update_time`) VALUES ('" + str(store_subject_alipay_id) +"','"+str(userId) +"','"+  str(store_subject_id) + "','" + str(store_subject_init_id) + "','pp_10000_1602818043045', '洪小明', '" +str(userId) + "', '" +str(merchant_type) + "', '5699', '2011', '799874674978', '洪小明', '6844789749878678', '440000', '440100', '440111', '添加何江区网商路699号', '', '', '洪小明', '02', 'LEGAL_PERSON', '13250252217', 'app支付', '2020-10-16', '1684847687799@qq.com', '1684847687799@qq.com', '02', '批批网', 4, '', '', '', '', '2020101600502000000066580485', '2088010048202378', 0, '2020-10-16 11:14:03', '2020-12-17 15:09:15');"
            try:
                cursor.execute(sql)
                coon.commit()
            except:
                coon.rollback()

    except:
        print("Error: 查询 store_subject_alipay失败")


    # 获取第三方进件日志表的最后一条记录
    sql = "select * from store_subject_log ORDER BY id desc LIMIT 0,1;"

    try:
        cursor.execute(sql)
        store_subject_log_id_result = cursor.fetchall()
        print(store_subject_log_id_result)
        store_subject_log_id_result_id = store_subject_log_id_result[0][0]
        print(store_subject_log_id_result_id)
        store_subject_log_id_result_id += 1
        print("第三方日志表第二次的值:", store_subject_log_id_result_id)

    except:
        print("Error: 查询store_subject_log失败")

    # 第三方进件日志表，添加2301记录
    sql = "INSERT INTO store_subject_log(`id`, `store_id`, `store_subject_id`, `status`, `content`, `create_time`, `update_time`) VALUES ('"+ str(store_subject_log_id_result_id) + " ', '"+str(userId) +"','"+str(store_subject_id) + "', 2301, '进件状态为进件完成', '2020-09-24 18:21:37', '2020-12-21 11:54:44');"
    try:
        cursor.execute(sql)
        coon.commit()
    except:
        coon.rollback()



    # 修改store表的状态为502/301
    current_status = 502
    sql = "update store set current_status = "+ str(current_status) +" where store_id =" + str(userId)

    try:
        cursor.execute(sql)
        coon.commit()
    except:
        coon.rollback()
        print("Error: 修改store表失败")


    coon.close()








if __name__ == '__main__':
    userId = input("请输入需进件完成的店铺:")
    merchant_type = input("店铺类型：5小微，6个人，7企业：")

    update_store_status(userId,merchant_type)
