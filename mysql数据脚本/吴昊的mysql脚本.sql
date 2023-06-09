INSERT INTO viewset_customer (Customer_ID, Customer_Name, Customer_Sex, Customer_Age, Customer_Type)
VALUES
    (1, '张斌', 1, 32, '普通顾客'),
    (2, '王响', 1, 45, '普通顾客'),
    (3, '王永祥', 1, 52, 'VIP顾客'),
    (4, '赵步凡', 1, 42, 'VIP顾客'),
    (5, '赵悦', 0, 22, '普通顾客'),
    (6, '赵丽颖', 0, 32, 'VIP顾客'),
    (7, '胡歌', 1, 37, 'VIP顾客'),
    (8, '杨幂', 0, 35, 'VIP顾客'),
    (9, '张靓颖', 0, 34, 'VIP顾客'),
    (10, '王俊凯', 1, 23, '普通顾客'),
    (11, '王源', 1, 22, '普通顾客'),
    (12, '丁真', 1, 20, 'VIP顾客'),
    (13, '王鸥', 0, 31, '普通顾客'),
    (14, '毛晓彤', 0, 27, '普通顾客'),
    (15, '胡语越', 1, 19, '普通顾客'),
    (16, '吴日天', 1, 20, '普通顾客'),
    (17, '罗贯中', 1, 67, 'VIP顾客'),
    (18, '吴承恩', 1, 72, 'VIP顾客'),
    (19, '郑凯', 1, 38, '普通顾客'),
    (20, '李晨', 1, 36, '普通顾客'),
    (21, '邓超', 1, 42, '普通顾客'),
    (22, '孙俪', 0, 39, 'VIP顾客'),
    (23, '黄晓明', 1, 35, '普通顾客'),
    (24, '周立波', 1, 34, '普通顾客'),
    (25, '杨颖', 0, 33, 'VIP顾客'),
    (26, '长泽雅美', 0, 31, '普通顾客'),
    (27, '小岛秀夫', 1, 46, 'VIP顾客'),
    (28, '宫崎英高', 1, 48, '普通顾客'),
    (29, '宫崎骏', 1, 65, '普通顾客'),
    (30, '魏晨', 1, 31, 'VIP顾客');

INSERT INTO viewset_product (Product_ID, Product_Name, Product_Type)
VALUES
    (1, '玫瑰苹果', '水果'),
    (2, '富士康苹果', '水果'),
    (3, '双汇五花肉', '肉类'),
    (4, '汇源胡萝卜', '蔬菜'),
    (5, '金果火龙果', '水果'),
    (6, '塔里木哈密果', '水果'),
    (7, '高钙牛奶', '奶类'),
    (8, '低脂牛奶', '奶类'),
    (9, '东北大米', '蔬菜'),
    (10, '云南金针菇', '其他'),
    (11, '海南香蕉', '水果'),
    (12, '云南猴头菇', '其他'),
    (13, '新鲜牛五花', '肉类'),
    (14, '新鲜牛舌', '肉类'),
    (15, '新鲜羊排', '肉类'),
    (16, '绿源生菜', '蔬菜'),
    (17, '有机卷心菜', '蔬菜'),
    (18, '有机大葱', '蔬菜'),
    (19, '有机奶', '奶类'),
    (20, '婴幼儿配方奶粉', '其他'),
    (21, '原酵酸奶', '奶类'),
    (22, '葡萄味酸奶', '奶类'),
    (23, '儿童成长奶粉', '其他'),
    (24, '海南猕猴桃', '水果'),
    (25, '东北大土豆', '蔬菜');

INSERT INTO viewset_supplier (Supplier_ID, Supplier_Name)
VALUES
    (1, '金果集团'),
    (2, '龙盛果业'),
    (3, '丰收果园'),
    (4, '天禾果业'),
    (5, '果香源农业'),
    (6, '宏达果品公司'),
    (7, '绿叶果汇'),
    (8, '果宝园有限公司'),
    (9, '东方果园'),
    (10, '新鲜果缘供应商'),
    (11, '蒙牛乳业'),
    (12, '伊利集团'),
    (13, '双汇肉业');

INSERT INTO viewset_warehouse (WareHouse_ID, WareHouse_Name, WareHouse_Address)
VALUES
    (1, '北京顺义仓', '北京市顺义区天竺镇新龙西路18号'),
    (2, '北京昌平1仓', '北京市昌平区南口镇回龙观东大街2号'),
    (3, '北京昌平2仓', '北京市昌平区沙河镇北清路8号'),
    (4, '天津滨海仓', '天津市滨海新区塘沽街道海河东路10号'),
    (5, '天津蓟县仓', '天津市蓟县城区静海路88号'),
    (6, '北京海淀仓', '北京市海淀区中关村南大街10号'),
    (7, '上海徐汇仓', '上海市徐汇仓虹桥路100号'),
    (8, '徐州鼓楼1仓', '江苏省徐州市鼓楼区胜利路168号'),
    (9, '徐州鼓楼2仓', '江苏省徐州市鼓楼区人民中路99号'),
    (10, '深圳蛇口仓', '深圳市南山区蛇口港大道1号'),
    (11, '深圳盐田仓', '深圳市盐田区盐田路88号'),
    (12, '海南海口仓', '海南省海口市美兰区人民大道100号'),
    (13, '海南文昌仓', '海南省文昌市文城镇中山路10号'),
    (14, '山东威海1仓', '山东省威海市环翠区海滨路56号'),
    (15, '山东威海2仓', '山东省威海市荣成区人民路98号'),
    (16, '河南商丘仓', '河南省商丘市梁园区中华路100号'),
    (17, '河北廊坊1仓', '河北省廊坊市安次区广阳道68号'),
    (18, '河北廊坊2仓', '河北省廊坊市霸州区胜利路36号'),
    (19, '福州宁德仓', '福建省福州市宁德市蕉城区解放路168号'),
    (20, '北京大兴仓', '北京市大兴区亦庄经济开发区科创十一街18号');