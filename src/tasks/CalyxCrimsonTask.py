import re

from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class CalyxCrimsonTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("拟造花萼（赤）", "行迹材料", *args, **kwargs)
        self.level=[re.compile('纷争'), re.compile('匹诺'), re.compile('苏乐达'),'绥园',
                    re.compile('克劳克'),re.compile('白日梦'),'鳞渊境','丹鼎司',
                    '大矿区','机械聚落','铆钉镇','边缘通路','城郊雪原','支援舱段','收容舱段']

    def run(self):
        if not self.page_locate(re.compile("赤")):
            return
        if not self.level_locate():
            return
        self.set_battle_number()
        self.battle()
        self.info_set(self.name,'任务完成')

