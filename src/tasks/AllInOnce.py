from ok import BaseTask

from src.tasks.CalyxCrimsonTask import CalyxCrimsonTask
from src.tasks.CalyxGoldenTask import CalyxGoldenTask
from src.tasks.CaverOfCorrosionTask import CaverOfCorrosionTask
from src.tasks.EchoOfWarTask import EchoOfWarTask
from src.tasks.OrnamentExtractionTask import OrnamentExtractionTask
from src.tasks.ReceiveRewardTask import ReceiveRewardTask
from src.tasks.StagnantShadowTask import StagnantShadowTask


class AllInOnce(BaseTask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "日常一条龙"
        self.description = "启动游戏、登录、清体力、领奖励（清体力在对应任务项配置，设置关卡或次数为0则跳过）"

    def run(self):
        if not self.wait_login():
            return
        self.log_info('日常一条龙任务进行中...')
        ornamentExtractionTask=self.get_task_by_class(OrnamentExtractionTask)
        ornamentExtractionTask.info_set=self.info_set
        ornamentExtractionTask.run()
        calyxGoldenTask=self.get_task_by_class(CalyxGoldenTask)
        calyxGoldenTask.info_set=self.info_set
        calyxGoldenTask.run()
        calyxCrimsonTask=self.get_task_by_class(CalyxCrimsonTask)
        calyxCrimsonTask.info_set=self.info_set
        calyxCrimsonTask.run()
        stagnantShadowTask=self.get_task_by_class(StagnantShadowTask)
        stagnantShadowTask.info_set=self.info_set
        stagnantShadowTask.run()
        caverOfCorrosionTask=self.get_task_by_class(CaverOfCorrosionTask)
        caverOfCorrosionTask.info_set=self.info_set
        caverOfCorrosionTask.run()
        echoOfWarTask=self.get_task_by_class(EchoOfWarTask)
        echoOfWarTask.info_set=self.info_set
        echoOfWarTask.run()
        receiveRewardTask= self.get_task_by_class(ReceiveRewardTask)
        receiveRewardTask.info_set=self.info_set
        receiveRewardTask.run()
        self.log_info('任务完成',notify=True)

    def wait_login(self):
        for i in range(600):
            state1=self.ocr(0.46875, 0.925, 0.53125, 0.955, match="点击进入", log=True)
            state2=self.ocr(0.04,0.89, 0.08,0.92, match='Enter', log=True)
            state3=self.ocr(0.67, 0.23, 0.72, 0.26, match="开拓等级", log=True)
            self.log_info("获取登录状态... {}/600 s".format(i+1))
            if len(state1)!=0:
                self.click(0.5, 0.5, down_time=0.3, after_sleep=1)
                self.log_info("点击进入游戏")
                continue
            elif len(state2)!=0:
                return True
            elif len(state3)!=0:
                self.send_key('esc', down_time=0.1)
            self.sleep(1)
        else:
            self.log_error("获取登录状态超时")
            return False


