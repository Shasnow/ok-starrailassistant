from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class OrnamentExtractionTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__('饰品提取', '刷选定的饰品提取关卡，需要有差分宇宙存档', *args, **kwargs)
        self.level = ["月下朱殷", "纷争不休", "蠹役饥肠", "永恒笑剧", "伴你入眠", "天剑如雨", "孽果盘生", "百年冻土",
                      "温柔话语", "浴火钢心", "坚城不倒"]

    def run(self):
        time = self.config.get('次数', 1)
        self.page_locate()
        if not self.page_check():
            self.page_relocate()
        if not self.level_locate():
            return

        # self.click(0.35,0.77,after_sleep=1)
        # self.click(0.22,0.12,after_sleep=1)
        # self.click(0.15, 0.26,after_sleep=1)
        while len(self.ocr(0.86, 0.90, 0.92, 0.92, match="开始挑战", log=True)) != 0:
            self.click(0.87, 0.91, down_time=1)
        if self.replenish_check()==-1:
            self.send_key('esc',after_sleep=1)
            self.send_key('esc', after_sleep=0.5)
            return
        self.wait_ocr(0.03, 0.01, 0.08, 0.04, match="差分宇宙", log=True, time_out=30)
        self.send_key('w', down_time=2.5)
        self.click_no_position()
        time-=1
        for i in range(time):
            self.wait_battle_end(timeout=600)
            self.again()
        else:
            self.wait_battle_end(timeout=600)
        self.quit()
        self.log_info("饰品提取任务完成")

    def page_check(self):
        """
        检查是否在饰品提取页面
        :return: bool
        """
        return len(self.ocr(0.46,0.32, 0.54, 0.36, match="饰品提取", log=True)) != 0

    def page_relocate(self):
        """
        定位到饰品提取页面
        :return: none
        """
        result_box_list=self.ocr(0.14,0.26,0.27,0.82, match="饰品提取", log=True)
        if len(result_box_list) == 0:
            self.log_error("未找到饰品提取页面，请手动定位")
            return False
        result_box = result_box_list[0]
        self.click(result_box,down_time=0.5)
        return True
