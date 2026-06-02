vehicle_list = []
next_id = 1

while True:
    print("\n===================================")
    print("QUẢN LÝ BÃI XE - SMART PARKING")
    print("===================================")
    print("1. Thêm xe mới vào bãi")
    print("2. Hiển thị danh sách xe trong bãi")
    print("3. Tìm kiếm xe theo ID")
    print("4. Xóa xe khỏi bãi")
    print("5. Thoát chương trình")
    print("===================================")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        while True:
            vehicle_type = input("Nhập loại xe: ").strip()
            if vehicle_type:
                break
            print("Loại xe không được để trống!")

        while True:
            owner = input("Nhập tên chủ xe: ").strip()
            if owner:
                break
            print("Tên chủ xe không được để trống!")

        vehicle = {
            "id": next_id,
            "type": vehicle_type,
            "owner": owner
        }

        vehicle_list.append(vehicle)
        print(f"Đã thêm xe ID {next_id} thành công!")
        next_id += 1

    elif choice == "2":
        if len(vehicle_list) == 0:
            print("Bãi xe hiện đang trống!")
        else:
            print(f"\n{'ID':<10}{'Loại xe':<20}{'Chủ xe':<20}")
            print("-" * 50)

            for vehicle in vehicle_list:
                print(f"{vehicle['id']:<10}"
                    f"{vehicle['type']:<20}"
                    f"{vehicle['owner']:<20}"
                )

    elif choice == "3":
        id_input = input("Nhập ID cần tìm: ")

        if not id_input.isdigit():
            print("ID phải là số!")
        else:
            search_id = int(id_input)
            found = False

            for vehicle in vehicle_list:
                if vehicle["id"] == search_id:
                    print(vehicle)
                    found = True
                    break

            if not found:
                print(f"Không tìm thấy xe có ID {search_id}!")

    elif choice == "4":
        id_input = input("Nhập ID xe muốn xóa: ")

        if not id_input.isdigit():
            print("ID phải là số!")
        else:
            delete_id = int(id_input)
            found = False

            for vehicle in vehicle_list:
                if vehicle["id"] == delete_id:
                    vehicle_list.remove(vehicle)
                    found = True
                    print(f"Đã xóa xe ID {delete_id} thành công!")
                    break

            if not found:
                print("Không tìm thấy xe để xóa!")

    elif choice == "5":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")