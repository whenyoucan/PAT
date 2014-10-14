stu_list = []
num_of_stu = int(raw_input())
for i in xrange(num_of_stu):
    stu_name, stu_id, stu_score = raw_input().split()
    stu_list.append({'name': stu_name, 'id': stu_id, 'score': int(stu_score)})
stu_list.sort(key=lambda stu: -stu['score'])
print stu_list[0]['name'], stu_list[0]['id']
print stu_list[-1]['name'], stu_list[-1]['id']