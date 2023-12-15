import random
import pytest
import yaml
# class Test_Demo():
#     def test_demo(self):
#         a = 5
#         b = -1
#         assert a != b
#         print("我的第一个测试用例")


# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",
#                          [(3,5,8),
#                           (-1,-2,-3),
#                           (100,200,300),
#                           ])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected


# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",
#                          [(3,5,8),
#                           (-1,-2,-3),
#                           (100,200,300),
#                           ],ids=["int","minus","bigint"])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected


# 参数组合
# @pytest.mark.parametrize("a",[0,1])
# @pytest.mark.parametrize("b",[2,3])
# def test_foo(a,b):
#     print("测试数据组合：a—>%s,b—>%s" % (a,b))


# 模块中的方法
# def setup_module():
#     print("\nesetup_module: 整个test_module.py模块只执行一次")
# def teardown_module():
#     print("\nteardown_module: 整个test_module.py模块只执行一次")
# def setup_function():
#     print("\nsetup_function: 每个不在类的用例开始前都会执行")
# def teardown_gnction():
#     print("\nteardown_function: 每个不在类中的用例结束后都会执行")
# # 测试模块中的用例1
# def test_one():
#     print("正在执行测试模块------test_one")
# # 测试模块中的用例2
# def test_two():
#     print("正在执行测试模块------test_two")
# # 测试模块中的用例3
# def test_three():
#     print("正在执行测试模块------test_three")
# # 测试模块中的用例4
# def test_four():
#     print("正在执行测试模块------test_four")



# class Test_Demo():
#     @pytest.mark.demo
#     def test_demo(self):
#         a = 5
#         b = -1
#         assert a != b
#         print("我的第一个测试用例") 
#     @pytest.mark.smoke
#     def test_two(self):
#         a = 2
#         b = -1
#         assert a != b
#         print("我的第二个测试用例")
    
#     @pytest.mark.demo
#     @pytest.mark.smoke
#     def test_add_02():
#         b = 1+2
#         assert 0 == b


# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",
#                          yaml.safe_load(open("./data.yml"))["datas"],
#                          ids=yaml.safe_load(open("./data.yml"))["myid"])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected
    
# def get_datas():
#     with open("./data.yaml") as f:
#         datas = yaml.safe_load(f)
#         print(datas)
#         add_datas=datas["datas"]
#         add_ids=datas["myid"]
#         return [add_datas,add_ids]
    
    
# # 改进    
# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",
#                          get_datas()[0],
#                          ids=get_datas()[1])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected

@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_example():
        print(3)
        assert 1 == -1
        # assert random.choice([True,False])