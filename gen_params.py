__author__ = 'Rocky'

import time
import rsa #https://pypi.python.org/pypi/rsa/
import base64
import cmdid
import hashlib
import  json
PASSWORD = 's123'
PUBLIC_MODULE = 'mYb9aRdThZkDlfAXEF0lEVy2b0eVaSrr+ghOWr4wry4fShasfU/7Rr/69bO/+N0Oe9No6SSFqTzKpq8PXoU8EdpYlok42WfUsE6kZchjq2wnMknY4tdQWAKEKfzsqRI4LiKAjZOj28+qdOVdYq04Zv6rW355xRy7oJ1V48Ov66U='
PUBLIC_EXPONENT = 'AQAB'
PRIVATE_MODULE = 'mYb9aRdThZkDlfAXEF0lEVy2b0eVaSrr+ghOWr4wry4fShasfU/7Rr/69bO/+N0Oe9No6SSFqTzKpq8PXoU8EdpYlok42WfUsE6kZchjq2wnMknY4tdQWAKEKfzsqRI4LiKAjZOj28+qdOVdYq04Zv6rW355xRy7oJ1V48Ov66U='
PRIVATE_EXPONENT = 'AQAB'
PRIVATE_P = 'xlF62EPaAELFmItSEf0FnqPcp3cnRZ8DPUaL8zWGm1e+pw4CNFfO5WYchOSsIxnuXIwDQJ9+S0itr+ZVQiJxHw=='
PRIVATE_Q = 'xi5usxeISPiecqjY4MrqCYET1vqQdiu9+QpWYsVTFsiqSdmZMu6Di/wJBSiMPMImj/am+X1DnT6sXtOAYD12uw=='
PRIVATE_DQ = 'rUDllyW/v9aVlWyxaDGpxSvWSx8XWgVO6StGfFTYocGIN51PY7cKcvJAHAFCOPAggw12kfBEfzShODh7Z2l7dQ==</DP><DQ>FlXBUBnE2ER8xvtUhfEYcz3C2KWghlDjth9+IN+QP68Z0fzeESlkVfBvq88oDujqo6ruoouFhUE89+rqOu5yZQ=='
PRIVATE_INVERSE_Q = 'DVNzBL+HwxBwpBBRy7QIH64u49mC/CuMKn1bN7IeKqtapItQduT87g6vqtlVcMz5pycx/5i+IO+vnnZgOuUziQ=='
PRIVATE_D = 'S3jBsFzIMT/ENHwfSmsPotZZ1KBzAY0ZDgPxSMiANE3PEePNjZi45NHRc+GWOKeqzBJkW2AZ2NVKpeAfBQ8oNLegEYKG0V0YbRYl4LZLZWV42pE8OUPBSx09BDc8Xf5WERlNn5dRsArKL0CrSvBWtv24RVRfCQkrvZezfXrA0+0='
current_milli_time = lambda: int(round(time.time()))


class GenParams:
    def __init__(self, bid):
        public_module = int.from_bytes(base64.b64decode(PUBLIC_MODULE), byteorder='big', signed=False)
        public_exponent = int.from_bytes(base64.b64decode(PUBLIC_EXPONENT), byteorder='big', signed=False)
        self.public_key = rsa.PublicKey(public_module, public_exponent)

        self.params = {'a': ''}
        self.params['b'] = str(bid)
        c = str(current_milli_time())
        self.params['c'] = c
        self.params['d'] = self.gen_d(c)
        self.params['e'] = ''
        self.params['f'] = '1'

    def gen_d(self, c):
        plain_text = c + PASSWORD
        plain_buf = plain_text.encode(encoding='utf-8')
        cipher_buf = rsa.encrypt(plain_buf, self.public_key)
        cipher_text = base64.b64encode(cipher_buf).decode(encoding='utf-8')
        return cipher_text

    @staticmethod
    def get_str_md5(str):
        m = hashlib.md5(str.encode(encoding='utf-8'))
        return base64.b64encode(m.digest()).decode(encoding='utf-8')


    def user_auth(self, param):
        self.params['a'] = str(cmdid.USER_AUTH)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def user_edit_pwd(self, param):
        self.params['a'] = str(cmdid.USER_CHANGE_PASSWORD)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def member_info(self, phone_number):
        self.params['a'] = str(cmdid.REQUEST_USER_INFO_BY_MOBILE)
        self.params['e'] = '{\"A\":\"' + phone_number + '\"}'
        return self.params

    def member_level(self):
        self.params['a'] = str(cmdid.REQUEST_USER_LEVEL)
        self.params['e'] = ''
        return self.params

    def member_info_card(self, card):
        self.params['a'] = str(cmdid.REQUEST_USER_INFO_BY_CARD)
        self.params['e'] = '{\"A\":\"' + card + '\"}'
        return self.params

    def jewelry_info(self, num):
        self.params['a'] = str(cmdid.REQUEST_JEWELS_INFO)
        self.params['e'] = '{\"A\":\"' + num + '\"}'
        return self.params

    def add_member(self, param):
        self.params['a'] = str(cmdid.NEW_USER)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def order_list(self, param):
        self.params['a'] = str(cmdid.READ_ORDER)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def del_order(self, ordernum):
        self.params['a'] = str(cmdid.DEL_ORDER)
        self.params['e'] = '{\"A\":\"' + ordernum + '\"}'
        return self.params

    def del_order_info(self, param):
        self.params['a'] = str(cmdid.DEL_ORDER_DETAIL)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def modify_order_row(self, param):
        self.params['a'] = str(cmdid.MODIFY_ORDER_ROW)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def read_last_n_order(self, param):
        self.params['a'] = str(cmdid.READ_LAST_N_ORDER)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def read_order_by_mobile(self, param):
        self.params['a'] = str(cmdid.READ_ORDER_BY_MOBILE)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def read_order_by_date(self, param):
        self.params['a'] = str(cmdid.READ_ORDER_BY_DATE)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def read_order_by_status(self, param):
        self.params['a'] = str(cmdid.READ_ORDER_BY_STATUS)
        self.params['e'] = json.dumps(param).replace(' ', '')
        print(type(self.params))
        return self.params

    def read_order_by_date_status_name(self, param):
        self.params['a'] = str(cmdid.READ_ORDER_BY_DATE_STATUS_NAME)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def read_order_by_status_mobile(self, param):
        self.params['a'] = str(cmdid.READ_ORDER_BY_STATUS_MOBILE)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params

    def query_inventory(self, param):
        self.params['a'] = str(cmdid.QUERY_INVENTORY)
        self.params['e'] = json.dumps(param).replace(' ', '')
        print(self.params['e'])
        return self.params

    def save_order(self, param):
        self.params['a'] = str(cmdid.SAVE_ORDER)
        self.params['e'] = json.dumps(param).replace(' ', '')
        return self.params


