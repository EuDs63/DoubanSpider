import os
import json
import datetime
# 指定包含六个文件夹的大文件夹路径
base_folder = 'books'

# 创建一个空的JSON来存储所有JSON数据
all_data = {}
count = 1

# 遍历一级文件夹
for folder1 in os.listdir(base_folder):
    folder1_path = os.path.join(base_folder, folder1)

    # 确保是文件夹
    if os.path.isdir(folder1_path):

        # 遍历JSON文件
        for json_file in os.listdir(folder1_path):
            if json_file.endswith('.json'):
                json_file_path = os.path.join(folder1_path, json_file)

                # 逐行读取JSON文件内容并解析
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip().rstrip(',')
                        try:
                            json_data = json.loads(line)

                            # 添加文件夹信息
                            json_data['category'] = folder1
                            json_data['tag'] = json_file.strip('.json')

                            # 添加到总列表中
                            all_data[count] = json_data
                            count = count+1
                            #all_data.append(json_data)
                        except json.JSONDecodeError:
                            # 处理无效的JSON行
                            pass

# 将所有数据保存到一个新的JSON文件中
output_file = 'merge/merged.json'
# 输出的中文是url编码，暂未找到原因
# with open(output_file, 'w',encoding='utf-8') as f:
#     json.dump(all_data, f, indent=4)

# 获取当前日期和时间
current_datetime = datetime.datetime.now()

# 格式化日期和时间为字符串，例如：09-02_12-34
formatted_datetime = current_datetime.strftime("%m-%d_%H-%M")
file_name = f"douban_{formatted_datetime}.json"
file_path = "merge/{}".format(file_name)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(all_data, ensure_ascii=False) + ',\n')# 需手动去除最后一行


print(f'合并完成，结果已保存到 {file_path}')
