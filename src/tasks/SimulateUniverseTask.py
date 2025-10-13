import re

from ok import BaseTask


class SimulateUniverseTask(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "差分宇宙"
        self.description = "刷周期演算，仅第一层，请先打开差分宇宙界面，再运行此任务"
        self.default_config = {
            "次数": 1
        }
        self.config_description = {
            "次数": "刷周期演算的次数"
        }

    def run(self):
        """主任务执行函数"""
        self.info_set("差分宇宙", "执行任务：差分宇宙-周期演算")

        for exe_time in range(self.config.get("次数", 1)):
            if not self._start_differential_universe(exe_time):
                return False
            if not self._select():
                return False
            if not self._navigate_and_fight():
                return False
            if not self._select():
                return False
            if not self._complete_mission():
                return False

        self._return_to_main_menu()
        self.info_set("差分宇宙", "Mission accomplished")
        return True

    def _start_differential_universe(self, exe_time):
        """开始差分宇宙任务"""
        self.info_set("差分宇宙", f"第{exe_time + 1}次进入差分宇宙，少女祈祷中…")
        box = self.wait_ocr(0.79, 0.87, 0.86, 0.92, match=re.compile("开始"), time_out=30)
        box = box[0] if box else None
        # 点击开始按钮
        if box is None or not self.click_box(box, down_time=0.2):
            self.log_error("发生错误，错误编号18")
            return False

        # 等待并点击周期演算
        box = self.wait_ocr(0.28, 0.46, 0.36, 0.52, match=re.compile("周期"), time_out=30)
        box = box[0] if box else None
        if box is None:
            self.log_error("发生错误，错误编号19")
            return False
        self.click_box(box, down_time=0.2)

        # 启动差分宇宙
        box = self.wait_ocr(0.82, 0.88, 0.93, 0.92, match=re.compile("启动"), time_out=30)
        box = box[0] if box else None
        if box is None or not self.click_box(box):
            self.log_error("发生错误，错误编号20")
            return False

        return True

    def _navigate_and_fight(self):
        """导航和战斗处理"""
        self.info_set("差分宇宙", "移动")
        self.send_key("w", down_time=2.6)

        self.info_set("差分宇宙", "进入战斗")
        self.click_no_position()

        # 检查是否需要使用技能
        # 框架不支持
        # if self.wait_img("resources/img/q.png", timeout=10):
        #     self.press_key("v")

        self.info_set("差分宇宙", "等待战斗结束")
        if not self.wait_ocr(0.04, 0.04, 0.13, 0.10, match=re.compile("选择"), time_out=120):
            self.log_error("失败/超时")
            return False

        return True

    def _select(self):
        """选择祝福"""
        var = ["选择基础效果", "选择祝福", "选择方程", "选择奇物", "点击空白处关闭","方程展开", re.compile("第一位面")]

        while True:
            box = self.wait_ocr(0.04, 0.00, 0.9, 0.95, match=var, time_out=30)
            box = box[0] if box else None
            if box.name in var:
                index = var.index(box.name)
            else:
                if "第一位面" in box.name:
                    index = 6
                else:
                    index = -1

            if index == 0 or index == 1 or index == 2 or index == 3:  # 祝福选择或方程式选择或奇物选择
                self.info_set("差分宇宙", var[index])
                self.sleep(0.5)
                self.click(0.45, 0.5, down_time=0.2)  # NOQA
                box = self.wait_ocr(0.45, 0.88, 0.90, 0.91, match=re.compile("确"), time_out=30)
                box = box[0] if box else None
                if box is None:
                    return False
                self.click_box(box, down_time=0.2)
            elif index == 4 or index == 5:  # 方程式扩展或关闭
                self.send_key('esc', down_time=0.1)
                self.sleep(0.5)
            else:  # 退出
                break

        return True

    def _complete_mission(self):
        """完成任务结算"""
        self.info_set("差分宇宙", "退出并结算")
        for i in range(30):
            if not self.ocr(0.68, 0.89, 0.77, 0.93, match=re.compile("结束")):
                self.send_key("esc", down_time=0.1)
                self.sleep(1)
            else:
                break
        else:
            self.log_error("无法退出，错误编号21")
            return False

        self.click(0.8, 0.9, down_time=0.2, after_sleep=0.5)  # NOQA
        self.click(0.61, 0.72, down_time=0.2, after_sleep=0.5)  # NOQA

        self.info_set("差分宇宙", "返回主界面")
        if self.wait_ocr(0.47, 0.89, 0.54, 0.93, match=re.compile("返回"), time_out=30):
            self.click(0.50, 0.91, down_time=0.1, after_sleep=0.5)  # NOQA

        return True

    def _return_to_main_menu(self):
        """返回主菜单"""
        self.send_key("esc", down_time=0.1, interval=1)
        self.send_key("esc", down_time=0.1, interval=1)

    def operate(self, func):
        self.executor.interaction.operate(func, block=True)  # NOQA

    def do_mouse_down(self, key):
        self.executor.interaction.do_mouse_down(key=key)  # NOQA

    def do_mouse_up(self, key):
        self.executor.interaction.do_mouse_up(key=key)  # NOQA

    def click_no_position(self):
        self.operate(self.do_click_no_position)

    def do_click_no_position(self):
        self.sleep(0.01)
        self.do_mouse_down('left')
        self.do_mouse_up('left')
        self.sleep(0.01)
