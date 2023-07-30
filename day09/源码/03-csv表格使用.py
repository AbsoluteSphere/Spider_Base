
import csv

# with open('data.csv', 'w')as f:
#     f.write('{},{},{}'.format('名字', '年龄', '性别'))
#     f.write('\n')
#     f.write('{},{},{}'.format('柏汌', '19', '男'))
#     f.write('\n')
#     f.write('{},{},{}'.format('安娜', '28', '女'))
#     f.write('\n')
#     f.write('{},{},{}'.format('双双', '32', '女'))

# 列表的写入方法
# with open('data.csv', 'w', newline='')as f:
#     csv_f = csv.writer(f)
#     csv_f.writerow(['姓名', '年龄', '性别'])
#     csv_f.writerows([['柏汌', '18', '男'], ['安娜', '48', '未知'], ['安娜', '48', '未知']])
    # csv_f.writerow()


# 字典写入方法
with open('data1.csv', 'w', newline='', encoding='utf-8') as f:
    file_name = ['id', 'name', 'age']
    csv_f = csv.DictWriter(f, fieldnames=file_name)
    csv_f.writerow({'id': '001', 'name':'baic', 'age': '18'})
    csv_f.writerow({'id': '002', 'name':'111', 'age': '19'})