封装及demo by 道长 on 2019/4/15
使用本模块需要环境支持:
1.dm.dll 和 lw.dll 提前注册到系统
2.32位python3.7.3版本
3.pypiwin2库 pywin32 可以通过命令 pip install pywin32 进行安装
4.win32com库 pypiwin32 可以通过命令 pip install pypiwin32 进行安装
5.comtypes库 可以通过命令 pip install comtypes 进行安装
6.打包exe库  pyinstaller 可以通过命令 pip install pyinstaller 进行安装


打包exe详细说明:
-i 表示设置软件图标 -w 表示隐藏命令黑框 -F表示打包主py程序
一般带gui界面的就要加上-w

pyinstaller --version-file=ver.txt -i logo.ico -w -F main.py  #打包不带黑窗口的单文件 打包窗口类脚本辅助推荐用这个
pyinstaller --version-file=ver.txt -i logo.ico -w --upx upx394w -F main.py  #打包不带黑窗口的且upx压缩单文件(win10运行异常)
pyinstaller --version-file=ver.txt -i logo.ico -w --upx upx394w -D main.py  #打包不带黑窗口的且upx压缩文件依赖文件夹(win10运行异常)
pyinstaller  -F  test.spec #按这个配置好的信息进行打包
pyinstaller --version-file=ver.txt -i logo.ico -F main.py  #打包带黑窗口的
python grab_version.py C:\Users\Administrator\Desktop\py大漠3.11\click.exe
python set_version.py file_version_info.txt C:\Users\Administrator\Desktop\py大漠3.11\click.exe

PyInstaller自带的版权工具路径 C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyInstaller\utils\cliutils\grab_version.py

到该工具路径，按住shift再右键再此处打开命令窗口然后输入:python grab_version.py 标准程序的路径 如:

python grab_version.py C:\Users\Administrator\Desktop\py大漠3.11\click.exe

会在PyInstaller自带的版权工具路径里面生成一个file_version_info.txt文档。将这个文档用notepad++打开并编辑里面直观的信息然后保存即可。

注入版权信息同样在该工具目录内:python set_version.py file_version_info.txt youfilename.exe即可,如:
python set_version.py file_version_info.txt C:\Users\Administrator\Desktop\py大漠3.11\click.exe

或者在打包的时候就已经准备好了版本信息文件：file_version_info.txt
打包时附带有如下参数：pyinstaller –file-version file_version_info.txt yourfile.py即可，如:
pyinstaller --version-file=ver.txt -i logo.ico -F main.py  #这里提前把文件file_version_info.txt改成ver.txt了
