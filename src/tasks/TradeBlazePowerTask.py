import ctypes
import re

import win32gui
from ok import BaseTask,Box


class TradeBlazePowerTask(BaseTask):
    def __init__(self, name, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.default_config = {
            '关卡': 0,
            '次数': 0,
            '连续作战': 1,
            '使用支援角色': False,
            '补充体力次数': 0,
            '补充体力方式': '后备开拓力',
        }
        self.config_description = {
            '关卡': '选择要刷的关卡，在列表中由上之下第几个（按更新时间排序）',
            '次数': '选择要刷的次数',
            '连续作战': '连续作战的次数，仅对有连续作战的关卡有效',
            '使用支援角色': '是否使用支援角色',
            '补充体力次数': '补充体力的次数，0表示不补充',
        }
        self.config_type['补充体力方式'] = {
            'type': 'drop_down',
            'options': ['后备开拓力', '燃料', '星琼'],
        }
        self.level=[]

    def run(self):
        pass

    def page_locate(self, page=None, need_scroll=False):
        """
        定位到页面
        :return: none
        """
        if self.config.get('关卡', 0) == 0 or self.config.get('次数', 0) == 0:
            self.info_set(self.name,"跳过")
            return False

        for i in range(30):
            if len(self.ocr(0.05, 0.06, 0.12, 0.09, match=["每日实训", "生存索引"], log=True))!=0:
                break
            self.send_key('f4',down_time=0.1)  # F4
            self.sleep(1)
        else:
            self.info_set(self.name,"超时")
            return False
        for i in range(30):
            if len(self.ocr(0.05, 0.06, 0.12, 0.09, match="生存索引", log=True)) != 0:
                break
            self.click(0.25, 0.20,down_time=0.5)
        else:
            self.info_set(self.name,"超时")
            return False

        self.sleep(0.5)
        if need_scroll:
            self.scroll_relative(0.24, 0.43, -12)
            self.sleep(0.5)
            self.scroll_relative(0.24, 0.43, -12)
            self.sleep(0.5)
        result_box_list = self.ocr(0.14, 0.26, 0.27, 0.82, match=page, log=True)
        if len(result_box_list) == 0:
            self.log_error("未找到页面，请手动定位")
            return False
        result_box = result_box_list[0]
        self.click(result_box, down_time=0.5)
        return True

    def level_locate(self,x_offset=600, y_offset=0):
        self.info_set(self.name, "定位关卡")
        for i in range(30):
            result_list=self.ocr(0.45, 0.28, 0.52, 0.81, match=self.level[self.config.get('关卡') - 1], log=True)
            if len(result_list) == 0:
                self.scroll_relative(0.5,0.5,-12)
                self.sleep(1)
                continue
            target_box = result_list[0]
            target_box.x += x_offset  # 向进入按钮偏移
            target_box.y += y_offset
            break
        else:
            self.info_set(self.name,'未找到指定关卡')
            return False
        for i in range(30):
            if len(self.ocr(0.81, 0.89, 0.92, 0.93, match=re.compile("挑战"), log=True)) != 0:
                break
            self.click(target_box,down_time=0.5, after_sleep=0.5)
            return True
        else:
            self.log_info('Time out: 未找到挑战按钮')
            return False

    def wait_battle_end(self, timeout=30):
        """
        等待战斗结束
        :return: none
        """
        self.info_set(self.name, "等待战斗结束")
        time = 0
        state = Box(name="未知状态", x=0, y=0, width=0, height=0)
        while time < timeout:
            self.sleep(1)
            time += 1
            result_list = self.ocr(0.43, 0.20, 0.57, 0.30, match=["挑战成功", "战斗失败"], log=True)
            if len(result_list) ==0:
                continue
            state = result_list[0]
            break
        if state.name == "挑战成功":
            self.info_set(self.name,"挑战成功")
        elif state.name == "战斗失败":
            self.info_set(self.name,"战斗失败")
        else:
            self.log_error("未知状态: {}".format(state.name))

    def again(self):
        """
        再来一次
        :return: none
        """
        self.click(0.63, 0.88,after_sleep=0.5,down_time=0.5)
        if self.replenish_check()==1:
            self.click(0.63, 0.88, after_sleep=0.5,down_time=0.5)
        elif self.replenish_check()==-1:
            self.info_set(self.name,"退出战斗")
            self.quit()
            return


    def replenish_check(self):
        if len(self.ocr(0.45, 0.30, 0.55, 0.35, match="开拓力补充", log=True)) !=0:
            if self.config.get("补充体力次数", 0) > 0:
                self.click(0.61, 0.67, after_sleep=0.5,down_time=0.5)
                self.click(0.61, 0.72, after_sleep=0.5,down_time=0.5)
                return 1
            else:
                self.info_set(self.name,"体力不足")
                self.send_key('esc',after_sleep=0.5,down_time=0.2)
                return -1
        return 0

    def quit(self):
        """
        退出战斗
        :return: none
        """
        self.click(0.37, 0.88,down_time=0.5)
        self.sleep(1)

    def click_no_position(self):
        self.operate(self.do_click_no_position)

    def do_click_no_position(self):
        self.sleep(0.01)
        self.do_mouse_down('left')
        self.do_mouse_up('left')
        self.sleep(0.01)

    def operate(self, func):
        self.executor.interaction.operate(func, block=True)

    def do_mouse_down(self, key):
        self.executor.interaction.do_mouse_down(key=key)

    def do_mouse_up(self, key):
        self.executor.interaction.do_mouse_up(key=key)

    def scroll_relative(self, x, y, amount):
        user32 = ctypes.windll.user32
        old_hwnd = user32.GetForegroundWindow()
        same = old_hwnd == self.hwnd.hwnd
        if not same:
            self.hwnd.bring_to_front()

        self.executor.interaction.do_scroll(self.width_of_screen(x), self.height_of_screen(y), amount)

        if not same:
            win32gui.SetForegroundWindow(old_hwnd)

    def set_battle_number(self):
        """
        设置战斗次数
        :return: none
        """
        num=self.config['连续作战']
        self.info_set(self.name,f"设置战斗次数为{num}")
        for i in range(num-1):
            self.click(0.96,0.81, down_time=0.4, after_sleep=0.1)

    def battle(self):
        """
        开始战斗
        :return: 流程正常完成返回True，流程中断返回False
        """
        _time=self.config.get('次数', 1)
        self.info_set(self.name,'开始战斗')
        for i in range(30):
            if len(self.ocr(0.84,0.89, 0.90, 0.92, match="开始挑战", log=True)) != 0:
                break
            self.click(0.83,0.91,down_time=0.4)
            if self.replenish_check()==-1:
                self.send_key('esc', after_sleep=0.5, down_time=0.2)
                self.send_key('esc', after_sleep=0.5, down_time=0.2)
                return False
            self.sleep(0.5)
        else:
            self.log_info('Time out: 未找到开始挑战按钮')
            return False
        if self.config.get('使用支援角色', False):
            self.click(0.90,0.67,down_time=0.4)
            target_box_list=self.wait_ocr(0.86,0.90,0.89,0.94, match='入队',time_out=10)
            if len(target_box_list) == 0:
                self.log_info("未找到支援角色")
                return False
            self.click(target_box_list[0],down_time=0.4,after_sleep=0.2)

        self.click(0.83,0.91,down_time=0.4)
        _time -= 1
        for i in range(_time):
            self.wait_battle_end(timeout=600)
            self.again()
        else:
            self.wait_battle_end(timeout=600)
        self.quit()
        self.send_key('esc', after_sleep=1)
        return True




