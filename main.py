from pylab import *
from gooey import Gooey, GooeyParser
from docx2pdf import convert
import os

def program_killer():
    sys.exit()


def transformer(filepath,lastpath):
    path = str(filepath)
    file = os.path.splitext(path)
    name_file = os.path.basename(filepath).split('.')[0]
    filename, type = file
    new_file = lastpath + r'\\' + name_file + ".pdf"
    print(filepath, new_file)
    real_type = type[1:]
    convert(filepath, new_file)


@Gooey(
    richtext_controls=True,  # 打开终端对颜色支持
    program_name="word格式转换器",  # 程序名称
    language='chinese',
    encoding="utf-8",  # 设置编码格式，打包的时候遇到问题
    progress_regex=r"^progress: (\d+)%$"  # 正则，用于模式化运行时进度信息
)
def main():
    parser = GooeyParser(description='开始转换吧')
    parser.add_argument('文件原路径', widget="FileChooser")
    parser.add_argument('目标格式', widget="Dropdown", choices={'pdf': 0})
    parser.add_argument('文件输出路径', widget="DirChooser")
    args = parser.parse_args()
    if args.目标格式 == 'pdf':
        transformer(args.文件原路径,args.文件输出路径)
        print(args, flush=True)  # 坑点：flush=True在打包的时候会用到


if __name__ == '__main__':
    main()
