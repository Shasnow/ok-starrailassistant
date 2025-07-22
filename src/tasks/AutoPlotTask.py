from ok import TriggerTask


class AutoPlotTask(TriggerTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动剧情"
        self.description = "进入剧情时自动点击对话和选项"
        self.plot_count = 0

    def run(self):
        if self.get_plot_state():
            self.send_key("space")


    def get_plot_state(self):
        """
        获取当前剧情状态
        :return: 当前剧情状态
        """
        return len(self.ocr(0.07, 0.04, 0.15, 0.07, match=['L','M'], log=True))!= 0
