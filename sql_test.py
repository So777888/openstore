# -*- coding: utf-8 -*-
import pymysql
import time



class update_store_sql(object):


    def __init__(self,userId,merchant_type):

        userId = int(userId)
        if (userId % 2) == 0:
            pp_store_num = 'pp_store_0'
        else:
            pp_store_num = 'pp_store_1'

        # 连接对应的mysql数据库
        self.coon = pymysql.connect(
            host='192.168.0.100',
            port=3306,
            user="root",
            password="123",
            db=pp_store_num,
            charset="utf8"
        )

        # 创建游标
        self.cursor = self.coon.cursor()

        self.userId = userId

        self.merchant_type = merchant_type

        #时间戳 10位数
        self.time01 = int(time.time())

        #微信真实二维码
        self.wechat_content = "https://pay.weixin.qq.com/public/apply4ec_sign/s?applymentId=2000002159341325&sign=1d5f6797645b5eeea52ea3e79dc424da"

        #第三方审核失败原因
        self.content = "实名认证必须本人手持身份证拍照，身份证信息不能反过来，禁止自拍（如不清楚可以查看示例图），提交的资料有错误"


    # 获取store_subject最后一条记录
    def get_store_subject_record(self):

        sql = "select * from store_subject ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_subject_id_result = self.cursor.fetchall()

            store_subject_id = store_subject_id_result[0][0]
            # print(store_subject_id)
            store_subject_id += 1
            # print("store_subject第二次的值:", store_subject_id)

        except:
            print("Error: 查询store_subject表失败")

        return store_subject_id


    # 获取store_subject_init最后一条记录
    def get_store_subject_init_record(self):

        sql = "select * from store_subject_init ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_subject_init_id_result = self.cursor.fetchall()

            store_subject_init_id = store_subject_init_id_result[0][0]
            # print(store_subject_init_id)
            store_subject_init_id += 1
            # print("store_subject_init第二次的值:", store_subject_init_id)

        except:
            print("Error: 查询store_subject表失败")

        return store_subject_init_id



    # 获取store_subject_id
    def get_store_subject_id(self):

        store_subject_record_id = self.get_store_subject_record()

        sql = "select *  from store_subject where store_id =" + str(userId) + " and deleted = 0;"

        try:
            self.cursor.execute(sql)
            store_subject_result = self.cursor.fetchall()
            # print(store_subject_result)


            if len(store_subject_result) == 0:
                print("store_subject表没有数据，需要新增数据")

                sql = "INSERT INTO store_subject(`id`, `store_id`, `store_type`, `current_status`, `content`, `deleted`, `subject_wechat_status`, `subject_alipay_status`, `create_time`, `update_time`) VALUES ("+ str(store_subject_record_id) +", " + str(userId) + ","+ str(merchant_type)+" , 2201, NULL, 0, 0, 0, '2020-12-18 18:31:27', '2020-12-18 19:46:46');"
                try:
                    self.cursor.execute(sql)
                    self.coon.commit()
                except:
                    self.coon.rollback()
                print("store_subject表记录新增完成")

                return store_subject_record_id

            else:
                print("store_subject表，已有记录")

                store_subject_id = store_subject_result[0][0]
                # print("store_subject_id:", store_subject_id)


        except:
            print("Error: 查询store_subject记录失败")

        return store_subject_id



    #获取store_subject_init_id
    def get_store_subject_init_id(self):

        store_subject_init_record_id = self.get_store_subject_init_record()
        store_subject_id = self.get_store_subject_id()
        # print(store_subject_id)

        sql = "select * from store_subject_init where store_id = " + str(userId) + " and deleted = 0;"
        try:
            self.cursor.execute(sql)
            store_subject_init_result = self.cursor.fetchall()
            # print(store_subject_init_result)


            if len(store_subject_init_result) == 0:
                print("store_subject_init表没有数据，需要新增数据")

                sql =  "INSERT INTO store_subject_init(`id`, `store_id`, `store_subject_id`, `legal_person_name`, `legal_person_card`, `legal_person_portrait`, `legal_person_national`, `legal_person_card_valid_time`, `alipay_province`, `alipay_city`, `alipay_area`, `alipay_address`, `mobile`, `email`, `business_license_type`, `business_license`, `business_license_valid_time`, `social_credit_code`, `merchant_name`, `alipay_type`, `alipay_account`, `operator_name`, `wechat_added`, `organization_number`, `organization_copy`, `organization_time`, `deleted`, `create_time`, `update_time`) VALUES ("+ str(store_subject_init_record_id)+", "+ str(userId) +", "+ str(store_subject_id)+", '花木兰', '410702197211052011', 'order/202011/20/43a430bd48a9200c3f9dec14ca05148e.jpg', 'order/202011/20/ea6c669ea21326396ed6fc737fd72910.jpg', '长期', NULL, NULL, NULL, NULL, 13250252197, '46756288@qq.com', 1, 'https://test-img1.ppwang.com/order/202011/20/80a7360d276d3400c95dcda074097704.jpg', '长期', '91440101MA9UXA8L0X', '百通优品汇', NULL, NULL, NULL, NULL, 'MA5TQ9201', 'https://test-img1.ppwang.com/order/202011/20/72f8c38c636328c28e031bf0bde404ab.jpg', '长期', 0, '2020-11-20 14:16:00', '2020-11-20 14:20:14');"
                try:
                    self.cursor.execute(sql)
                    self.coon.commit()
                except:
                    self.coon.rollback()
                print("store_subject_init表记录新增完成")

                return store_subject_init_record_id

            else:
                print("store_subject_init表，已有记录")

                store_subject_init_id = store_subject_init_result[0][0]
                # print("store_subject_init_id:", store_subject_init_id)

        except:
            print("Error: 查询store_subject_init表失败")

        return store_subject_init_id


    # 获取微信进件信息表最后一条记录ID
    def get_wechat_record(self):

        sql = "select * from store_subject_wechat ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_wechat_id_result = self.cursor.fetchall()

            store_subject_wechat_id = store_wechat_id_result[0][0]
            # print(store_subject_wechat_id)
            store_subject_wechat_id += 1
            # print("subject_wechat第二次的值:", store_subject_wechat_id)

        except:
            print("Error: 查询store_subject_wechat表失败")

        return store_subject_wechat_id


    # 查询支付宝进件信息表，获取最后一条记录ID
    def get_alipay_record(self):


        sql = "select * from store_subject_alipay ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_alipay_id_result = self.cursor.fetchall()

            store_subject_alipay_id = store_alipay_id_result[0][0]
            # print(store_subject_alipay_id)
            store_subject_alipay_id += 1
            # print("alipay_record第二次的值:", store_subject_alipay_id)

        except:
            print("Error: 查询支付宝进件信息表失败")

        return store_subject_alipay_id

    # 查询store_sign表，获取最后一条记录ID
    def get_store_sign(self):

        sql = "select * from store_sign ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_sign_id_result = self.cursor.fetchall()

            store_sign_id = store_sign_id_result[0][0]

            store_sign_id += 1

        except:
            print("Error: 查询store_sign表失败")

        return store_sign_id


    # 查询store_personal_real_name表，获取最后一条记录ID
    def get_store_personal_real_name(self):

        sql = "select * from store_personal_real_name ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_personal_real_name_result = self.cursor.fetchall()

            store_personal_real_name_id = store_personal_real_name_result[0][0]

            store_personal_real_name_id += 1


        except:
            print("Error: 查询store_personal_real_name表信息表失败")

        return store_personal_real_name_id


    # 查询store_personal_real_name表，获取最后一条记录ID
    def get_store_company_real_name(self):

        sql = "select * from store_company_real_name ORDER BY id desc LIMIT 0,1;"
        try:
            self.cursor.execute(sql)
            store_company_real_name_result = self.cursor.fetchall()

            store_company_real_name_id = store_company_real_name_result[0][0]

            store_company_real_name_id += 1


        except:
            print("Error: 查询store_company_real_name表信息表失败")

        return store_company_real_name_id


    # 查询微信表是否有店铺记录
    def query_wechat(self):

        store_subject_id = self.get_store_subject_id()
        store_subject_init_id = self.get_store_subject_init_id()

        store_subject_wechat_id = self.get_wechat_record()

        sql = "select * from store_subject_wechat where store_id = " + str(userId) + " and deleted = 0;"
        try:
            self.cursor.execute(sql)
            store_subject_wechat_result = self.cursor.fetchall()
            # print(store_subject_wechat_result)

            if len(store_subject_wechat_result) == 0:
                print("微信进件表没有数据，需要新增数据")

                sql = "INSERT INTO store_subject_wechat(`id`, `store_id`, `store_subject_id`, `store_subject_init_id`, `out_request_no`, `organization_type`, `business_license_copy`, `business_license_number`, `merchant_name`, `legal_person`, `id_doc_type`, `id_card_copy`, `id_card_national`, `id_card_name`, `id_card_number`, `id_card_valid_time`, `need_account_info`, `contact_type`, `contact_name`, `contact_id_card_number`, `mobile_phone`, `store_name`, `store_url`, `merchant_shortname`, `subject_status`, `content`, `organization_number`, `organization_copy`, `organization_time`, `legal_person_portrait`, `legal_person_national`, `business_license`, `organization_code`, `applyment_id`, `sub_mchid`, `deleted`, `create_time`, `update_time`) VALUES ('" + str(
                    store_subject_wechat_id) + "','" + str(userId) + "','" + str(store_subject_id) + "','" + str(
                    store_subject_init_id) + "','pp_964090_1608115567149', '2', '/storage/emulated/0/temp/img_3.png1603798684385.png', '91440101MA9UXA8L0X', '广州百通有限公司', '袁波', 'IDENTIFICATION_TYPE_MAINLAND_IDCARD', 'order/202011/03/5c820a99a6f46e85486dbe549ec24aee.jpg', 'order/202011/03/57ec9826ad939814ca11f8312e8f348d.jpg', '袁波', '410702197211052011', '2023-02-12', 'false', '65', '袁波', '410702197211052011', '13250252111', '10000店铺', 'https://test-wap.ppwang.com/store/964090.html?qd=wx', '10000店铺', 4, '原因', NULL, NULL, NULL, 'order/202011/03/5c820a99a6f46e85486dbe549ec24aee.jpg', 'order/202011/03/57ec9826ad939814ca11f8312e8f348d.jpg', '/storage/emulated/0/temp/img_3.png1603798684385.png', NULL, '2000002166046385', NULL, 0, '2020-12-16 18:46:14', '2020-12-17 15:37:40');"

                try:
                    self.cursor.execute(sql)
                    self.coon.commit()
                except:
                    self.coon.rollback()
                print("微信表记录新增完成")

            else:
                print("微信进件表，已经有进件记录")

        except:
            print("Error: 新增store_subject_wechat表记录失败")



    # 查询支付宝表是否有店铺记录
    def query_alipay(self):

        store_subject_id = self.get_store_subject_id()
        store_subject_init_id = self.get_store_subject_init_id()
        store_subject_alipay_id = self.get_alipay_record()

        sql = "select * from store_subject_alipay where store_id = " + str(userId) + " and deleted = 0;"
        try:
            self.cursor.execute(sql)
            store_subject_alipay_result = self.cursor.fetchall()
            # print(store_subject_alipay_result)

            if len(store_subject_alipay_result) == 0:
                print("支付宝进件表没有数据，需要新增数据")

                sql = "INSERT INTO store_subject_alipay(`id`, `store_id`, `store_subject_id`, `store_subject_init_id`, `external_id`, `name`, `alias_name`, `merchant_type`, `mcc`, `cert_type`, `cert_no`, `legal_name`, `legal_cert_no`, `province_code`, `city_code`, `district_code`, `address`, `cert_name`, `service_phone`, `contact_infos_name`, `contact_infos_tag`, `contact_infos_type`, `contack_infos_mobile`, `service`, `sign_time_with_isv`, `alipay_logon_id`, `binding_alipay_logon_id`, `site_type`, `site_name`, `subject_status`, `content`, `legal_person_portrait`, `legal_person_national`, `business_license`, `order_id`, `smid`, `deleted`, `create_time`, `update_time`) VALUES ('" + str(
                    store_subject_alipay_id) + "','" + str(userId) + "','" + str(store_subject_id) + "','" + str(
                    store_subject_init_id) + "','pp_10000_1602818043045', '洪小明', '" + str(userId) + "', '" + str(
                    merchant_type) + "', '5699', '2011', '799874674978', '洪小明', '6844789749878678', '440000', '440100', '440111', '添加何江区网商路699号', '', '', '洪小明', '02', 'LEGAL_PERSON', '13250252217', 'app支付', '2020-10-16', '1684847687799@qq.com', '1684847687799@qq.com', '02', '批批网', 4, '', '', '', '', '2020101600502000000066580485', '2088010048202378', 0, '2020-10-16 11:14:03', '2020-12-17 15:09:15');"
                try:
                    self.cursor.execute(sql)
                    self.coon.commit()
                except:
                    self.coon.rollback()
                print("支付宝进件表记录新增完成")

            else:
                print("支付宝进件表已有记录")

        except:
            print("Error: 查询 store_subject_alipay失败")



    #更改微信进件表
    def update_wechat(self,subject_status):
        userId = self.userId
        sub_mchid = self.time01

        self.query_wechat()

        if subject_status == 2:
            sql = "update store_subject_wechat set subject_status = " + str(subject_status) + ",sub_mchid = " + str(
                sub_mchid) + ", content = ' " + str(self.wechat_content) + " '  where store_id = " + str(userId) + " and deleted = 0;"
            # print(sql)

        elif subject_status == 3:
            sql = "update store_subject_wechat set subject_status = " + str(subject_status) + ",sub_mchid = " + str(
                sub_mchid) + ", content = ' " + str(self.content) + " '  where store_id = " + str(userId) + " and deleted = 0;"
            # print(sql)

        else:
            sql = "update store_subject_wechat set subject_status = " + str(subject_status) + ",sub_mchid = " + str(
                sub_mchid) + "  where store_id = " + str(userId) + " and deleted = 0;"
            # print(sql)

        # print(self.coon)
        # print(type(self.coon))
        # print(self.cursor)
        # print(type(self.cursor))

        try:
            self.cursor.execute(sql)
            self.coon.commit()
        except:
            self.coon.rollback()
            print("Error: 修改subject_wechat表失败")

        print("更新微信进件表成功")



    #更新支付宝进件表
    def update_alipay(self,subject_status):

        self.query_alipay()

        if subject_status == 3:

            sql = "update store_subject_alipay set subject_status = " + str(subject_status) + ", content = '" + str(self.content) + "'  where store_id = " + str(userId) + " and deleted = 0;"
            # print(sql)

        else:
            sql = "update store_subject_alipay set subject_status = " + str(subject_status) + " where store_id = " + str(userId) + " and deleted = 0;"
            # print(sql)

        try:
            self.cursor.execute(sql)
            self.coon.commit()
        except:
            self.coon.rollback()
            print("Error: 修改subject_alipay表失败")

        print("更新支付宝进件表成功")


    #更新store_subject表进件状态
    def update_store_subject(self,current_status):
        # print(current_status)
        sql = "update store_subject set current_status = " + str(current_status) + "  where store_id = " + str(userId) + " and deleted = 0;"
        # print(sql)

        try:
            self.cursor.execute(sql)
            self.coon.commit()
        except:
            self.coon.rollback()
            print("Error: 修改store_subject表失败")



    #更新java-store表
    def update_store(self,current_status):

        sql = "update store set current_status = " + str(current_status)  + "  where store_id = " + str(
            userId)
        # print(sql)

        try:
            self.cursor.execute(sql)
            self.coon.commit()
        except:
            self.coon.rollback()
            print("Error: 修改java_store表失败")




    # 第三方记录表
    def update_store_subject_log(self):

        store_subject_id = self.get_store_subject_id()
        # 获取第三方进件日志表的最后一条记录
        sql = "select * from store_subject_log ORDER BY id desc LIMIT 0,1;"

        try:
            self.cursor.execute(sql)
            store_subject_log_id_result = self.cursor.fetchall()
            store_subject_log_id_result_id = store_subject_log_id_result[0][0]
            # print(store_subject_log_id_result_id)
            store_subject_log_id_result_id += 1
            # print("第三方日志表第二次的值:", store_subject_log_id_result_id)

        except:
            print("Error: 查询store_subject_log失败")

        # 第三方进件日志表，添加2301记录
        sql = "INSERT INTO store_subject_log(`id`, `store_id`, `store_subject_id`, `status`, `content`, `create_time`, `update_time`) VALUES ('" + str(
            store_subject_log_id_result_id) + " ', '" + str(userId) + "','" + str(
            store_subject_id) + "', 2301, '进件状态为进件完成', '2020-09-24 18:21:37', '2020-12-21 11:54:44');"
        try:
            self.cursor.execute(sql)
            self.coon.commit()
        except:
            self.coon.rollback()




    # 新增签约记录
    def add_store_sign(self):

        store_sign_id = self.get_store_sign()
        time = self.time01
        # 判断该id是否有签约记录
        sql = "select * from store_sign where store_id = " + str(userId)
        try:
            self.cursor.execute(sql)
            store_sign_result = self.cursor.fetchall()
            print(store_sign_result)

            if len(store_sign_result) == 0:
                print("store_sign表没有数据，需要新增数据")

                sql = "INSERT INTO `store_sign`(`id`, `store_id`, `sign_type`, `valid`, `status`, `sign_time`, `src_pdf_file`, `seal_data`, `sign_service_id`, `create_time`, `update_time`) VALUES (  "+ str(store_sign_id) +" ," + str(userId) + ", 1, 0, 1, 1610708980791, 'sign/store/965044/202101/15/TjMRhiT54M0gsnvw5VNiNW7GSjtKVSjw.pdf', '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', '1350037425384149000', '2021-01-15 19:07:24', '2021-01-15 19:11:16');"
                try:
                    self.cursor.execute(sql)
                    self.coon.commit()
                except:
                    self.coon.rollback()
                print("store_sign表记录新增完成")
            else:
                print("store_sign表，已经有进件记录")

        except:
            print("Error: 查询store_subject_wechat表失败")



    # 新增实名认证记录
    def add_real_name(self,merchant_type):

        personal_name = '洪泽佳'
        id_card = '440582199704224876'
        Real_name_mobile = '13250252197'
        Real_name_status = 2  # 1认证中 2认证成功 3认证失败
        company_name = 'esigntest批批网实名测试企业'
        social_credit_code = '912388479846526897'


        # 判断是小微，个体企业  5小微，6个体，7企业
        if int(merchant_type) == 5:
            # 获取userId在store_personal_real_name表是否存在记录
            sql = "select * from store_personal_real_name where store_id =" + str(userId)
            try:
                self.cursor.execute(sql)
                store_personal_real_name_result = self.cursor.fetchall()
                print(store_personal_real_name_result)

                if len(store_personal_real_name_result) == 0:
                    print("store_personal_real_name表没有数据，需要新增数据")
                    # 获取小微类型实名认证表最后一条数据
                    sql = "select * from store_personal_real_name ORDER BY id desc LIMIT 0,1;"

                    try:
                        self.cursor.execute(sql)
                        store_personal_real_name_result = self.cursor.fetchall()
                        store_personal_real_name_result_id = store_personal_real_name_result[0][0]
                        store_personal_real_name_result_id += 1
                    except:
                        print("Error: 查询store_personal_real_name失败")

                    # 新增小微类型实名认证记录
                    sql = "INSERT INTO `store_personal_real_name`(`id`, `store_id`, `name`, `id_card`, `mobile`, `certification_time`, `account_id`, `flow_id`, `short_link`, `expiration_time`, `verifycode`, `seal_data`, `status`, `create_time`, `update_time`) VALUES (" + str(store_personal_real_name_result_id) +", "+ str(userId) +",' " +str(personal_name) +" ','"+ str(id_card) +"','"+ str(Real_name_mobile)+"', 1610707439343, '4E71E32CF517445D8F4E6D7D4E256A6E', '1610133189748148105', 'https://smlt.tsign.cn/m8ClyUfX2QLN', 1613213016885, '67c9bbbd4abd44989de7427b964ccb82', NULL, "+ str(Real_name_status)+", '2021-01-15 18:43:36', '2021-01-15 18:43:36');"
                    try:
                        self.cursor.execute(sql)
                        self.coon.commit()
                    except:
                        self.coon.rollback()
                    print("新增小微类型实名认证记录成功")

                else:
                    print("store_personal_real_name表已有记录，不需要新增")
            except:
                print("Error: 查询store_personal_real_name表失败")


        else:
            # 获取userId在store_company_real_name表是否存在记录
            sql = "select * from store_company_real_name where store_id =" + str(userId)
            try:
                self.cursor.execute(sql)
                store_company_real_name_result = self.cursor.fetchall()
                print(store_company_real_name_result)

                if len(store_company_real_name_result) == 0:
                    print("store_company_real_name表没有数据，需要新增数据")
                    # 获取个体企业实名认证表最后一条数据
                    sql = "select * from store_company_real_name ORDER BY id desc LIMIT 0,1;"

                    try:
                        self.cursor.execute(sql)
                        store_company_real_name_result = self.cursor.fetchall()
                        store_company_real_name_result_id = store_company_real_name_result[0][0]
                        store_company_real_name_result_id += 1

                    except:
                        print("Error: 查询store_company_real_name失败")

                    # 新增个体企业类型实名认证记录
                    sql = "INSERT INTO `store_company_real_name`(`id`, `store_id`, `company_name`, `social_credit_code`, `legal_person_name`, `legal_person_card`, `certification_time`, `account_id`, `flow_id`, `short_link`, `expiration_time`, `verifycode`, `seal_data`, `status`, `create_time`, `update_time`) VALUES ("+ str(store_company_real_name_result_id) +", "+ str(userId)+", '"+ str(company_name)+"', '"+ str(social_credit_code) +"', '"+ str(personal_name) +"', '"+ str(id_card) +"', 1610708951447, '3EEB2C6E15344BD3BA0E10369A751115', '1610157822392223517', 'https://smlt.tsign.cn/sPRYuyq9UXSx', 1613214485156, 'ac0a956fdf3b854ea7200715d9dac709', 'iVBORw0KGgoAAAANSUhEUgAAAcQAAAHECAYAAACnX1ofAAAdJ0lEQVR42u3dW7LbyLFAUc1/bJ6T76cVfVs6QCGrKh9rR/DDbYki87WRIAn8+gXgKP/99es/Tx4iBQAoLbKMD9kDAIyRHlECAEiPLAEAxEeWAADyI0gAIEAPggQAAvQgSAAgQA+CBAAS9CBIACBAD4IEABL0IEYAIMFpQ16syBEAERrI8kCOAEjQsJUv+QJgqBqiciqnAAxMQ1Lu5R2AYWgQqgk1AcDAM+zUi1oBYLAZaupIDQEwwAwv9aW2ABhUhpSaU3MADCUDCWoRwPjhI/ogRgBjh43Iw4EbACIE1DCAiUNE1KGuAYwdGCIOYgRAhIDaBzBxGIg29IJeAEYPAJGG3tAbgGYH9IpeATQ3oHf0DaChAX2kjwANDOgrPQUQIaDP9BigSQE9p+eAxk0puv1qRRT0IKAJNaKakVdiBDSexsP/6kYkavanyAKaDRtqRzQctAIaTIOpITl3AAtoKk2ljv6ef3VRp4dFFRpJI4EQ9bJ+hubRPNgvxCd1opYc5AIaBm1l+M8/R4gOeIFWjSKiWBXikz8nsg5+AY0BQlRnDoQBzYDKNfamDr+KEw6KATJEeSFGiBNmAqDoMUaIoms+AIodbYX4pn4zvDezwqyAAlfgeF1zkULM9P7MDDMDQwtbNEGIM4RIilDQihkbau/kn8v03swRcwSO7IA/SuP3//2mzgiRFAGFizZC/NP/rvQN08l9YrZAwQIHhPimrgmxx5zRJSBDtK+5f5Pdkz/zRq6ZZTihh8waKE4gqO6qC/HJn5N/cweKEgPr7209VhPiyheAzCAzCAoRCYZyxk1qghCn9pVZBAUIQlyUQqWfXKy+VlI0k6DwQIhHL+q9Ox477sjRtf/MJpQrOFEkxExCjHqubNvhrddMiiBCRTayBqpKO0qIu2Ox4+IBE/rRvILiAiF+FOJPX8Q5KZddnx1O6UlzC4oKhPhRiE+vZhMRj9M3L57Wm+YX0hWUKBLijdf4ViBP/1u0EJ88/9MtlhBJEWQIQvwkxKf/7afeiIrpT9JekeHKnzfPzDMoHjyshw5CfCulyIODN33003/zG0VzDYoGhBguxBMy/LoxftkO1bL5BsWCDXWR9TX+2///kxhWhHijB22H5hwUCRLWRRaBPpHYm03p6ynKnT34duPTo/HzTgQVh+JQF2kPmp4KLEqIp97D6kGJ7dDcg6LA0LqI/tzty0YWveH+LSe2Q/MPiTYAUZxdBxXew9tt6cZ73n1VGr1KiiBDbJJJFSFGSCfLNUvfbnx6lRRBhliohwjhZJZhhBBPvH7bISlC4rFRZqfFk/X1ZLzE2YTtsNLMMBvJUMIJsZwQV2o043bVfTusODfMSDKU6OI5nSLEqJ8gZNiuol776melJ3NlVkKCcTSnnYX4tU4z3jMwYuP78k1aMtw3L81MMgQhlhdipc8OV79Jm+m9mZuQVGzL5TQhvpVAls/fon4T+eV3lqfyZH6iRUJFr2b+bryWG3FYFcvKNnZShn97f29vEXXy/XWdJ6RIhpKoAVNtiZFXn8kmxNWLer89MDh9cfKTMSVFSOCAnK3mtZsQ/3Sqr5oQIze+N6eNd+cs6qIIFgyQIZaO3icKcWXQZviG6dcbEUfJ6MSNjW9u36QISWuUr+yS6izEqPcU0XNRQtzd6xPvvmG+ShYSbYY3RZX58m23hRjVbztlmKF2SRGShG0yPDloqgvxxqa+86a+T794k0WGXaRo1koQEsvw9+e9VWdZY1hJiF9PQd46S5D1AM7MNWAlZ7AQb9YaIX77jeDX7bCSDEnR3JUUbBkqhJjjot5fvzH6ZTu89YWqk3k0fyEZhEiIHwbpyZ9cRN+YOFMOfrogwGQpmsESAUJsJcSoz8RO/fu3r070RoYrv6s1iyEJw/Pm9e8V4g3BVL8B8JPPRVe25gzvzTwmQ8EnFEI8tJ3sOl2b4RqyT2Q38WcZ5rKgIzB/pBgrmx1fvJm6HZ6S4dPnyNgvZrOAY6AUI177ib+743PGCdvhm1tU/VQXO84CZO4VM1qwsSGPUXnPegm3qL/7dcvYLcRq2+HqnSt21V7FmWZOCzIO5TKDHCsIcfVGvF+FWHk7fHPh8ZPSqjjXzGoBxhApVhfil8uqdd0O396F40kt7JaiBcbwFFh5vS7FakL823+PFGLV7XD1M9mvP8v4/c92kqG57UgDpHjkNkBfvlATcZ3Rbtvh6j0an37u/fTf7yZDUhRQFBPjLSHe+Ibp041x0nb45U4cK581fpWhGW5ICmSi+HesoR3Pm02ITz9PPCHELNthFhk+3UjNcQhk4nh3eV+nt8QTN5d9834jhHhiO9x5FZ3oz/CivgHcaaaZ5QIo3gXe30nRRnyr84sQv251HbbDUzJcrYGuM808F7zWsZ56hZnI+H193gxCrLQd7pbh0wOZJzdS7jjTzHWBGyHDKvG/cTWRyC/ffPk25Kp0oj7ryrgdRtfJl6vYTJlnZruApY9zZE4mCvFNjHaekl09LbsqxMrb4Y4aIUPzXcCay3D30L9dXx232mxC3CHzkzJc3Q5XTltPmGVmvECVl2EXKU4T4tdYfP3Jxuq/s+t09kpNr/RV5Glrs37grBegGkJ8ky9CvPOaI7+48/QLIKuv/eQ1Z3fV8epzTJ5l5r0AtZFh5JH1356bDL8JMbrnVl7Pm+c4+Vu/iNfwRermmJkvMM2EuOtU16mrk3TNW+Q3WSN//vHTqcRdMnzzJZbI7ZAMzX2BabJl3Hru21+syJy73dv1zd9SRm2Hb2X4tUZOX6nI7G8eNwHpJcRdNTFVhl8Ed6JHV/t6tYZWZbjjMz0yvOcAwVBIKYV48jTsyXsO4ud87JDhqhBPyvDGNWwJcYAHBKK2EE/fmmfXkTv2bkJfr4azKsMTFzPYdQk4NUaIZJhoqD19vmwHS+rl/sHUrp8evPmCzA5Z7b5ykBob3N8GXE0hnswFEdY8s7DzIgJv6yPitUZeZF1FWZC8+SZCPC1T9ZGnbnbkeUUsP/39aHFH/eheffKCN10g5jdkuPrvqofzNbPzoOfLFhl5cBf9uWSGeq38jWpCJMTUQrz98we10HOjXN0Od5/6//KN1Zuzq0ufjPKDz4Tyxf2EDKOEKJM9tsrV06WRMnwrs+ifkOzsbQuTN4tgKWa6Woxa6F+Lb2fFaaFkkuGJWXmr38YsTbbDOkLMdlUbdTCvFm/IcFWaJy+NeGJe3p69hEiGKQfR7n9fRtTijbkQ+fOMk5vrib7N0J/tlyfbYb08nPj3ZUQ9npwJ0RfwvrkZ7tjsMvUnIRqWaXJx6t+WDaxsQ6c2n1syfHo2J3K7y9abbZco2yEhEiK+1mfEc0bVa+azKREXws/Sm4RoULaWohyjynB++uP8bLW8+56OlilviBRthyDDdPL46VviN7ZxC5XtsK0Qb3zFHeoxo5SryPDt/5+9L9ssVbZDUiRDdBBzVhlGXBS9Ql+OFaJ2zJ0nQsSEfniyMZ7c9la36RsXO7BcEWL500e78iTH6HaweLvXV69FXH3mlvYJGZ49YsyWMzlGRyHePvj9cmGBjgcnhGg7THlqQn5BhmdluPu3iaRIhik2u6qXTSJDTJThiZtm377BNyES4pWjyupXiSBCTJPh7ivDrN7H1JZIiGnfd+VTG2QIMowT4k4Z3rilG7+Q4fL7rybDyPcHdDu78/U2Um9uSPzlfo2dtkRCHCBFUgH292TE1rbav19kuEOyk6TohRZIWLcjN6BCP0bL8EkPv5mBX7fNDmeiWixetkMHB0CFXoyW4d+ku/uqTyvPXX3mEOKAxBlbQJ6zNhFbYuS/EzlLOsyd9L4hw5pSJGPow5ge+NsdMrK9bkK0HZZJ3o3XZWTmqxlRqCPD6J46fQeaivOZEAdJcWeM5IQQ9d7+S7Jlfr0dZkBK75DhvjjtjpXc5K4Vkag5/COvYLPrlC4hEmJZKZ7eFo3QPHUiGjXr+8sP/E9+I7V6rZUXouZ8ftPO06d45IgQxfHcv51FhL5cYztM16A3YyhPeRtcRL7H83YuT4nwqYw71RghNkhexm1bnvI2uKjU3bb97GqQFMlwT2PeiqtcESIpnp+RMtRAiLbD2O0wgxjlKmdji0y9MyDmISEqgEAZ3pCiXOVtbNHJfcBhDtaSYr8XMESIJ+MtX4RoeMb8VEIeh22JCqHfkZB81R7S2DtAvwxduWy8JToyqpX8lecT4Xz5FKUaYnTASYgaufBpAvkiRMTJ8cm/IdqEiCJHuSKaM38idT8vX0Unn/kXhPz/KI6JURRz5020cufvzZ8XuQZboiHbV4qiR4g4J0T5HChEKRpSGJAnOfzP27/zt1oQ2QILmwbuVyCiNKiBsTV/kbkX3eT9pHkBQsR+IYpsgaVN8wJ3Zain+gjxTzUgqk2FKDVAvBD1Vt78nRYqLi5umhYgRMRud/JaUIiaFsghQ73VR4a/P5eo3usvQgQKC1F/9REiBghRSgBCnJQ7kq7dX4QIFJWhHiPElfrSYwGx0awAISK/DC0xB96/Zt2TCONFfZBij7y9+bvVa65KvaYRoqYx3HBmMIlone0w++eN04X4+PVp0rrDztBUI7gvw4xSPC3HCu+LEJsXlcHZv05EtYYM//R8Wd7Xzpqt0m/3LGvIHRmGhmb/OhHZHOL4WgtV3tOTv5OlPq8LUcPk+dDa0CRE5JPhrs3z1L/55mC8Ws8R4qUjva4fZONOzkV3b86yS+rkv1Op5gix6BGkYUmGcqw+duQ2+rk7C/HH96Uxnwc86xA1bggR/erk63NlnHnpt0SNmac4DEtClGe18uYLLbu3zlFC1JTvAl2tcdBHhnI9s0Zuv15C1JBphPgkX0YNIWJGTRAiIRLiD6/L6JkjRPnul/8vz2HGECIhFjyCMwwJUc6ffS6YSZCEqBlLbYhGEyEi//b3ZSO7WStdhfjH96QZa0rRcJwrRHnvIcCVvj5dO+M+R9SIdbdEzJShGsyT15sHuqcvDZm97j73kEZcD7SRAUKcdyC8O/4RV5eZWoPHhag5xAM5hKj+7uc7+/NPqz1CPFj0BhIyyVD93c979efvVneEmCCwxoPBSIiEWOn5v9R1t34kxBNHGlAnpEiIRYWY/fVsm92ab9YpBfSSoVq7n/vpAiJEgTW0iknDo+bDlkiKx4RoqN8d5lMaxWD36HgQSYiEKLAJBkDFfBjwHt3mDCES4sjA3hruNz67IEYPMsz1OaKPXgix1NGfwUGKHjPrecfrN4cJsV2hGyCk6DHn4O5UL9AdIY5M0pRcEAIZThOib6oTIoJFIBYeRJhfiOJFiHDahBg9xtTvv90JQ1wIEYcSq5g9yLB2vZpuCaUoiTUTrJg9iJAAQYgS7HqyHmSYviZNLEIEIZKix8hT+yYUIeJCghW3BxkChCjBw3NANGSoz0GI+DHRCt2DCPvUtmgQIukEJFfBe5BhjjokQ0IkxCSDX9F7kGHN+sv0fghR4f/KEgODihSJcGbdOdt0WIiKnxANKA+19a6+Ttebs0uE6JTpLxcFJkUizFpblQ5wXUCBEI8J8dbR3Zu/51SWBxnmkWJ07WY961VtoSDERancPrL7+vqJ0YMM98yGFIM9Ya/ZEBseDZ4eKr7GTYpEWKeuMtd2hQ2WEIcO05NNZ6gRIxn22RZvSrJa7RBiMylGF7HhRXB6/VxdZTrdeOqzyEy1Q4jFhujOJrMlkiIZ1hHjjTy6byUhhgd1V6NExt+gI0Y9nnteqANCbH8q5MtnDoRIigZg79rqXpu/v5cSQlz+S0OLesfzEiIxkqH6Ov154YT6IsSNAd313IRIimSoxrLkqlN9ESIhkiIp6uPh9dZxXhJiooDeeG5CJEYynFFfmWov88wkxMZC/On5d5wyNQwJUQ3kqadqdUmIhEiIBhghIrR2KtatDVEzHTllSoiESIhz6qPae6k8ZwiRENMftZEhKU6sj20DPNHcI0RCPCbDiFtIGWeEqBZynxqtnP/y1zIlxDsyIURCJERUrUFCJMTQrySvCvHr/RSNGjJUD+p1Qm0tv15NdEYqT2Oa6dZRBgwhot6pwkz1ToiDhuTtgtt9ulWuCRHxMuyQC0J0CyjDT45JEf9aM7fqrUMsCHH4wFw9yjL0CJEQc9ZKxXrTz4R4fWiuPCchEqKhmLc2ptYcIWqgXzu/rhwlUPkiQzWSX4iVa9aGqHm2iyn6CzuyRIjqJG+/V613p0w10FLwq3yeIX+EiDx1kvk9jziA0UAw5EgR9WtGdggRIESDVD2pAUIECNEwVItq6EscCREGEBHqa7XcrrY+vzaNA0PEQ0Ws1Yg+yBUfQgSKCjHja8H7WhGXBtcxJcUexSgStWWY5TWpipiaEae7MSBETSofhYSYWdQqI65uRIsQQYiEGNA3hDhg6IIQQYgTZdj5daojMa6cE0IkRfEqIhlSrFdPT/Mmcok3d01DiJomr1wIMV+9/CTFN7kT5eJClMScRSAaOcTitc8T45M4njqbIEcBta5xbIkaJr9QSDFX/TzdFHdujfJHiHBkmE4m3gcpvu3JiHzIHSHil/shZpGI96Pnvkoq6jes8kKIki8v1wTifamj6M3tbX7kbYO/NEyPhIvUGXF0l72KeR7vqD/7NbdyQoiSLDejZTjpPVbcEqO2ODlLLkRNk3e4ieA+WXiv+FucM+RYPoJqW8M4whfb+vFUQzlifPM1yAch2gZ/+bbZdBk605AvvqdfgzwQoiFNiKTg/V+L7a2tUY42ekvD9NhU5OZ73MVADb0V4q7NMTon0w/68jy5gXz01kFiTwIOeM/E9EvMV8W7qw4IkRDLboMnGsiRIynie69l+iikSw1sr2fNUlOCtsRvOREXsTnVa2/jvntGVD6Tsv01O4KsLUJCJMNdgxnxvZahTiddutAR5CAJIub0lDiJ0+mDz515iLgt1eizHYb7HiEaHXlyJELilfVsws7vFHTK5bEZbNA7JWe4i5sh2uejDz8n+vDebT+GbsfciMzc2O2+qXL2b4sT4sf3Pulaj1lObSDnKScx7BPDW2K8+YP8rj1AiAlPCxm6PQ920D+WkTNt52UYXagjJt6EuLEBJhyBVW8U0RDPN32782D5y28Po0RtO6xk4CRBNDR6DTmI60rP7ppxt067Ttvut7iJEA3iak0iCuIbeQC7e9a5rnGhZY0Qe2yJNljgey+cutxi1JyyHV4WYvbgn/qa9IT3ClQeptG9dXPoE+KhOTfxc8TqQvQbUuBZb2QRbGRfTzgrdHW+TRJipQaJkiEpYqIMp9z/b7oMCXHhfUU/bzUZkiKmyPBPvdJdEITY5QUgJE8nTyMB2Q98u82tKfP5uosIsa8MT2zMQIbeeNo3k7Yo2yEpjhNixNE00Gk7fNI7XQ4CJl1pjBDxyw95ge8Hd11m2MrVd9wMuPqLwTYhkiI69sQUKX69Ak/W959uKbMl1hLiyaNroEtPdDmlGD3bCZEQxwrRlojq/fB146v+G+udM368DFdfmPasL0R5RMVe2LUtZj7A3Hnj85tzoI0QDVNCBDJsR7eluLuXdtwyqtJ1mQkRW6Uoh+giwx1SXL1bRqbZXGF2p3/dhHguxlmEKI/o0i83T6Hu7KUdQvRlGltiuiOiLEKUR1TeDnduixmEGD27s5/9SvO6CfF8bLMIUU7RQYY7pPimTzNLpsI8TPf6STGPDHdJUU7RWYY3pKh3CFEBHDpiOy1EWUOWfrl5MLoqRVmM94wXS4ZbhCiXqNYzN5/3TZ/ooaZLly1xfwxvDQo5RLWeuS3bp69LLxGiAji0he3cNOUPHXsmqo+evi791NgtpLgvbjeEKGeY1jOR2+Lb06Z6ixAVQDEhyhay9cvf/sxtKb59Ttlt5BRCPNv0uxtYrtCxJ7JJUZ81dgop5hdipatpABmlsfNnTbJNiNjUJGIOfbDn9URui/qzsUtIkRCBblvhn3pyhxRlnxDRTIjyje4yjOwzPdLYIaQYf3qmghDlHDvqp8LBabQU1QEhIliKN3+jJfeIrKEqZ2t8s5s7SDFJMz6NfyYZyr36fnIll1s1cus+iYRIiIZiUJPcvqzV7iNp9JdhBilG3/lipS/IsJEzSPG8FG9f0ur038eses4wu74+jy2REAnxUjxPxNfVOrBz67pdH6elOLEfRnzU4vOkXFKs9J5kuv9WOEkSb3tyWj+M8QQhiikpqtcnP2rvvjWt3Dx4Qi+MWpxsiXdjW/m9yHBfGe6SYubaedunU/phnB8IkUwIkQhP/Nns9eOb2BYmWyJIkQyPC7FD/RBi05lAiLXzRojYmcMoKXasn649MXpRsiXa2AhxVq3svHTZLSnemF1d+2K8DwixR76q/1voLcXMlyu0JVqQBKFprggR0RvNri3x1CULd822Tr3BA4LRNk+EiCc53bUNvdkSs0px2rdOOUAwWuVoxykcee9dTzs3zBtS3CHE1fsumv+kiEv5WT2Sj/j3MLcGV//srrqKvqj9as91uAAHIQpK6e0w6tQYIeLWlhh1QfoMZ2eq9Im5Lzhtt8OoI2b5xpu6yCTFbHPSvCdFJBHi6rYoz/hpA/tyL9Avgq04L816QsTlI/PVbVGecfpMxYRvaprzpIiETfb2av5yjCdbIinGHsCa8Q2CZWDWaK6Vz3XkFv8UIinWFKLZLmiEGJBf2cBPB1JfhNhFipl7yFwXPEIMyLFM4MSWWGHDMtMFT/CS5eF0nmUBT7fEqJ8DqUPzXBCxPEDIELeE+Lf//qWe1aNZLpA4NhTkEDuESIpmuGAKZqktUf5QRYq7z5SY3/pfUAcLUe6wQ4g//X9fNz81anaXDqrAnhlCZIiMQtxxvV21SoaCi89SlC90kWLkAaJ5bQaQYpP4kyGyHpyRIhkKtECn2RTlB7cPznYLkRQtLqSIz3mQE3TZEv/59+XELHAEIg9ygfRb4gkpyod5IPDyIf5IKcQnm2SUEOXCTJYAOFpGijkQITqz4uw8FjlSBHBxSyRFc1gyJAIYuyWu/jnzggwlBIAt0awweyUGQEchkmKOuStypAiAFM1bMZQgAHmE+M8/T4hmrURJFNC6922JZqzGkDBA7wff39Cs+H65RhVKigCSbon//DuESIaSJ3mALZEULRkSKImALZEUyVAiJRMgxP/393Y8vxkKCQWQot9tiWYnfsXcyFYUgd5CJEUyJEUJBsb0PCmSISQZ0PsveniyEM1JUpRsYEj/R26J3WaE+UiKkg5gSYqdZoS5qNglH8CjOfF2lkyah2YiKSoAwJb4x79HhiBFAKRoBkJBAJgwH8w+s48UFQZgNvh5hZlHiAoEMBvq97tZB4UCIHxWmHEgRQUDwGyDwlE4AMw0KCAFBMAsg0JSTADIEApKUQEwu6CwFBYAMwtQYABGzSpRBCkCIEOAFAGYS4DiA2AeAYoQgDkEKEgAZg+gMAGYOYACBTB0zpg1UKwAzBfzBYoWgLlirkDxAjBLgPqFrJgBM8T8gIJW1IDZYW5AYStuwLwwL6DQFTpgRpgRUPAKHjAbzAYofIUPmAfmATSCRgDMADMAGkJTAPpe30NzaA5Ar+t1aBbNAuhv/Q1oGkBP62lgewNpIkAfAxpKQwF6F9BYGgvQr4Am02iAHgU0naYD9CWg+TQfoBcBzagZgYq9p/8AzQnoNQD5G1WzQn/pLUDjal7oJ/0EaGSNDP2jfwBNrbGhZ/QLoMk1OvSIHgE0vKaHntATgCFgCEAP6AHAUDAYoObVPGBIGBRQ3+obMDgMDqhl9QzAMIG6VbsADBioU3UKIOvAMXSgJgEYQoYQEtWfGgSQcjAZTupMnQEwsAwuNaWeABhiBpraUTcADDeDTo2oDwAGnwGoDtQAAEPRgJRjeQZgcBqi8id/AAxWg1Zu5AYAOXZ7iDERAoDB7UGCAECMHiQIAATpQYIAQJAeBAgA5OhBgABAkB4ECAAE6UGAAECQHgQIAERJfAAAsiQ+AABRkh4AAJkFKvJADP8HDM69CwypaAUAAAAASUVORK5CYII=', "+ str(Real_name_status) +", '2021-01-15 19:08:05', '2021-01-15 19:08:05');"
                    try:
                        self.cursor.execute(sql)
                        self.coon.commit()
                    except:
                        self.coon.rollback()
                    print("新增个体企业类型实名认证记录成功")

                else:
                    print("store_company_real_name已有记录")
            except:
                print("Error: 查询store_company_real_name表失败")



    def update_store_subject_status(self,sb_status):

        sb_status = int(sb_status)

        if sb_status == 1:
            #1微信认证中，支付宝认证失败

            self.update_wechat(1)

            self.update_alipay(3)

            self.update_store_subject(2201)

            self.update_store(201)



        elif sb_status == 2:
            #2微信认证中，支付宝待签约
            self.update_wechat(1)

            self.update_alipay(2)

            self.update_store_subject(2201)

            self.update_store(201)



        elif sb_status == 3:
            # 3微信认证中，支付宝认证通过
            self.update_wechat(1)

            self.update_alipay(4)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 4:
            # 4支付宝认证中，微信认证失败
            self.update_wechat(3)

            self.update_alipay(1)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 5:
            # 5支付宝认证中，微信待签约
            self.update_wechat(2)

            self.update_alipay(1)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 6:
            # 6支付宝认证中，微信认证通过
            self.update_wechat(4)

            self.update_alipay(1)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 7:
            # 7微信待签约，支付宝认证失败
            self.update_wechat(2)

            self.update_alipay(3)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 8:
            # 8微信待签约，支付宝认证通过
            self.update_wechat(2)

            self.update_alipay(4)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 9:
            # 9支付宝待签约，微信认证失败
            self.update_wechat(3)

            self.update_alipay(2)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 10:
            # 10支付宝待签约，微信认证通过
            self.update_wechat(4)

            self.update_alipay(2)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 11:
            # 11双方待签约
            self.update_wechat(2)

            self.update_alipay(2)

            self.update_store_subject(2201)

            self.update_store(201)


        elif sb_status == 12:
            # 12微信认证失败，支付宝认证通过
            self.update_wechat(3)

            self.update_alipay(4)

            self.update_store_subject(2203)

            self.update_store(201)


        elif sb_status == 13:
            # 13支付宝认证失败，微信认证通过
            self.update_wechat(4)

            self.update_alipay(3)

            self.update_store_subject(2203)

            self.update_store(201)


        elif sb_status == 14:
            # 14双方都认证失败
            self.update_wechat(3)

            self.update_alipay(3)

            self.update_store_subject(2203)

            self.update_store(201)

        elif sb_status == 15:
            # 15老店进件完成
            self.update_wechat(4)

            self.update_alipay(4)

            self.update_store_subject(2301)

            self.update_store(301)

            self.update_store_subject_log()


        elif sb_status == 16:
            # 16新店进件完成
            self.update_wechat(4)

            self.update_alipay(4)

            self.update_store_subject(2301)

            self.update_store(301)

            self.update_store_subject_log()

        elif sb_status == 17:
            # 17新店进件完成需跑定时任务
            self.update_wechat(4)

            self.update_alipay(4)

            self.update_store_subject(2201)

            # self.update_store(201)

        else:
            print("error")

        return "111"




    def close_coon(self):
        self.coon.close()







if __name__ == '__main__':
    userId = input("请输入需改为进件完成的店铺:")
    merchant_type = input("店铺类型：5小微，6个人，7企业：")
    sb_status = input(
                      "1微信认证中，支付宝认证失败；\n"
                      "2微信认证中，支付宝待签约；\n"
                      "3微信认证中，支付宝认证通过；\n"
                      "4支付宝认证中，微信认证失败；\n"
                      "5支付宝认证中，微信待签约；\n"
                      "6支付宝认证中，微信认证通过；\n"
                      "7微信待签约，支付宝认证失败；\n"
                      "8微信待签约，支付宝认证通过；\n"
                      "9支付宝待签约，微信认证失败；\n"
                      "10支付宝待签约，微信认证通过；\n"
                      "11双方待签约；\n"
                      "12微信认证失败，支付宝认证通过；\n"
                      "13支付宝认证失败，微信认证通过；\n"
                      "14双方都认证失败；\n"
                      "15老店进件完成；\n"
                      "16新店进件完成；\n"
                      "17新店进件完成需要跑定时任务：\n"
                      "-----需要修改的状态："
                      )


    update_store = update_store_sql(userId,merchant_type)

    # 修改店铺进件状态
    update_store.update_store_subject_status(sb_status)

    #  新增签约记录
    # update_store.add_store_sign()

    # 新增实名认证记录
    # update_store.add_real_name(merchant_type)


    # 关闭数据库连接
    update_store.close_coon()
