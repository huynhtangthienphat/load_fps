import csv
import json
import os
from collections import OrderedDict
folder = 'test' # thư mục chứa file json 
map_folder='map'

output_csv='fps.csv'
def get_fps():
    with open(output_csv,'w',newline='') as csv_file:
        csv_write=csv.writer(csv_file)

        csv_write.writerow(['Ten file','FPS'])
        for filename in os.listdir(map_folder):
            if filename.endswith('.csv'):
                # ket noi ten thu muc voi file csv 
                csv_file = os.path.join(map_folder,filename)
                with open(csv_file,'r') as r:
                    read_csv=csv.reader(r)
                    header=next(read_csv)
                    cot_fps=header.index('fps')
                    
                    # lay 1 fps cua 1 file csv 
                    for row in read_csv:
                        # lay fps cua cot fps 
                        fps_value=row[cot_fps]
                        
                        break
                file_name = os.path.splitext(filename)[0]
                csv_write.writerow([file_name,fps_value])

def load_file():
    # Tạo một empty dictionary để lưu giá trị FPS
    fps_data = {}

    # Đọc tệp CSV và thêm dữ liệu vào dictionary
    with open('fps.csv', newline='') as csvfile:
        read_csv = csv.reader(csvfile)
        next(read_csv)  # Bỏ qua dòng tiêu đề
        for row in read_csv:
            ten_file, fps = row
            fps_data[ten_file] = int(float(fps))  # Chuyển đổi FPS thành kiểu số thực
        #print(fps_data)

    # Lặp qua các tệp JSON và ghi dữ liệu FPS vào tệp JSON tương ứng
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            json_data = os.path.join(folder, filename)
            
            with open(json_data, 'r', encoding='utf-8') as r:
                data = json.load(r, object_pairs_hook=OrderedDict)
                
                # Lấy tên tệp JSON từ tên file
                json_name = os.path.splitext(filename)[0]
                
                # Kiểm tra xem có dữ liệu FPS tương ứng trong dictionary không
                if json_name in fps_data:
                    data['FPS'] = fps_data[json_name]
                else:
                    print(f"Không tìm thấy FPS cho tệp JSON {json_name}")
                
                with open(json_data, 'w', encoding='utf-8') as w:
                    json.dump(data, w, ensure_ascii=False, indent=4)

if __name__=='__main__':
    get_fps()
    load_file()
