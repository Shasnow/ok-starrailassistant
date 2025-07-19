from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class OrnamentExtractionTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__('饰品提取', '刷选定的饰品提取关卡，需要有差分宇宙存档', *args, **kwargs)
        self.level=["月下朱殷","纷争不休","蠹役饥肠","永恒笑剧","伴你入眠","天剑如雨","孽果盘生","百年冻土","温柔话语","浴火钢心","坚城不倒"]

    def run(self):
        self.page_locate()
        target_box=self.ocr(0.45,0.42,0.52,0.81, match=self.level[self.config.get('关卡') - 1], log=True)[0]
        target_box.x+=600 #向进入按钮偏移
        while len(self.ocr(0.86,0.90,0.92,0.92, match="开始挑战", log=True))==0:
            self.click(target_box,after_sleep=0.5)
        self.click(0.35,0.77,after_sleep=1)
        self.click(0.22,0.12,after_sleep=1)
        self.click(0.15, 0.26,after_sleep=1)
        while len(self.ocr(0.86, 0.90, 0.92, 0.92, match="开始挑战", log=True)) != 0:
            self.click(0.87, 0.91,after_sleep=0.5)
        self.wait_ocr(0.03,0.01,0.08,0.04, match="差分宇宙", log=True, time_out=30, settle_time=1)
        self.send_key('w',down_time=2.5)
        while len(self.ocr(0.16,0.80,0.17,0.82, match="1",log=True)) ==0:
            self.click(0.5,0.5,after_sleep=0.5) #点击屏幕中心普攻进入战斗
