# 京东爬虫

这是一个简单的爬虫程序，初学者随便学习一下。

## 快速开始

在目录的main.py下，修改参数productID为你需要爬取的商品ID，运行即可。

项目还提供两个参数，page：你需要爬取的评论页数；score：score=0爬取所有类型的评论，score=1 爬取差评，score=2爬取中评，score=3爬取好评

运行完成后，会在当前目录下生成名为商品ID的CSV数据文件。

那么怎么获取你需要爬取商品的ID呢？

- 1. 打开网页版京东

     ![](https://picgo2333.oss-cn-beijing.aliyuncs.com/picgo/image-20230823015538134.png)

- 2. 搜索你需要的商品（例如sony wf-1000xm4）

     ![](https://picgo2333.oss-cn-beijing.aliyuncs.com/picgo/image-20230823015737135.png)



- 3. 打开商品详情页
 ![image-20230823015904872](https://picgo2333.oss-cn-beijing.aliyuncs.com/picgo/image-20230823015904872.png)

- 4. 网址上的这串数字就是商品ID（10081732738778）

     ![image-20230823020053629](https://picgo2333.oss-cn-beijing.aliyuncs.com/picgo/image-20230823020053629.png)