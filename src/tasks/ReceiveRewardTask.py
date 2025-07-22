from ok import BaseTask


class ReceiveRewardTask(BaseTask):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = "领取奖励"
        self.description = "领取奖励"

    def run(self):
        if not self.esc_page_locate():
            return
        self.assignments_reward()
        self.sleep(1)
        self.send_key('esc')

    def trailblazer_profile(self):
        self.log_info("执行任务：签证奖励")
        if self.click(0.92,0.10, down_time=0.5):
            if self.click(0.82,0.13, down_time=0.5):
                pass
            else:
                self.log_info("没有可领取的奖励2")
        else:
            self.log_info("没有可领取的奖励3")
        self.log_info("任务完成：签证奖励")

    def mail(self):
        pass

    def assignments_reward(self):
        self.log_info("执行任务：领取派遣奖励")
        for i in range(30):
            if len(self.ocr(0.05,0.03, 0.08, 0.06, match="委托", log=True)) == 0:
                self.click(0.91,0.35, down_time=0.5,after_sleep=0.5)  # 点击派遣
            else:
                break
        else:
            self.log_info('Time out: 未找到派遣按钮')
            return

        result_list= self.ocr(0.23,0.83, 0.28, 0.86, match="一键领取", log=True)
        if len(result_list) == 0:
            self.log_info("没有可以领取的派遣奖励")
            self.send_key("esc")
            self.sleep(2)
            return

        self.click(result_list[0],down_time=0.5,after_sleep=0.5)

        box=self.wait_ocr(0.61,0.87, 0.66, 0.90, match="再次派遣", log=True, time_out=20)
        self.click(box,after_sleep=4)
        self.send_key('esc')

    def esc_page_locate(self):
        for i in range(30):
            if not self.ocr(0.67, 0.23, 0.72, 0.26, match="开拓等级", log=True):
                self.send_key('esc')
                self.sleep(2)
            else:
                return True
        else:
            self.log_info('Time out')
            return False