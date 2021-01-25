# shadowsocksr-win-speedtest
![](http://81.68.195.64/pic/ssr-speed-test.png)
项目主要借鉴自mobier的shadowsocksr-speed,项目链接：https://github.com/mobier/shadowsocksr-speed
针对自己的使用对windows版本进行了一定的修改
所使用shadowsocksr-csharp版本:v4.9.2

# 使用
## Windows用户
仅通过sivel的speedtest-cli进行节点测速

```
git clone https://github.com/HaoKeee/shadowsocksr-win-speedtest.git
cd shadowsocksr-win-speedtest
将个人已经更新订阅,需要测试的gui-config.json替换到./ShadowsocksR/gui-config.json
打开./ShadowsocksR/ShadowsocksR-dotnet4.0.exe,修改服务器订阅设置为关闭自动更新订阅，并将选项设置中的本地端口修改为6665,推出ssr客户端
python main.py
```

PS:
测试速度较慢,后续如有需要或添加根据订阅地址进行批量测速的功能
代码还有很大的改进空间，部分最终结果为Fail的节点实际或仍可使用，请酌情使用
