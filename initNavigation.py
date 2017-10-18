# -*- coding: utf-8 -*-
# !/usr/bin/env python2

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

next_line_tag = '\n'
navigation = [u"关于我",u"Java",u"数据库",u"设计模式",u"集成框架",u"Linux",u"Go",u"Python",u"Docker",u"大前端",u"工具",u"解决方案",u"管理相关",u"面试题"]
navigationName = 'navigation.md'


def walk_dir_get_data(dir,fileinfo):
    for nav in navigation:
        # 主目录
        fileinfo.write(next_line_tag)
        fileinfo.write('[' + nav + ']()' + next_line_tag)
        fileinfo.write(next_line_tag)

        dir2 = os.path.join(dir, nav)
        if os.path.isdir(dir2):
            # 二级目录
            for file_name in os.listdir(dir2):
                dir3 = os.path.join(dir2, file_name)
                if os.path.isdir(dir3):
                    # 三级目录
                    fileinfo.write('* # '+file_name+next_line_tag)
                    for file_name_2 in os.listdir(dir3):
                        if os.path.isdir(os.path.join(dir3,file_name_2)):
                            continue
                        else:
                            if file_name_2.find('.md') != -1:
                                fileinfo.write('* [' + file_name_2.replace('.md','') + '](' + nav + '/' + file_name + '/' + file_name_2 + ')' + next_line_tag)
                    fileinfo.write('- - - -'+next_line_tag)
                else:
                    if file_name.find('.md') != -1:
                        fileinfo.write('* [' + file_name.replace('.md', '') + '](' + nav + '/' + file_name + ')' + next_line_tag)


# 获取脚本文件的当前路径
def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def main():
    # dir = raw_input('please input the path:')
    dir = cur_file_dir()
    os.remove(navigationName)
    fileinfo = open(navigationName,'w')
    fileinfo.write(u'# 非专业Java程序员博客'+next_line_tag)
    fileinfo.write(u'[gimmick:theme](cerulean)'+next_line_tag)
    walk_dir_get_data(dir, fileinfo)


if __name__ == '__main__':
    main()
    print 'init navigation success!'
