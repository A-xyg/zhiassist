"""生成器:按需分块读取大文件,避免一次性载入内存"""

from collections.abc import Iterator  #类型注解:迭代器


def read_chunks(path:str,chunk_size: int = 1024) -> Iterator[str]:
    """
    按固定字节数分块读取文本文件
    
    参数:
        path:文件路径
        chunk_size:每块读取的字符数
    返回:
        生成器,每次yield 一块文本.
    说明:
        用yield而非返回list:100MB文件也不好一次占满内存。
    """
    with open(path,"r",encoding="UTF-8") as f: #上下文管理器:自动关闭文件
        while True:
            chunk = f.read(chunk_size)  #只读一小块
            if not chunk:               #读到文件末尾，退出循环
                break
            yield chunk                 #产出这一块,暂停在此处 