from jd_spider import Spider

# 修改该商品ID,就可以写入前50页商品评论到本目录下的CSV文件中
productID = 10081732738778  # 商品ID
page = 50   # 爬取页数
score = 0   # score=0爬取所有类型的评论，score=1 爬取差评，score=2爬取中评，score=3爬取好评


def run(ID, page, score):
    jd = Spider(productId=ID, page=page, score=score)
    jd.csv_write()


run(productID, page, score)
