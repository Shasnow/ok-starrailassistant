<div align="center">
  <img src="icons/icon.png" alt="icon"><br>
  <h1>ok-sra</h1>
  <img src="https://img.shields.io/badge/platform-Windows-blue" alt="platform">
  <img alt="Static Badge" src="https://img.shields.io/badge/python-3.12%2B-skyblue">

  <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/Shasnow/ok-starrailassistant/total">
  <img alt="GitHub Release" src="https://img.shields.io/github/v/release/Shasnow/ok-starrailassistant">
</div>

### 一个基于图像识别的崩铁自动化程序，帮您完成从启动到退出的崩铁日常。现已支持后台运行。

## 免责声明

本软件是一个外部工具旨在自动化《崩坏：星穹铁道》的游戏玩法。它被设计成仅通过现有用户界面与游戏交互,并遵守相关法律法规。该软件包旨在提供简化和用户通过功能与游戏交互,并且它不打算以任何方式破坏游戏平衡或提供任何不公平的优势。该软件包不会以任何方式修改任何游戏文件或游戏代码。

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。

请注意，根据MiHoYo的 [崩坏:星穹铁道的公平游戏宣言](https://sr.mihoyo.com/news/111246?nav=news&type=notice):

    "严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
    "一经发现，米哈游（下亦称“我们”）将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"

## 有什么功能？

* 日常一条龙
  * 包含 启动游戏、登录、清体力、领奖励
* 清体力
  * 您可以自由选择关卡，是否`补充体力`、`连战次数`、`执行次数`，一切都交由您来决定，也可以`混合搭配`。
* 领取奖励
* 后台运行

## 兼容性
* 支持全 16:9 分辨率
* 简体中文

### Python 源码运行

仅支持Python 3.12

```bash
#CPU版本, 使用openvino
pip install -r requirements.txt --upgrade #install python dependencies, 更新代码后可能需要重新运行
python main.py # run the release version 运行发行版
python main_debug.py # run the debug version 运行调试版
```

### 相关项目

* [StarRailAssistant](https://github.com/Shasnow/StarRailAssistant) 一个基于图像识别的崩铁自动化程序，帮您完成从启动到退出的崩铁日常，支持多账号切换。原始项目。
* [ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves) 鸣潮 后台自动战斗 自动刷声骸 一键日常
* [ok-script-boilerplate](https://github.com/ok-oldking/ok-script-boilerplate) ok-script 脚本模板项目