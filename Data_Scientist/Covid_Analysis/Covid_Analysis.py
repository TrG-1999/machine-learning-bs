#!/usr/bin/env python
# coding: utf-8
# # Covid_Analysis
# ## Phân tích dữ liệu khi đã có dữ liệu xạch sau khi lọc.
# >- Function sys.patch.append() thêm vào khi ta có thư mục chứa các module riêng.
# >- Dưới đây ta sử dụng chủ yếu 3 module numpy, pandas và matplotlib
import sys
sys.path.append("c:/users/root/appdata/local/programs/python/python38-32/lib/site-packages")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# > -Chúng ta sẽ kiểm tra bảng dữ liệu này gồm có các trường nào.
df = pd.read_csv('covid_19_data.csv')
df.head(20)

# > +Chúng ta sẽ bỏ cột SNo và Last Update trong bảng dữ liệu, sau đó đổi tên 3 cột rồi chuyển đổi cột Date về thời gian hệ thống. 
# > +Trong phần này ta sử dụng hàm SimpleImputer() của sklearn để sử lý những dữ liệu thiếu sót (NaN/Null), hoạc có 1 cách khác nữa là nếu ta sử dụng DataFrame thì ta có thể sử dụng hàm fillna() của Pandas để lọc dữ liệu thiếu sót.
# > +Sau đó Nhóm các dữ liệu có chung 1 Quốc gia và ngày thông báo lại với nhau, những cột có dữ liệu số sẽ được tính tổng lại theo nhóm, riêng cột Tỉnh thành sẽ không được cộng lại theo nhóm và bị loại bỏ.

df.drop(['SNo','Last Update'],axis=1,inplace=True)
df.rename(columns = {'ObservationDate':'Date','Province/State':'State','Country/Region':'Country'},inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
df3 = df2.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum().reset_index()
df3.head(20)

# > Hàm unique() giúp ta lọc ra list những quốc gia có trong bảng dữ liệu và đặc biệt tên quốc gia trong list này sẽ không bị chùng lập với nhau.

countries = df3['Country'].unique()
len(countries)

# >- Dòng lệnh dưới sẽ giúp ta vẽ biểu đồ số ca (xác nhận, chữa khỏi, chết) trải qua theo từng ngày. Chúng ta có thể chạy biểu đồ hết 226 quốc gia, nhưng như vậy thì hơi dài nên ta lấy mẫu 15 quốc gia (range  0->15).
# >- Ta thấy 2 quốc gia đầu tiên(Azerbaijan, ST. Martin) có số ngày là số thập phân là vì những quốc gia này không được cập nhật dữ liệu thường xuyên theo dõi những trường hợp Covid, chính xác hơn thì nó mới chỉ khi nhận trong 1 ngày hoạc là trường hợp thu thập dữ liệu này nó bị lỗi.
# >- Dưới những đồ thị ta biết được rẵng những quốc gia nào có đường màu xanh nước biển tách rời(không đi sát nhau) đường màu xanh lá cây thì rõ ràng 1 điều là những quốc gia đó khắc phục, chữa trị Covid chưa tốt(có thể là do cơ sở vật chất, y tế các quốc gia đó không tốt). Với các quốc gia có đường nét đứt màu xanh lá cây thì ta biết là quốc gia đó chữa chị bệnh khá lâu nên mới không có cập nhật dữ liệu bình phục thường xuyên.
# >- Những đường xanh nước biển càng dốc cho thấy là quốc gia đó đang trong giai đoạn bùng phát mạnh, nhưng nếu 2 đường màu xanh đi sát nhau và tách xa đường màu đỏ thì quốc gia đó mạnh trong việc ngăn ngừa bùng phát và quốc gia đó cũng đáng an tâm.

#range(0,len(countries))
for idx in range(0,15):
    C = df3[df3['Country']==countries[idx]].reset_index()
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()

# >- Chúng ta có thể xem trực tiếp của quốc gia Mỹ và Việt Nam xem và so sánh nó như thế nào.
#Graph of US
C = df3[df3['Country']=='US'].reset_index()
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('US')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()
#Graph of Vietnam
C = df3[df3['Country']=='Vietnam'].reset_index()
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('Vietnam')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()

# >- Ta sẽ xem biểu đồ các trường hợp theo ngày của cả thế giới hiện nay sẽ như thế nào

df4 = df3.groupby(['Date'])[['Date','Confirmed','Deaths','Recovered']].sum().reset_index()
C = df4
print(C)
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('World')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.ticklabel_format(useOffset=False, style='plain') # unlimit number of axist ex: 1e8
plt.show()