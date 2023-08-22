"""
这是一个数据处理的包
"""


class Record:  # 定义数据处理的类
    ID = None
    Content = None
    Score = None

    def __init__(self, ID, Content, Score):
        self.ID = ID
        self.Content = Content
        self.Score = Score

    def __str__(self):
        return f"ID:{self.ID},\nContent:{self.Content},\nScore:{self.Score}\n"
