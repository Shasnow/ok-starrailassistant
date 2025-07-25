import re

from ok import BaseTask


class ReceiveRewardTask(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "领取奖励"
        self.description = "领取奖励"

    def run(self):
        if not self.esc_page_locate():
            return
        self.trailblazer_profile()
        self.assignments_reward()
        self.mail()
        self.sleep(1)
        self.send_key('esc',down_time=0.1)
        self.sleep(0.5)
        self.daily_reward()
        self.sleep(0.5)
        self.nameless_honor()

    def trailblazer_profile(self):
        self.log_info("执行任务：签证奖励")
        self.click(0.92, 0.10, down_time=0.3, after_sleep=0.5)
        self.click(0.82, 0.13, down_time=0.3, after_sleep=0.5)
        self.click(0.88, 0.26, down_time=0.3, after_sleep=1)  # 点击签证奖励
        if len(self.ocr(0.45, 0.08, 0.55, 0.12, match="支援奖励", log=True)) == 0:
            self.send_key('esc', down_time=0.1)
        self.log_info("任务完成：签证奖励")

    def mail(self):
        self.click(0.97, 0.25, down_time=0.3, after_sleep=0.5)  # 点击邮件
        self.click(0.23, 0.91, down_time=0.3, after_sleep=0.5)  # 点击全部领取
        self.click(0.23, 0.91, down_time=0.3, after_sleep=0.5)  # 点击全部领取
        self.send_key('esc', down_time=0.1)
        self.log_info("完成：领取邮件奖励")

    def assignments_reward(self):
        self.log_info("执行任务：领取派遣奖励")
        for i in range(30):
            if len(self.ocr(0.045, 0.025, 0.085, 0.065, match="委托", log=True)) == 0:
                self.click(0.91, 0.35, down_time=0.5, after_sleep=0.5)  # 点击派遣
            else:
                break
        else:
            self.log_info('Time out: 未找到派遣按钮')
            return

        result_list = self.ocr(0.225, 0.825, 0.29, 0.865, match=re.compile('领取'), log=True)
        if len(result_list) == 0:
            self.log_info("没有可以领取的派遣奖励")
            self.send_key("esc")
            self.sleep(2)
            return

        self.click(result_list[0], down_time=0.5, after_sleep=0.5)

        box = self.wait_ocr(0.61, 0.87, 0.66, 0.90, match="再次派遣", log=True, time_out=20)
        self.click(box, down_time=0.2, after_sleep=3)
        self.send_key('esc')

    def daily_reward(self):
        for i in range(30):
            result_list = self.ocr(0.05, 0.06, 0.12, 0.09, match=["每日实训", "生存索引"], log=True)
            if len(result_list) != 0:
                break
            self.send_key('f4', down_time=0.1)  # F4
            self.sleep(0.5)
        else:
            self.log_error("Time out: F4展开超时")
            return

        if result_list[0].name == '生存索引':
            self.send_key('esc', down_time=0.1)
            return
        self.sleep(2)
        target = self.ocr(0.21, 0.75, 0.25, 0.78, match='领取', log=True)
        while len(target)!=0:
            self.click(target[0], down_time=0.3, after_sleep=0.5)
            target = self.ocr(0.21, 0.75, 0.25, 0.78, match='领取', log=True)

        count=self.ocr(0.16,0.31, 0.195, 0.345, log=True)
        if len(count)==0:
            self.log_info("没有可领取的奖励")
            return
        count = count[0].name
        self.log_info("活跃度："+ count)
        match count:
            case "100":
                self.click(0.33,0.29,down_time=0.3)
            case "200":
                self.click(0.46, 0.29, down_time=0.3)
            case "300":
                self.click(0.59, 0.29, down_time=0.3)
            case "400":
                self.click(0.72, 0.29, down_time=0.3)
            case "500":
                self.click(0.85, 0.29, down_time=0.3)
            case _:
                self.log_info(f"未知奖励数量：{count}，请手动领取")
                return

        close=self.ocr(0.45,0.85, 0.55, 0.90, match=re.compile('关闭'), log=True)
        if len(close) != 0:
            self.click(close[0], down_time=0.3, after_sleep=0.5)
        self.send_key('esc', down_time=0.1)

    def nameless_honor(self):
        for i in range(30):
            if len(self.ocr(0.05, 0.03, 0.10, 0.07, match="无名勋礼", log=True)) != 0:
                break
            self.send_key('f2', down_time=0.1)
            self.sleep(1)
        else:
            self.log_error("Time out: F2展开超时")
            return

        self.click(0.50,0.06, down_time=0.3, after_sleep=0.5)  # 点击无名勋礼

        box_list = self.ocr(0.84, 0.83, 0.91, 0.87, match=re.compile('领取'), log=True)
        if len(box_list) != 0:
            self.click(box_list[0], down_time=0.3, after_sleep=1)
            self.send_key('esc', down_time=0.1)

        self.click(0.45, 0.06, down_time=0.3, after_sleep=0.5)
        box_list = self.ocr(0.71, 0.82, 0.775, 0.87, match=re.compile('领取'), log=True)
        if len(box_list) != 0:
            self.click(box_list[0], down_time=0.3, after_sleep=2)
            self.send_key('esc', down_time=0.1)

        self.send_key('esc', down_time=0.1)
        self.log_info('完成：领取无名勋礼')




    def esc_page_locate(self):
        for i in range(30):
            if not self.ocr(0.67, 0.23, 0.72, 0.26, match="开拓等级", log=True):
                self.send_key('esc', down_time=0.1)
                self.sleep(2)
            else:
                return True
        else:
            self.log_info('Time out')
            return False
