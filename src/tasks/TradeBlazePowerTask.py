from ok import BaseTask


class TradeBlazePowerTask(BaseTask):
    def __init__(self, name,description,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.default_config={
            '关卡': 1,
            '次数': 1,
            '连续作战': 1,
            '使用支援角色': False,
        }
        self.config_description = {
            '关卡': '选择要刷的关卡,在列表中由上之下第几个',
            '次数': '选择要刷的次数',
            '连续作战': '连续作战的次数，仅对有连续作战的关卡有效',
            '使用支援角色': '是否使用支援角色',
        }

    def run(self):
        pass

    def page_locate(self):
        """
        定位到生存索引页面
        :return: none
        """

        self.send_key('f4')  # F2
        self.wait_ocr(0.05, 0.06, 0.12, 0.09, match=["每日实训","生存索引"],log=True, time_out=30, settle_time=1)
        while len(self.ocr(0.05, 0.06, 0.12, 0.09, match="生存索引", log=True)) == 0:
            self.click(0.25,0.20)
        self.sleep(0.5)
