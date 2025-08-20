import random

def mo_phong_rut_tat(so_luong_rut):
    """
    Mô phỏng việc rút tất từ ngăn kéo và kiểm tra có đôi tất cùng màu hay không.
    Ngăn kéo có: 5 đôi tất đen (10 chiếc), 5 đôi tất trắng (10 chiếc).
    """
    tat_trong_ngan_keo = ['đen'] * 10 + ['trắng'] * 10 + ['xám'] * 6

    # Trộn ngẫu nhiên các chiếc tất
    random.shuffle(tat_trong_ngan_keo)

    # Rút ra số lượng tất yêu cầu
    tat_da_rut = tat_trong_ngan_keo[:so_luong_rut]

    # Đếm số lượng tất đen và trắng đã rút được
    dem_den = tat_da_rut.count('đen')
    dem_trang = tat_da_rut.count('trắng')
    dem_xam = tat_da_rut.count('xám')

    print(f"Bạn đã rút ra: {tat_da_rut}")
    print(f"Số tất đen: {dem_den}, Số tất trắng: {dem_trang}, Số tất xám: {dem_xam}")

    # Kiểm tra xem có đôi tất cùng màu hay không (ít nhất 2 chiếc cùng màu)
    if dem_den >= 2 or dem_trang >= 2 or dem_xam >= 2:
        print("=> CHẮC CHẮN CÓ MỘT ĐÔI TẤT CÙNG MÀU (theo Nguyên lý Dirichlet)!")
        return True
    else:
        print("=> CHƯA CHẮC CHẮN có đôi tất cùng màu.")
        return False

print("--- Mô phỏng rút 2 chiếc tất ---")
mo_phong_rut_tat(2) # Thử chạy vài lần để thấy kết quả có thể chưa chắc chắn

print("\n--- Mô phỏng rút 3 chiếc tất ---")
mo_phong_rut_tat(3) # Thử chạy vài lần, bạn sẽ thấy kết quả luôn là "CHẮC CHẮN CÓ MỘT ĐÔI"
mo_phong_rut_tat(3)
mo_phong_rut_tat(3)

"""
Giải thích trường hợp có hai màu đen trắng:
nếu cả 2 cùng màu đen đen trắng trắng => đôi tất cùng màu
nếu rút ra 1 đen 1 trắng thì lúc này không có đôi tất cùng màu
=> mô phỏng 2 chiếc tất có thể thấy đôi khi cùng màu đôi khi khác màu hợp với nguyên lý dirichlket
"""
