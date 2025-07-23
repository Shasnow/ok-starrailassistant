from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class CaverOfCorrosionTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("侵蚀隧洞", "仪器", *args, **kwargs)
        self.level = ['雳涌之径', '弦歌之径', '迷识之径', '勇骑之径', '梦潜之径',
                      '幽冥之径', '药使之径', '野焰之径', '圣颂之径', '睿治之径',
                      '漂泊之径', '迅拳之径', '霜风之径']

    def run(self):
        self.page_locate("侵蚀隧洞", True)
        if not self.level_locate():
            return
        self.set_battle_number()
        self.battle()
        self.log_info('侵蚀隧洞 任务完成')
