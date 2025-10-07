def find_larger():
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    if num1 > num2:
        larger = num1
    elif num2 > num1:
        larger = num2
    else:
        larger = num1
    print(f"较大的数字是：{larger}")
    return larger
find_larger()
