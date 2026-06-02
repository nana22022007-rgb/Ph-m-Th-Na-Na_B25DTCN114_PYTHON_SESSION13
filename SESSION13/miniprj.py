
parking_lot = []
next_id = 1

GIA_XE_MAY = 5000
GIA_O_TO = 20000
while True:
    print("\n====================================================")
    print("           QUẢN LÝ BÃI XE - SMART PARKING")
    print("====================================================")
    print("   1. Check-in (Đăng ký xe vào)")
    print("   2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("   3. Tìm kiếm xe (Theo biển số)")
    print("   4. Check-out (Xử lý xe ra & Tính phí)")
    print("   5. Thoát chương trình")
    print("====================================================")
    
    choice_str = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    if not choice_str.isdigit():
        print("[ERR-05] [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue # Quay lại đầu vòng lặp menu
        
    choice = int(choice_str)
    if choice < 1 or choice > 5:
        print("[ERR-05] [Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue

    if choice == 1:
        print("\n--- CHECK-IN (ĐĂNG KÝ XE VÀO) ---")
        
        while True:
            plate = input("Nhập biển số xe: ").strip().upper()
            if not plate:
                print("[Lỗi]: Biển số xe không được để trống!")
                continue
            
            is_duplicate = False
            for car in parking_lot:
                if car['plate'] == plate:
                    is_duplicate = True
                    break
            
            if is_duplicate:
                print("[ERR-01] [Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
                continue 
            break 

        # Nhập loại xe (Bắt lỗi nhập chữ/sai số bằng .isdigit())
        while True:
            type_str = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            
            if not type_str.isdigit():
                print("[ERR-02] [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                continue
                
            vehicle_type = int(type_str)
            if vehicle_type not in [1, 2]:
                print("[ERR-02] [Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                continue
            break

        # Nhập giờ vào (Bắt lỗi nhập chữ bằng .isdigit())
        while True:
            entry_str = input("Nhập giờ vào (0-24): ").strip()
            
            if not entry_str.isdigit():
                print("[Lỗi]: Định dạng giờ vào phải là số nguyên!")
                continue
                
            entry_time = int(entry_str)
            if entry_time < 0 or entry_time > 24:
                print("[Lỗi]: Giờ vào phải nằm trong khoảng từ 0 đến 24!")
                continue
            break

        # Lưu thông tin xe vào Dictionary
        new_vehicle = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }
        parking_lot.append(new_vehicle)
        print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi.")
        next_id += 1 

    # -------------------------------------------------------------------------
    # CHỨC NĂNG 2: BÁO CÁO TỒN KHO
    # -------------------------------------------------------------------------
    elif choice == 2:
        print("\n--- BÁO CÁO TỒN KHO ---")
        if len(parking_lot) == 0:
            print("[Thông báo: Bãi xe hiện đang trống!]")
        else:
            print(f"{'ID':<6} | {'Biển số xe':<15} | {'Loại xe':<10} | {'Giờ vào':<8}")
            print("-" * 50)
            for car in parking_lot:
                type_str = "Xe máy" if car['type'] == 1 else "Ô tô"
                print(f"{car['id']:<6} | {car['plate']:<15} | {type_str:<10} | {car['entry_time']:<8}")

    # -------------------------------------------------------------------------
    # CHỨC NĂNG 3: TÌM KIẾM XE
    # -------------------------------------------------------------------------
    elif choice == 3:
        print("\n--- TÌM KIẾM XE ---")
        search_plate = input("Nhập biển số xe cần tìm: ").strip().upper()
        
        found = False
        for car in parking_lot:
            if car['plate'] == search_plate:
                print(f"Thông tin chi tiết: {car}")
                found = True
                break 
                
        if not found:
            print(f"[ERR-04] [Lỗi]: Không tìm thấy biển số {search_plate} trong hệ thống!")

    # -------------------------------------------------------------------------
    # CHỨC NĂNG 4: CHECK-OUT (TÍNH PHÍ & XÓA XE)
    # -------------------------------------------------------------------------
    elif choice == 4:
        print("\n--- CHECK-OUT (XỬ LÝ XE RA & TÍNH PHÍ) ---")
        checkout_plate = input("Nhập biển số xe cần ra: ").strip().upper()
        
        car_index = -1
        for i in range(len(parking_lot)):
            if parking_lot[i]['plate'] == checkout_plate:
                car_index = i
                break 
                
        if car_index == -1:
            print(f"[ERR-04] [Lỗi]: Không tìm thấy biển số {checkout_plate} trong hệ thống!")
        else:
            car = parking_lot[car_index]
            
            # Nhập giờ ra và bẫy lỗi bằng .isdigit() thay cho try-except
            while True:
                exit_str = input("Nhập giờ ra (0-24): ").strip()
                
                if not exit_str.isdigit():
                    print("[Lỗi]: Định dạng giờ ra phải là số nguyên!")
                    continue
                    
                exit_time = int(exit_str)
                if exit_time < 0 or exit_time > 24:
                    print("[Lỗi]: Giờ ra phải nằm trong khoảng từ 0 đến 24!")
                    continue
                if exit_time < car['entry_time']:
                    print("[ERR-03] [Lỗi]: Giờ ra phải sau hoặc bằng giờ vào!")
                    continue 
                break 
            
            # Tính tiền
            duration = exit_time - car['entry_time']
            if duration == 0:
                duration = 1 
                
            unit_price = GIA_XE_MAY if car['type'] == 1 else GIA_O_TO
            total_fee = duration * unit_price
            
            print(f"Tổng phí phải trả: {total_fee} VNĐ")
            
            # Xóa xe khỏi danh sách
            parking_lot.pop(car_index)
            print(f"[Thành công]: Đã thanh toán và giải phóng xe {checkout_plate} ra khỏi hệ thống.")

    # -------------------------------------------------------------------------
    # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
    # -------------------------------------------------------------------------
    elif choice == 5:
        print("\n[Hệ thống]: Đang đóng ứng dụng. Cảm ơn em đã sử dụng Smart Parking!")
        break