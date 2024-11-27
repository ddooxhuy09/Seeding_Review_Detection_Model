-- Bảng ThuThu:
 INSERT INTO ThuThu (MATHUTHU, HO, TEN, PHAI, DIACHI, NGAYSINH, EMAIL, NGAYTAO) VALUES
 ('TT001', N'Nguyễn', N'Hùng', N'NAM', N'123 Nguyễn Văn Cừ, Q.5, TP.HCM', '1990-01-01', 'hungnguyen@gmail.com', '2022-01-01'),
 ('TT002', N'Trần', N'Ngọc', N'NỮ', N'45 Lê Văn Sỹ, Q.3, TP.HCM', '1985-05-10', 'ngoctran@gmail.com', '2022-01-01'),
 ('TT003', N'Lê', N'Minh', N'NAM', N'78 Trần Hưng Đạo, Q.1, TP.HCM', '1988-12-20', 'minhle@gmail.com', '2022-01-01'),
 ('TT004', N'Phạm', N'Thùy', N'NỮ', N'92 Phan Đăng Lưu, Q.Phú Nhuận, TP.HCM', '1992-07-15', 'thuypham@gmail.com', '2022-01-01'),
 ('TT005', N'Võ', N'Thanh', N'NAM', N'135 Nguyễn Thị Minh Khai, Q.1, TP.HCM', '1991-09-05', 'thanhvo@gmail.com', '2022-01-01'),
 ('TT006', N'Đỗ', N'Hương', N'NỮ', N'56 Trương Định, Q.3, TP.HCM', '1993-03-12', 'huongdo@gmail.com', '2022-01-01'),
 ('TT007', N'Hoàng', N'Tuấn', N'NAM', N'89 Lý Thường Kiệt, Q.10, TP.HCM', '1989-11-25', 'tuanhoang@gmail.com', '2022-01-01'),
 ('TT008', N'Trịnh', N'Lan', N'NỮ', N'67 Võ Thị Sáu, Q.3, TP.HCM', '1987-06-18', 'lantrinh@gmail.com', '2022-01-01'),
 ('TT009', N'Ngô', N'Dũng', N'NAM', N'23 Trần Phú, Q.5, TP.HCM', '1994-04-02', 'dungngo@gmail.com', '2022-01-01'),
 ('TT010', N'Đặng', N'Ngân', N'NỮ', N'178 Nguyễn Đình Chiểu, Q.3, TP.HCM', '1990-08-30', 'ngandang@gmail.com', '2022-01-01');
-- Bảng DocGia:
 INSERT INTO DocGia (MADOCGIA, HO, TEN, PHAI, DIACHI, NGAYSINH, EMAIL, SODIENTHOAI, NGAYTAO) VALUES
 ('DG001', N'Lê', N'Hùng', N'NAM', N'123 Nguyễn Văn Cừ, Q.5, TP.HCM', '1990-01-01', 'hungle@gmail.com', '0901234567', '2022-01-01'),
 ('DG002', N'Trần', N'Hoa', N'NỮ', N'45 Lê Văn Sỹ, Q.3, TP.HCM', '1985-05-10', 'hoatran@gmail.com', '0902345678', '2022-01-01'),
 ('DG003', N'Nguyễn', N'Minh', N'NAM', N'78 Trần Hưng Đạo, Q.1, TP.HCM', '1988-12-20', 'minhnguyen@gmail.com', '0903456789', '2022-01-01'),
 ('DG004', N'Phạm', N'Hạnh', N'NỮ', N'92 Phan Đăng Lưu, Q.Phú Nhuận, TP.HCM', '1992-07-15', 'hanhpham@gmail.com', '0904567890', '2022-01-01'),
 ('DG005', N'Võ', N'Trung', N'NAM', N'135 Nguyễn Thị Minh Khai, Q.1, TP.HCM', '1991-09-05', 'trungvo@gmail.com', '0905678901', '2022-01-01'),
 ('DG006', N'Đỗ', N'Ngọc', N'NỮ', N'56 Trương Định, Q.3, TP.HCM', '1993-03-12', 'ngocdo@gmail.com', '0906789012', '2022-01-01'),
 ('DG007', N'Hoàng', N'Dũng', N'NAM', N'89 Lý Thường Kiệt, Q.10, TP.HCM', '1989-11-25', 'dunghoang@gmail.com', '0907890123', '2022-01-01'),
 ('DG008', N'Trịnh', N'Tâm', N'NỮ', N'67 Võ Thị Sáu, Q.3, TP.HCM', '1987-06-18', 'tamtrinh@gmail.com', '0908901234', '2022-01-01'),
 ('DG009', N'Ngô', N'Tùng', N'NAM', N'23 Trần Phú, Q.5, TP.HCM', '1994-04-02', 'tungngo@gmail.com', '0909012345', '2022-01-01'),
 ('DG010', N'Đặng', N'Hằng', N'NỮ', N'178 Nguyễn Đình Chiểu, Q.3, TP.HCM', '1990-08-30', 'hangdang@gmail.com', '0900123456', '2022-01-01');
-- Bảng TheLoaiSach:
 INSERT INTO TheLoaiSach (MATHELOAI, TENTHELOAI) VALUES
 ('TL001', N'Văn học'),
 ('TL002', N'Kinh tế'),
 ('TL003', N'Khoa học'),
 ('TL004', N'Kỹ thuật'),
 ('TL005', N'Lịch sử'),
 ('TL006', N'Địa lý'),
 ('TL007', N'Tâm lý'),
 ('TL008', N'Triết học'),
 ('TL009', N'Tôn giáo'),
 ('TL010', N'Nghệ thuật');
-- Bảng TacGia:
 INSERT INTO TacGia (MATACGIA, HO, TEN, DIACHI, PHAI, EMAIL, NGAYSINH) VALUES
 ('TG001', N'Nguyễn', N'Tuân', N'123 Nguyễn Văn Cừ, Q.5, TP.HCM', N'NAM', 'nguyentuan@gmail.com', '1970-01-01'),
 ('TG002', N'Trần', N'Hân', N'45 Lê Văn Sỹ, Q.3, TP.HCM', N'NỮ', 'tranhang@gmail.com', '1975-05-10'),
 ('TG003', N'Lê', N'Minh', N'78 Trần Hưng Đạo, Q.1, TP.HCM', N'NAM', 'leminh@gmail.com', '1980-12-20'),
 ('TG004', N'Phạm', N'Hà', N'92 Phan Đăng Lưu, Q.Phú Nhuận, TP.HCM', N'NỮ', 'phamha@gmail.com', '1985-07-15'),
 ('TG005', N'Võ', N'Thắng', N'135 Nguyễn Thị Minh Khai, Q.1, TP.HCM', N'NAM', 'vothang@gmail.com', '1982-09-05'),
 ('TG006', N'Đỗ', N'Hương', N'56 Trương Định, Q.3, TP.HCM', N'NỮ', 'dohuong@gmail.com', '1987-03-12'),
 ('TG007', N'Hoàng', N'Hải', N'89 Lý Thường Kiệt, Q.10, TP.HCM', N'NAM', 'hoanghai@gmail.com', '1979-11-25'),
 ('TG008', N'Trịnh', N'Lan', N'67 Võ Thị Sáu, Q.3, TP.HCM', N'NỮ', 'trinhlan@gmail.com', '1983-06-18'),
 ('TG009', N'Ngô', N'Khoa', N'23 Trần Phú, Q.5, TP.HCM', N'NAM', 'ngokhoa@gmail.com', '1988-04-02'),
 ('TG010', N'Đặng', N'Ngân', N'178 Nguyễn Đình Chiểu, Q.3, TP.HCM', N'NỮ', 'dangngan@gmail.com', '1981-08-30');
-- Bảng NhaXuatBan:
 INSERT INTO NhaXuatBan (MANXB, TEN, DIACHI, SODIENTHOAI, EMAIL) VALUES
 ('NXB001', N'NXB Trẻ', N'161B Lý Chính Thắng, Q.3, TP.HCM', '0283931628', 'nxbtre@gmail.com'),
 ('NXB002', N'NXB Kim Đồng', N'55 Quang Trung, Hai Bà Trưng, Hà Nội', '0243943246', 'nxbkimdong@gmail.com'),
 ('NXB003', N'NXB Tổng hợp TP.HCM', N'62 Nguyễn Thị Minh Khai, Q.1, TP.HCM', '0283829364', 'tonghop@gmail.com'),
 ('NXB004', N'NXB Giáo dục Việt Nam', N'81 Trần Hưng Đạo, Hoàn Kiếm, Hà Nội', '0243942621', 'giaoduc@gmail.com'),
 ('NXB005', N'NXB Lao động', N'175 Giảng Võ, Đống Đa, Hà Nội', '0243851725', 'laodonghanoi@gmail.com'),
 ('NXB006', N'NXB Đại học Quốc gia TP.HCM', N'16 Linh Trung, Thủ Đức, TP.HCM', '0283897117', 'nxbdhqg@gmail.com'),
 ('NXB007', N'NXB Thông tin và Truyền thông', N'6 Nguyễn Công Hoan, Ba Đình, Hà Nội', '0243823213', 'thongtinvatt@gmail.com'),
 ('NXB008', N'NXB Chính trị Quốc gia Sự thật', N'6/86 Duy Tân, Cầu Giấy, Hà Nội', '0243726720', 'nxbctqg@gmail.com'),
 ('NXB009', N'NXB Hải Phòng', N'94 Đà Nẵng, Hải Phòng', '0313746731', 'nxbhaiphong@gmail.com'),
 ('NXB010', N'NXB Đà Nẵng', N'17 Lê Duẩn, Q.Hải Châu, TP.Đà Nẵng', '0236383979', 'nxbdanang@gmail.com');
-- Bảng DauSach:
 INSERT INTO DauSach (MADAUSACH, MATHELOAI, MANXB, TENSACH, SOTRANG, DONGIA, NAMXUATBAN, SOLUONGCUONSACH) VALUES
 ('DS001', 'TL001', 'NXB001', N'Tiếng chim hót trong bụi mận gai', 246, 60000, 2005, 50),
 ('DS002', 'TL002', 'NXB002', N'Kinh tế vi mô', 320, 75000, 2010, 30),
 ('DS003', 'TL003', 'NXB003', N'Vũ trụ trong vỏ hạt dẻ', 416, 120000, 2015, 20),
 ('DS004', 'TL004', 'NXB004', N'Kỹ thuật lập trình C++', 576, 90000, 2012, 40),
 ('DS005', 'TL005', 'NXB005', N'Lịch sử Việt Nam', 824, 180000, 2008, 25),
 ('DS006', 'TL006', 'NXB006', N'Địa lý thế giới', 315, 70000, 2018, 35),
 ('DS007', 'TL007', 'NXB007', N'Nhập môn tâm lý học', 280, 65000, 2016, 45),
 ('DS008', 'TL008', 'NXB008', N'Lịch sử triết học Trung Quốc', 712, 150000, 2009, 15),
 ('DS009', 'TL009', 'NXB009', N'Đạo Phật và đời sống', 192, 50000, 2014, 55),
 ('DS010', 'TL010', 'NXB010', N'Lịch sử nghệ thuật phương Tây', 640, 130000, 2007, 20);
-- Bảng SangTac:
 INSERT INTO SangTac (MATACGIA, MADAUSACH) VALUES
 ('TG001', 'DS001'),
 ('TG002', 'DS002'),
 ('TG003', 'DS003'),
 ('TG004', 'DS004'),
 ('TG005', 'DS005'),
 ('TG006', 'DS006'),
 ('TG007', 'DS007'),
 ('TG008', 'DS008'),
 ('TG009', 'DS009'),
 ('TG010', 'DS010');
-- Bảng KeSach:
 INSERT INTO KeSach (MAKE, SOTHUTUKE) VALUES
 ('KE01', 1),
 ('KE02', 2),
 ('KE03', 3),
 ('KE04', 4),
 ('KE05', 5),
 ('KE06', 6),
 ('KE07', 7),
 ('KE08', 8),
 ('KE09', 9),
 ('KE10', 10);
-- Bảng NganSach:
 INSERT INTO NganSach (MANGAN, MAKE, LOAIKHO, SOTHUTUNGAN) VALUES
 ('NG01', 'KE01', N'LỚN', 1),
 ('NG02', 'KE01', N'LỚN', 2),
 ('NG03', 'KE02', N'VỪA', 1),
 ('NG04', 'KE02', N'VỪA', 2),
 ('NG05', 'KE03', N'NHỎ', 1),
 ('NG06', 'KE03', N'NHỎ', 2),
 ('NG07', 'KE04', N'LỚN', 1),
 ('NG08', 'KE05', N'VỪA', 1),
 ('NG09', 'KE06', N'NHỎ', 1),
 ('NG10', 'KE07', N'LỚN', 1);
-- Bảng CuonSach:
 INSERT INTO CuonSach (MACUONSACH, MADAUSACH, MANGAN, KHOSACH, CHOMUONVE, TINHTRANG) VALUES
 ('CS001', 'DS001', 'NG01', N'LỚN', N'CÓ', N'CÒN'),
 ('CS002', 'DS002', 'NG02', N'LỚN', N'KHÔNG', N'ĐANG ĐƯỢC MƯỢN'),
 ('CS003', 'DS003', 'NG03', N'VỪA', N'KHÔNG', N'CÒN'),
 ('CS004', 'DS004', 'NG04', N'VỪA', N'CÓ', N'CÒN'),
 ('CS005', 'DS005', 'NG05', N'NHỎ', N'CÓ', N'ĐANG ĐƯỢC MƯỢN'),
 ('CS006', 'DS006', 'NG06', N'NHỎ', N'KHÔNG', N'ĐANG ĐƯỢC MƯỢN'),
 ('CS007', 'DS007', 'NG07', N'LỚN', N'KHÔNG', N'CÒN'),
 ('CS008', 'DS008', 'NG08', N'VỪA', N'CÓ', N'CÒN'),
 ('CS009', 'DS009', 'NG09', N'NHỎ', N'CÓ', N'ĐANG ĐƯỢC MƯỢN'),
 ('CS010', 'DS010', 'NG10', N'LỚN', N'KHÔNG', N'CÒN');
-- Bảng PhieuMuonSach:
 INSERT INTO PhieuMuonSach (MADOCGIA, MATHUTHUMUON, SOSACHMUON, NGAYMUON, NGAYDUKIENTRA) VALUES
 ('DG001', 'TT001', 1, '2023-01-01', '2023-01-08'),
 ('DG002', 'TT002', 2, '2023-02-10', '2023-02-20'),
 ('DG003', 'TT003', 3, '2023-03-15', '2023-03-22'),
 ('DG004', 'TT004', 2, '2023-04-20', '2023-04-27'),
 ('DG005', 'TT005', 1, '2023-05-25', '2023-06-01'),
 ('DG006', 'TT006', 3, '2023-06-30', '2023-07-07'),
 ('DG007', 'TT007', 1, '2023-07-05', '2023-07-12'),
 ('DG008', 'TT008', 2, '2023-08-10', '2023-08-17'),
 ('DG009', 'TT009', 1, '2023-09-15', '2023-09-22'),
 ('DG010', 'TT010', 2, '2023-10-20', '2023-10-27');
-- Bảng ChiTietPhieuMuon:
 INSERT INTO ChiTietPhieuMuon (MAPHIEUMUON, MACUONSACH, NGAYTRATHUCTE, NGAYGIAHAN, MATHUTHUTRA) VALUES
 (1, 'CS001', '2023-01-07', NULL, 'TT001'),
 (2, 'CS002', '2023-02-18', '2023-02-25', 'TT002'),
 (2, 'CS003', '2023-02-20', NULL, 'TT002'),
 (3, 'CS004', '2023-03-21', NULL, 'TT003'),
 (3, 'CS005', '2023-03-22', NULL, 'TT003'),
 (3, 'CS006', '2023-03-20', '2023-03-27', 'TT003'),
 (4, 'CS007', '2023-04-26', NULL, 'TT004'),
 (4, 'CS008', '2023-04-27', NULL, 'TT004'),
 (5, 'CS009', '2023-06-01', NULL, 'TT005'),
 (6, 'CS010', '2023-07-05', '2023-07-12', 'TT006'),
 (6, 'CS001', '2023-07-06', NULL, 'TT006'),
 (6, 'CS002', '2023-07-07', NULL, 'TT006');
-- Bảng PhieuNhapSach:
 INSERT INTO PhieuNhapSach (MATHUTHU, NGAYNHAP, TONGSOLUONG, TONGGIA) VALUES
 ('TT001', '2022-01-01', 20, 2000000),
 ('TT002', '2022-02-15', 15, 1500000),
 ('TT003', '2022-03-10', 25, 3000000),
 ('TT004', '2022-04-20', 18, 1800000),
 ('TT005', '2022-05-05', 30, 3500000),
 ('TT006', '2022-06-12', 22, 2200000),
 ('TT007', '2022-07-18', 16, 1600000),
 ('TT008', '2022-08-25', 28, 3200000),
 ('TT009', '2022-09-08', 12, 1200000),
 ('TT010', '2022-10-30', 20, 2500000);
-- Bảng ChiTietPhieuNhapSach:
 INSERT INTO ChiTietPhieuNhapSach (MAPHIEUNHAP, MADAUSACH, DONGIA, SOLUONG) VALUES
 (1, 'DS001', 100000, 5),
 (1, 'DS002', 120000, 3),
 (2, 'DS003', 90000, 4),
 (2, 'DS004', 110000, 2),
 (3, 'DS005', 130000, 6),
 (3, 'DS006', 100000, 4),
 (4, 'DS007', 80000, 3),
 (4, 'DS008', 140000, 2),
 (5, 'DS009', 150000, 7),
 (5, 'DS010', 100000, 5),
 (6, 'DS001', 100000, 4),
 (6, 'DS002', 120000, 3),
 (7, 'DS003', 90000, 3),
 (7, 'DS004', 110000, 2),
 (8, 'DS005', 130000, 5),
 (8, 'DS006', 100000, 4),
 (9, 'DS007', 80000, 2),
 (9, 'DS008', 140000, 1),
 (10, 'DS009', 150000, 4),
 (10, 'DS010', 100000, 3);
-- Bảng PhieuThanhLySach:
 INSERT INTO PhieuThanhLySach (MATHUTHU, MACUONSACH, LYDO, NGAYTHANHLY) VALUES
 ('TT001', 'CS001', N'Sách bị rách nhiều trang', '2023-01-01'),
 ('TT002', 'CS002', N'Sách bị mất trang', '2023-02-15'),
 ('TT003', 'CS003', N'Sách bị hư hỏng do độ ẩm', '2023-03-10'),
 ('TT004', 'CS004', N'Sách bị cũ nát', '2023-04-20'),
 ('TT005', 'CS005', N'Sách không còn phù hợp', '2023-05-05'),
 ('TT006', 'CS006', N'Sách bị rách nhiều trang', '2023-06-12'),
 ('TT007', 'CS007', N'Sách bị mất trang', '2023-07-18'),
 ('TT008', 'CS008', N'Sách bị hư hỏng do độ ẩm', '2023-08-25'),
 ('TT009', 'CS009', N'Sách bị cũ nát', '2023-09-08'),
 ('TT010', 'CS010', N'Sách không còn phù hợp', '2023-10-30');
-- Bảng PhiThanhVien:
 INSERT INTO PhiThanhVien (MAPHI, NAM, TIENPHI) VALUES
 (1, 2022, 100000),
 (2, 2022, 120000),
 (3, 2023, 150000),
 (4, 2023, 180000),
 (5, 2024, 200000),
 (6, 2024, 220000),
 (7, 2025, 250000),
 (8, 2025, 280000),
 (9, 2026, 300000),
 (10, 2026, 320000);
-- Bảng DongPhiThanhVien:
 INSERT INTO DongPhiThanhVien (MAPHI, MADOCGIA, NGAYDONG) VALUES
 (1, 'DG001', '2022-01-01'),
 (1, 'DG002', '2022-01-05'),
 (2, 'DG003', '2022-01-10'),
 (2, 'DG004', '2022-01-15'),
 (3, 'DG005', '2023-01-01'),
 (3, 'DG006', '2023-01-05'),
 (4, 'DG007', '2023-01-10'),
 (4, 'DG008', '2023-01-15'),
 (5, 'DG009', '2024-01-01'),
 (5, 'DG010', '2024-01-05');
-- Bảng PhiPhat:
 INSERT INTO PhiPhat (LOAIPHAT, MOTA, TIENPHAT) VALUES
 (N'Trả sách trễ hạn', N'Phí phạt khi trả sách trễ hạn', 10000),
 (N'Làm hỏng sách', N'Phí phạt khi làm hỏng sách', 50000),
 (N'Mất sách', N'Phí phạt khi làm mất sách', 100000);
-- -- Bảng DongPhiPhat:
 INSERT INTO DongPhiPhat (MAPHAT, MADOCGIA, NGAYPHAT, NGAYDONGPHAT, GHICHU) VALUES
 (1, 'DG001', '2023-01-10', '2023-01-15', N'Trả sách trễ 2 ngày'),
 (1, 'DG002', '2023-02-20', '2023-02-25', N'Trả sách trễ 1 ngày'),
 (2, 'DG003', '2023-03-22', '2023-03-27', N'Làm rách trang sách'),
 (2, 'DG004', '2023-04-28', '2023-05-03', N'Làm bẩn bìa sách'),
 (3, 'DG005', '2023-06-05', '2023-06-10', N'Làm mất sách'),
 (1, 'DG006', '2023-07-15', '2023-07-20', N'Trả sách trễ 3 ngày'),
 (2, 'DG007', '2023-08-20', '2023-08-25', N'Làm nhàu trang sách'),
 (1, 'DG008', '2023-09-25', '2023-09-30', N'Trả sách trễ 1 ngày'),
 (2, 'DG009', '2023-10-30', '2023-11-04', N'Gáy sách bị hỏng'),
 (1, 'DG010', '2023-12-05', '2023-12-10', N'Trả sách trễ 2 ngày');

