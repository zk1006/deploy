#!/usr/bin/env python
# encoding: utf-8

# @Time         : 2018/3/17 下午3:03
# @Author       : zk
# @Mail         : zk1006@live.cn 
# @File         : upProject.py
# @description  :
import shell
import datetime
import sys


def up_pro(pros, svn_path, bak_path):
    temp = pros[0]
    if isinstance(temp, str):
        pros = api_sort(pros)
        for api in pros:
            # 打包api
            shell.exec_cmd("cd "+svn_path+"/"+api+" && svn update && mvn clean install -Dmaven.test.skip=true")
    else:
        pros = tomcat_sort(pros)
        for pro in pros:
            commd_str = sys.path[0] + "/cpAndStart.sh " + pro["tomcat"] + " "+bak_path+" "
            # 停止tomcat操作
            # shell.exec_cmd("ps -ef|grep "+pro["tomcat"]+"|grep -v grep|cut -c 9-15|xargs kill -9")
            for path in pro["pro"]:
                # 打包
                shell.exec_cmd("cd " + svn_path + "/" +
                               path['svn'] + " && svn update && mvn clean install -Dmaven.test.skip=true -P test")
                # 备份到目录
                shell.exec_cmd(
                    "cp -rp " + pro["tomcat"] + "/webapps/" + path['name'] + ".war " + bak_path + "/" + path['name'] +
                    "/" + datetime.datetime.now().strftime('-%Y%m%d%H%M%S') + ".war")
                # 删除相应的项目
                shell.exec_cmd("rm -rf " + pro["tomcat"] + "/webapps/" + path['name'] + "*")
                commd_str += path['name']+","
            # 停止tomcat操作
            shell.exec_cmd("ps -ef|grep " + pro["tomcat"] + "|grep -v grep|cut -c 9-15|xargs kill -9")
            shell.exec_cmd(commd_str)
    return


# api排序,model类放到前面
def api_sort(apis):
    api_list = []
    for api in apis:
        if 'model' in api:
            api_list.append(api)
    for api in apis:
        api_list.append(api)
    return sorted(set(api_list), key=api_list.index)


def tomcat_sort(pros):
    tomcats = []
    for pro in pros:
        tomcats.append(pro["tomcat"])
    tomcats = sorted(set(tomcats), key=tomcats.index)
    project = []
    for tomcat in tomcats:
        pro_paths = []
        for pro in pros:
            if tomcat == pro["tomcat"]:
                pro_paths.append({"svn": pro["path"], "name": pro["name"]})
        project.append({"tomcat": tomcat, "pro": pro_paths})
    return project