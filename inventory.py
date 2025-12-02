products = []  # Danh sách toàn cục
def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "qty": quantity
    }
    products.append(product)
    print(f"Đã thêm sản phẩm: {name}")

def main():
    while True:
        print("\n=== QUẢN LÝ KHO HÀNG ===")
        print("1. Nhập hàng (Add Product)")
        print("2. Xem tồn kho (View Inventory)")
        print("3. Cảnh báo hết hàng (Low Stock)")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")
        if choice == "0":
            print("Thoát chương trình...")
            break
        elif choice == "1":
            n = input("Tên sản phẩm: ")
            p = int(input("Giá bán: "))
            q = int(input("Số lượng: "))
            add_product(n, p, q)

    else:
        print("Chức năng này sẽ được cập nhật sau.")
      
