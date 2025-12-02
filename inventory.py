products = []  # Danh sách toàn cục

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
        else:
            print("Chức năng này sẽ được cập nhật sau.")
