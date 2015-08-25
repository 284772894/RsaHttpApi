__author__ = 'Rocky'


import json_request
import gen_params
import json
gen = gen_params.GenParams(10027)

#登陆
def user_auth():
    s_param = { 'A': 'A001-0001', 'B': gen_params.GenParams.get_str_md5('123456')}
    params = gen.user_auth(s_param)
    response = json_request.request(params=params)
    print(response)
#修改密码
def user_edit_pwd():
    s_param = { 'A': 'A001-0001', 'B': gen_params.GenParams.get_str_md5('123456')}
    params = gen.user_edit_pwd(s_param)
    response = json_request.request(params=params)
    print(response)

#获取会员级别名称表
def member_level():
    params = gen.member_level()
    response = json_request.request(params=params)
    print(response)

#按手机号获取会员信息
def member_info(phone_number):
    params = gen.member_info(phone_number)
    response = json_request.request(params=params)
    print(response)

#按卡号获取会员信息
def member_info_card(card):
    params = gen.member_info_card(card)
    response = json_request.request(params=params)
    print(response)

#获取珠宝成品信息
def jewelry_info(num):
    params = gen.jewelry_info(num)
    response = json_request.request(params=params)
    print(response)

#新增会员
def add_member():
    s_params = {"A": "13925526263", "B": "姓名", "C": "1001001", "D": "1982", "E": "12", "F": "31", "G": "深圳市罗湖翠竹路8号", "H": "A001"}
    params = gen.add_member(s_params)
    response = json_request.request(params=params)
    print(response)

#读取订单
def order_list():
    s_params = {"A": "H0115050001", "B": "0", "C": "H001"}
    params = gen.order_list(s_params)
    response = json_request.request(params=params)
    print(response)

#删除订单
def del_order(ordernum):
    params = gen.del_order(ordernum)
    response = json_request.request(params=params)
    print(response)

#删除订单明细行
def del_order_info():
    s_params = {"A": "H0115050001", "B": "1"}
    params = gen.del_order_info(s_params)
    response = json_request.request(params=params)
    print(response)

#更改订单主表行
def modify_order_row():
    s_params ={"单号":"H0114050001","卡号":"88888888","备注":"","客户姓名":"张三","客户级别":2,"工号":"1001","店铺":"H01","总实销价":12000,"总数量":2,"总销售价":15000,"手机号":"13901000001",
               "日期": "2014-06-15","时间":"2014-06-15 12:20","状态":128,"积分":0}
    params = gen.modify_order_row(s_params)
    response = json_request.request(params=params)
    print(response)

#读取最后N笔订单列表
def read_last_n_order():
    s_params = {"A": "H001001", "B": "0"}
    params = gen.read_last_n_order(s_params)
    response = json_request.request(params=params)
    print(response)

#按手机号读取订单列表
def read_order_by_mobile():
    s_params = {"A": "H001", "B": "13912345678"}
    params = gen.read_order_by_mobile(s_params)
    response = json_request.request(params=params)
    print(response)

#按日期读取订单列表
def read_order_by_date():
    s_params = {"A": "H001", "B": "2014-6-6", "C": "2014-6-6"}
    params = gen.read_order_by_date(s_params)
    response = json_request.request(params=params)
    print(response)

#按状态读取订单列表
def read_order_by_status():
    s_params = {"A": "H001", "B": "2014-6-6", "C": "2014-6-6", "D": "128", "E": "张三", "F": "13800138000"}
    params = gen.read_order_by_status(s_params)
    response = json_request.request(params=params)
    print(response)

#按日期状态客户姓名读取
def read_order_by_date_status_name():
    s_params = {"A": "H001", "B": "2014-6-6", "C": "2014-6-6", "D": "128", "E": "13800138000"}
    params = gen.read_order_by_date_status_name(s_params)
    response = json_request.request(params=params)
    print(response)

#按状态读取订单
def read_order_by_status_mobile():
    s_params = {"A": "H001", "B": "2014-6-6", "C": "2014-6-6", "D": "128", "E": "13800138000"}
    params = gen.read_order_by_status_mobile(s_params)
    response = json_request.request(params=params)
    print(response)
#查询库存
def query_inventory():
    s_params = {"A": "A001_SY01", "B": "", "C": "", "D": "", "E": "", "F": "-1", "H": " -1"}
    params = gen.query_inventory(s_params)
    response = json_request.request(params=params)
    print(response)

#保存订单
def save_order():
    dct_json = {"Orders": []}
    for i in range(0, 2):
        list_json = {}
        list_json["LID"] = str(i + 1)
        list_json["名称"] = "18K吊坠"
        list_json["款号"] = "A001"
        list_json["实销价"] = "8000"
        list_json["序号"] = str(i + 1)
        list_json["数量"] = "1"
        list_json["货号"] = "1254633"
        list_json["销售价"] = "50000"
        dct_json["Orders"].append(list_json)
    dct_json["单号"] = ""
    dct_json["卡号"] = "88888888"
    dct_json["备注"] = ""
    dct_json["客户姓名"] = "张三"
    dct_json["客户级别"] = "2"
    dct_json["工号"] = "1001"
    dct_json["店铺"] = "H01"
    dct_json["总实销价"] = "12000"
    dct_json["总数量"] = "2"
    dct_json["总销售价"] = "15000"
    dct_json["手机号"] = "13901000001"
    dct_json["日期"] = "2014-06-15"
    dct_json["状态"] = "128"
    dct_json["积分"] = "0"
    params = gen.save_order(dct_json)
    response = json_request.request(params=params)
    print(response)
    # print(temp)


#裸钻api
def loose_diamond():
    params = { "token": "gIj(aJ]bU*IbchuG_ac"}

    response = json_request.request(base_url='order.kela.cn', port=None, api='/api/jxs/api.php?a=dialist', params=params)
    dict_r = json.loads(response)
    print(dict_r)

#总部公告
def notice():
    params = {"status": 0, "nums": 10, "token": "gIj(aJ]bU*IbchuG_ac"}
    response = json_request.request(base_url="order.kela.cn", api="/api/jxs/api.php?a=notice", port=None, params=params)
    dict_r = json.loads(response)
    print(dict_r)
#客户管理
def users():
    #http://order.kela.cn/api/jxs/api.php?a=users
    params = {"act": "list", "token": "gIj(aJ]bU*IbchuG_ac", "Name": "小小"}
    response = json_request.request(base_url="order.kela.cn", api="/api/jxs/api.php?a=users", port=None, params=params)
    dict_r = json.loads(response)
    print(dict_r)
#款号查询
def Goodsprice():
    params_str = "&a=Goodsprice&opt=ori&page=1&style_sn=KLRW006460&xiangkou=0.25&caizhi=1&shoucun=14"
    response = json_request.request(base_url="order.kela.cn", api="/api/jxs/api.php?token=gIj(aJ]bU*IbchuG_ac" + params_str, port=None,  method="get")
    dict_r = json.loads(response)
    print(dict_r)

if __name__ == "__main__":
    user_auth()
    #Goodsprice()
    Goodsprice()

