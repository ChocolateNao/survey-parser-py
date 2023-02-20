# # hd = get_header_data()
# # for h in hd:
# #     if h[0] is not None:
# #         print(h)
#
# # print(get_subjects())
# data = get_header_data()
#
#
# def get_ognp_dict(data: list[list]):
#     ognp_list = []
#     for item in data:
#         regex = regex_find_ognp(item[0])
#         if regex is not None:
#             ognp_list.append(item)
#     pattern = r'\((.*?)\)'  # pattern to match text inside parentheses
#
#     result = {}
#     for item in ognp_list:
#         match = re.search(pattern, item[0])
#         key = item
#         value = [item[0], item[1]]
#         result[re.findall(pattern, key[0])].append
#
#     print(result)
#     return result
#
#
# print(get_ognp_dict(data))
# # header_data = get_header_data()
# # teachers_data = get_teachers()
# # teacher_dict = get_dictionary_by_teacher(header_data, teachers_data)
# # print(teacher_dict)
#
#
# get_ognp_dict(data)