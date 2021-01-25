import subprocess,os,time,json,re,socks,socket,requests,speedtest
from prettytable import PrettyTable

#设置全局变量
ssr_path = '.\ShadowsocksR'

# 绘制结果图表
class DrawTable(object):
    def __init__(self):
        self.table=[]
        header=[
        "name",
        "ip",
        "ping",
        "upload",
        "download",
        "country",
        "network"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True
        self.x.sortby = "download"
        
    def append(self,*args,**kwargs):
        if(kwargs):

            content=[
                kwargs['name'],
                kwargs['ip'],
                kwargs['ping'],
                kwargs['upload'],
                kwargs['download'],
                kwargs['country'],
                kwargs['network'],
            ]
            self.x.add_row(content)
    def str(self):
        return str(self.x)

# 运行 ssr
def run_ssr():
    exe_path = ssr_path + "\ShadowsocksR-dotnet4.0.exe"
    subprocess.Popen(exe_path)
# 关闭ssr
def close_ssr():
    os.popen('taskkill /f /im ShadowsocksR-dotnet4.0.exe')

#获取config文件中的节点列表
def get_nodes():
    config_path = ssr_path + '\gui-config.json'
    with open(config_path,'r',encoding='utf-8') as f:
        json_config = json.load(f)
        return json_config['configs']
# 修改config文件中的index
def change_index(x):
    config_path = ssr_path + '/gui-config.json'
    with open(config_path,'r',encoding='utf-8') as f:
        json_config = json.load(f)

    json_config['index'] = x

    with open(config_path,'w',encoding='utf-8') as f:
        json.dump(json_config,f,indent=4)

#网络测速方法
def speed_test():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 1080)
    socket.socket = socks.socksocket
    servers = []
    # 可设置为具体服务器
    # servers = [1234]

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=None)
    s.upload(threads=None)
    s.results.share()
    return s.results.dict()

#测试当前index为x的节点
def connect_node(ssr):
    result = {}

    result['remarks']=ssr['remarks']

    result['ip']=""
    result['download']=0
    result['upload']=0
    result['ping']=0
    result['country'] = ""
    result['state']="Fail"

    try:
        results_dict = speed_test()

        result['ip'] = results_dict['client']['ip']
        result['download'] = result['download']=round(results_dict['download'] / 1000.0 / 1000.0,2)
        result['upload'] = result['upload']=round(results_dict['upload'] / 1000.0 / 1000.0 ,2)
        result['ping'] = results_dict['ping']
        result['country'] = results_dict['client']['country']

        result['state'] = "Succeed"

    
    except Exception as e:
        print(ssr['remarks'] + " occurred error: " + str(e))
        print(e)

    return result

def main():
    table=DrawTable()
    json_config = get_nodes()
    for x in range(len(json_config)):
        print(str(x+1) + '/' + str(len(json_config)))
        change_index(x)
        run_ssr()
        speed_result = connect_node(json_config[x])
        # os.system('cls')

        table.append(
        name=speed_result['remarks'],
        ip=speed_result['ip'],
        ping=speed_result['ping'],
        upload=speed_result['upload'],
        download=speed_result['download'],
        country=speed_result['country'],
        network=speed_result['state']
    )
        print(table.str())
        close_ssr()
        time.sleep(1)

main()