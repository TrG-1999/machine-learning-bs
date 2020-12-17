# Data-Scientist-bs
 Data Scientist
## [1.Get Data and Analysis Data of DIEM_THPTQG_2020 ](https://github.com/TrG-1999/machine-learning-bs/tree/master/Data_Scientist/DIEM_THI_THPTQG_2020)
>Truy cập website tra cứu điểm thi THPT QG năm 2020.
![Image of game char](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/1.PNG)

>Kiểm tra đường dẫn đến tra cứu thông tin [Link HTTP POST]
![Image of game char](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/2.PNG)

>Xác định các Tag để có thể crawl dữ liệu từ những đối tượng Tag này.
![Image of game char](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/3.PNG)

>File dữ liệu sạch sau khi Crawl [source file csv DIEM_THPTQG_2020](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/kqthi_thptqg_2020.csv)
### [ Cách 1: Lấy dữ liệu từ server rồi làm sạch luôn (source code)](![Image of game char](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/crawl_Data_cleaning_2020.py)
>Cách này phù hợp cho những dữ liệu ít, nếu với dữ liệu nhiều mà dán đoạn thì mất hết công sức ngồi crawl. Lợi của cách này là lấy dữ liệu sạch một nhanh chóng và ít tốn bộ nhớ dữ liệu.

### [ Cách 2: Lấy dữ liệu dạng Raw rồi sau đó mới làm sạch dữ liệu]
>Phù hợp với những dạng dữ liệu nhiều. Phải làm nhiều công đoạn, khá tốn bộ nhớ nhưng được cái là ăn chắc từng bộ dữ liệu.
>Lấy dữ liệu thô.
[ Source code Get data Raw](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/get_raw_data_thptqg_2020.py)

>Lấy dữ liệu sạch từ dữ liệu thô.
[ Source code Get data Raw](https://github.com/TrG-1999/machine-learning-bs/blob/master/Data_Scientist/DIEM_THI_THPTQG_2020/get_clean_data_thptqg_2020.py)
