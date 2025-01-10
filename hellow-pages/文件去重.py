from pathlib import Path
import filecmp

path_list = [path for path in Path(r'D:backup').iterdir() if path.is_file()]

for front in range(len(path_list) - 1):
    for later in range(front + 1, len(path_list)):
        if filecmp.cmp(path_list[front], path_list[later], shallow=False):
            path_list[front].unlink()    # 删除文件
            break
