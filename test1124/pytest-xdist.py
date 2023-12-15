import pytest
# 模块中的方法
def setup_module():
    print("\nesetup_module: 整个test_module.py模块只执行一次")
def teardown_module():
    print("\nteardown_module: 整个test_module.py模块只执行一次")
def setup_function():
    print("\nsetup_function: 每个不在类的用例开始前都会执行")
def teardown_gnction():
    print("\nteardown_function: 每个不在类中的用例结束后都会执行")
# 测试模块中的用例1
def test_one():
    print("正在执行测试模块------test_one")
# 测试模块中的用例2
def test_two():
    print("正在执行测试模块------test_two")
# 测试模块中的用例3
def test_three():
    print("正在执行测试模块------test_three")
# 测试模块中的用例4
def test_four():
    print("正在执行测试模块------test_four")\
        
        
class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("我的第一个测试用例") 
    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b = -1
        assert a != b
        print("我的第二个测试用例")
    
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_add_02():
        b = 1+2
        assert 3 == b
