import re

from ok import BaseTask

from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class CalyxGoldenTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("CalyxGoldenTask","拟造花萼（金）",*args, **kwargs)

    def run(self):
        self.page_locate()

    def page_locate(self):
        super().page_locate()
        result_box_list = self.ocr(0.14, 0.26, 0.27, 0.82, match=re.compile("金"), log=True)
        if len(result_box_list) == 0:
            self.log_error("未找到页面，请手动定位")
            return False
        result_box = result_box_list[0]
        self.click(result_box, down_time=0.5)
        return True


