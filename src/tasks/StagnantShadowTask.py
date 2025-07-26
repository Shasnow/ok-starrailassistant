import re

from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class StagnantShadowTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("凝滞虚影", "角色晋阶材料", *args, **kwargs)
        self.level = ['烬日之形', '溟簇之形', '凛月之形', '役轮之形', '弦音之形',
                      '今宵之形', '机狼之形', '职司之形', '嗔怒之形', '焦炙之形',
                      '冰酿之形', '幽府之形', '燔灼之形', '孽兽之形', '偃偶之形',
                      '天人之形', '震厄之形', '冰棱之形', '幻光之形', '霜晶之形',
                      '锋芒之形', '炎华之形', '鸣雷之形', re.compile('风'), '空海之形', ]

    def run(self):
        if not self.page_locate('凝滞虚影', True):
            return
        if not self.level_locate():
            return
        self.set_battle_number()
        self.battle()
        self.info_set(self.name,'任务完成')
