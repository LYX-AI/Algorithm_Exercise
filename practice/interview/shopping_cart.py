from datetime import datetime
#获取折扣
def find_discount(text, target_category, settlement_date):
    lines = text.strip().split('\n')
    for line in lines:
        if line.strip():
            parts = line.split('|')
            if len(parts) >= 3:
                date = parts[0].strip()
                discount = float(parts[1].strip())
                category = parts[2].strip()

                if category == target_category:
                    discount_date = datetime.strptime(date, "%Y.%m.%d")
                    pay_date = datetime.strptime(settlement_date, "%Y.%m.%d")
                    if discount_date == pay_date:
                        return discount
    return 1.0  # 没打折，返回原价系数
#找到商品所属的分类
def find_category(categories, product_name):
    for category, products in categories.items():
        if product_name in products:
            return category
    return None  # 没找到

def calculate_total(commodity, input_text):
    sections = input_text.strip().split('\n\n')
    promotional_info = sections[0]
    shopping_info = sections[1]
    settlement_date = sections[2].strip()
    coupon_info = sections[3].strip() if len(sections) > 3 else None
    # 解析商品列表
    lines = shopping_info.strip().split('\n')
    total = 0.0
    for line in lines:
        if line.strip():
            amount_part, product_part = line.split('*')
            amount = int(amount_part.strip())
            product_name, price_part = product_part.split(':')
            product_name = product_name.strip()
            price = float(price_part.strip())
            category = find_category(commodity, product_name)
            discount = find_discount(promotional_info, category, settlement_date)
            final_price = amount * price * discount
            total += final_price

    # 处理优惠券
    if coupon_info:
        parts = coupon_info.split()
        if len(parts) == 3:
            coupon_date_str, threshold_str, discount_str = parts
            coupon_date = datetime.strptime(coupon_date_str, "%Y.%m.%d")
            pay_date = datetime.strptime(settlement_date, "%Y.%m.%d")
            threshold = float(threshold_str)
            discount_amount = float(discount_str)
            if pay_date <= coupon_date and total >= threshold:
                total -= discount_amount
    # 保留2位小数，四舍五入
    return round(total + 1e-8, 2)
def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        input_text = f.read()
    commodity = {
        "电子": ["ipad", "iphone", "显示器", "笔记本电脑", "键盘"],
        "食品": ["面包", "饼干", "蛋糕", "牛肉", "鱼", "蔬菜"],
        "日用品": ["餐巾纸", "收纳箱", "咖啡杯", "雨伞"],
        "酒类": ["啤酒", "白酒", "伏特加"]
    }
    result = calculate_total(commodity, input_text)
    print(result)
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python shopping_cart.py 输入文件名")
    else:
        main(sys.argv[1])

