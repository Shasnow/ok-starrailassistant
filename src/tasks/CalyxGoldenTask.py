import re

from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class CalyxGoldenTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("拟造花萼（金）", "经验材料/信用点", *args, **kwargs)
        self.default_config['关卡'] = '角色经验材料'
        self.config_type['关卡'] = {
            'type': "drop_down",
            'options': ['角色经验材料', '光锥强化材料', '信用点'],
        }

    def run(self):
        if not self.page_locate(re.compile("金")):
            return
        if not self.level_locate():
            return
        self.set_battle_number()
        self.battle()
        self.info_set(self.name,'任务完成')

    def level_locate(self, **kwargs):
        match self.config.get('关卡'):
            case '角色经验材料':
                target_point = (0.80, 0.38)
            case '光锥强化材料':
                target_point = (0.80, 0.51)
            case '信用点':
                target_point = (0.80, 0.64)
            case _:
                self.log_error("未找到指定关卡")
                self.send_key('esc')
                return False
        for i in range(30):
            if len(self.ocr(0.81, 0.89, 0.92, 0.93, match=re.compile("挑战"), log=True)) == 0:
                self.click(*target_point, down_time=0.5, after_sleep=0.5)
            else:
                return True
        else:
            self.log_info('Time out: 未找到挑战按钮')
            return False
