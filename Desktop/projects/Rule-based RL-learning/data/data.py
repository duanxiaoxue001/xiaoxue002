INF = float('inf')
def final_matrix(a, b, c):
    computation_time_matrix=[]
    communication_time_matrix=[]
    OR = []

    computation_time_matrix = a

    print(computation_time_matrix)

    task_number=0  # 任务总数
    task_number_list = []   # 存储每个子列表中任务的累计数量
    for i in b:
        task_number += len(i)
        task_number_list.append(task_number)
    task_number_list1 = [0]+task_number_list

    for j in range(len(b)):
        for l in b[j]:
            temp=[]
            for p in range(task_number_list1[j]):
                temp.append(INF)
            temp+=l
            for q in range(task_number_list1[j+1],task_number):
                temp.append(INF)
            communication_time_matrix.append(temp)
    print(communication_time_matrix)


    for i, sublist in enumerate(c):
        for tup in sublist:
            tuple_sublist = tup
            v = task_number_list1[i]
            updated_tuple = tuple(elem + v if isinstance(elem, int) else elem for elem in tuple_sublist)
            OR.append(updated_tuple)
    print(OR)
    print("\n")
    return computation_time_matrix, communication_time_matrix, OR


""" job1-n """
computation_time_matrix1 = [{3: 16.7, 6: 14.1, 8: 25.6}, {12: 20.8, 14: 18.9}, {4: 30.1, 5: 41.5, 7: 18.9},
                            {2: 21.5, 6: 12.6, 8: 40.1}, {9: 13.1}, {12: 7.9}, {4: 31.4, 6: 61.2},
                            {5: 9.1, 7: 13.5}]
communication_time_matrix1 = [
                               [INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR1 = []

""" job2-n """
computation_time_matrix2 = [{1: 16.2, 3: 18.4, 5: 27.3}, {5: 14.3, 7: 16.1}, {2: 41.3, 4: 36.2},
                            {10: 11.7, 11: 15.8, 12: 21.3}, {6: 31.2, 8: 25.4, 13: 31.6}, {3: 8.9, 5: 11.6}]
communication_time_matrix2 = [
                              [INF, 0, INF, 0, 0, INF],
                              [INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF]
                              ]
OR2 = []

"""job3-n """
computation_time_matrix3 = [{2: 21.3, 5: 35.6, 6: 17.8}, {3: 6.7, 7: 12.3, 9: 17.8}, {11: 36.7, 14: 41.2},
                            {13: 21.8, 14: 14.6, 15: 11.9}, {6: 14.5, 7: 16.7}, {8: 51.4, 9: 47.8, 12: 12.8},
                            {3: 6.8, 4: 13.6}, {1: 19.9, 5: 25.6, 9: 21.2, 14: 30.7}, {4: 26.7, 6: 45.5},
                            {8: 21.8, 9: 19.9, 14: 34.7}, {11: 26.3, 13: 18.1, 14: 31.4, 15: 16.2}, {1: 9.1, 6: 14.5, 8: 19.6},
                            {2: 16.8, 3: 24.5}, {3: 28.9, 6: 18.4, 9: 19.7, 11: 23.5}]
communication_time_matrix3 = [
                               [INF, 0, 0, INF, INF, 0, INF, 0, INF, INF, 0, 0, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                             ]
OR3 = [(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)]


""" job4-n """
computation_time_matrix4 = [{5: 32.1}, {12: 15.3, 15: 18.9}, {1: 14.6, 6: 15.7, 9: 16.9},
                            {2: 21.4, 6: 18.8, 8: 12.4}, {1: 14.6, 12: 18.7, 14: 19.2}, {1: 8.9, 5: 14.7, 8: 16.7, 9: 12.3, 12: 19.5},
                            {3: 16.2, 6: 12.9, 8: 19.4}, {4: 24.6, 7: 28.9, 10: 15.1}, {4: 41.3, 8: 26.9},
                            {5: 50.7, 9: 44.6, 11: 51.1, 14: 29.9}]
communication_time_matrix4 = [
                              [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, 0, 0, INF, 0, INF, 0, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR4 = [(3, 4, 5, 6, 7, 8, 9, 10)]

""" job5-1 ??? """
computation_time_matrix5 = [
        {3: 35, 4: 29, 5: 36, 11: 31}, {1: 40, 3: 34, 5: 44, 10: 41, 15: 39}, {11: 15, 15: 13}, {2: 31, 6: 33, 7: 29, 10: 27, 14: 25},
        {6: 13, 12: 9, 13: 8, 14: 14}, {11: 28, 12: 29}, {2: 31, 4: 24, 10: 28, 12: 26, 14: 32}, {6: 34, 10: 33, 11: 30, 13: 29},
        {3: 41, 4: 37, 13: 40}, {1: 38, 4: 29, 5: 35, 8: 30, 9: 31}, {6: 48, 10: 50, 11: 44, 14: 41, 15: 47},
        {6: 26, 7: 32, 9: 38, 12: 29, 13: 30}, {6: 23, 10: 20, 13: 25, 14: 18, 15: 22}, {2: 14, 8: 11, 10: 17, 12:13},
        {3: 27, 5: 24, 13: 26}, {4: 20, 8: 19, 13: 14}, {2: 27, 3: 21, 4: 28, 7: 30, 14: 29}, {3: 39, 7: 34, 10: 40, 14: 35}
    ]
communication_time_matrix5 = [
        [INF,   0, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF,   0, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR5 = [(2, 3, 9, 10, 11, 12, 13), (4, 5, 6, 7, 8)]

# computation_time_matrix5 = [{2: 13.4, 9: 16.6}, {12: 21.4, 14: 36.7, 15: 51.2}, {3: 21.6, 5: 27.1, 7: 33.2},
#                             {1: 5.9, 9: 16.2, 10: 18.9, 12: 20.3}, {4: 18.1, 5: 14.6}, {6: 23.4, 8: 31.2, 9: 16.8, 13: 14.7},
#                             {3: 16.7, 6: 19.9, 8: 9.8}, {11: 21.3, 13: 15.1, 15: 31.7}, {2: 25.6, 6: 12.8, 10: 31.1},
#                             {6: 17.9, 10: 19.2, 13: 21.6}, {1: 31.6, 9: 26.8}],
# communication_time_matrix5 = [
#                               [INF, 0, INF, INF, 0, 0, INF, 0, 0, 0, INF],
#                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
#                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                               ],
# in_OR5 = [(2, 3, 4, 5, 6, 7), (8, 9)],
# OR5 = {((2, 3, 4), (5, ), (6, 7)), ((8, ), (9, ))}

""" job6-n """
computation_time_matrix6 = [{12: 31.2, 14: 26.7, 15: 15.8}, {3: 6.8, 13: 14.5}, {2: 12.4, 8: 16.7, 12: 8.9, 14: 24.5},
                            {4: 16.7, 7: 13.2, 8: 26.5}, {1: 25.6, 5: 18.9, 9: 31.5}, {9: 19.9, 12: 11.1, 15: 22.3},
                            {6: 41.2, 13: 32.5}, {5: 16.3, 8: 17.1, 12: 26.2}, {10: 16.8, 13: 18.9, 15: 25.6},
                            {2: 21.4, 4: 19.1, 6: 30.4, 8: 17.6}]
communication_time_matrix6 = [[INF, 0, 0, INF, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              ]
OR6 = [(2, 3, 4, 5), (7, 8, 9, 10)]

""" job7-n """
computation_time_matrix7 = [{4: 13.6, 7: 17.8}, {13: 20.1, 14: 18.9, 15: 19.9}, {3: 18.3, 6: 16.5, 7: 30.1, 8: 28.6},
                            {2: 8.9, 12: 15.6, 14: 11.4}, {1: 6.7, 9: 11.3, 11: 14.5, 15: 27.1}, {3: 34.5, 5: 41.2, 7: 21.7},
                            {1: 17.3, 9: 13.4, 10: 17.8, 11: 14.5}, {10: 23.5, 11: 26.7, 13: 19.8}, {4: 14.5, 6: 12.3, 7: 18.6},
                            {2: 24.5, 8: 18.9}, {1: 51.2, 7: 31.4, 12: 30.1, 15: 29.4}]
communication_time_matrix7 = [[INF, 0, INF, INF, 0, 0, INF, 0, INF, INF, 0],
                              [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR7 = [(2, 5, 6, 7, 8, 11)]

""" job8-n """
computation_time_matrix8 = [{5: 31.5, 13: 52.6}, {6: 36.7, 7: 37.8, 9: 31.9}, {1: 41.3, 3: 46.7, 8: 38.9},
                            {11: 16.7, 14: 18.9}, {2: 25.6, 6: 22.8, 8: 16.5}, {6: 37.8, 9: 40.1, 12: 35.6},
                            {12: 18.9, 14: 15.6}, {1: 31.6, 3: 37.8, 6: 40.3, 7: 29.6, 9: 26.8}, {12: 18.3, 13: 19.2},
                            {4: 26.7, 10: 21.9, 13: 30.7}]
communication_time_matrix8 = [[INF, 0, INF, INF, INF, 0, INF, 0, INF, INF],
                              [INF, INF, 0, 0, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR8 = [(3, 4, 5)]

""" job9-n """
computation_time_matrix9 = [{6: 32.6, 7: 27.8, 8: 24.3}, {1: 15.6, 4: 25.6, 6: 29.8, 9: 30.1}, {2: 31.2, 7: 36.7, 10: 38.9, 11: 40.2},
                            {5: 18.9, 7: 21.4, 13: 19.2, 14: 23.6}, {11: 13.4, 13: 16.7, 15: 20.1}, {6: 25.6, 7: 24.1, 8: 27.8, 9: 19.9},
                            {8: 15.6, 9: 6.7, 11: 18.3}, {6: 23.4, 7: 27.8, 8: 25.3, 9: 28.9}, {11: 21.4, 14: 28.3, 15: 23.7},
                            {12: 31.4, 13: 36.2}, {3: 26.7, 6: 28.9, 14: 30.1}, {2: 12.3, 7: 9.9, 9: 11.4},
                            {5: 25.6, 15: 24.3}]
communication_time_matrix9 = [[INF, 0, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              ]
OR9 = [(2, 3, 4), (9, 10), (12, 13)]

""" job10-n """
computation_time_matrix10 = [{7: 7.9}, {12: 24.5, 14: 21.6, 15: 25.6}, {3: 21.4, 8: 26.7, 12: 29.1},
                             {5: 12.3, 7: 9.8, 9: 11.6, 11: 16.4}, {1: 31.3, 6: 35.6, 13: 38.9, 15: 40.5}, {2: 14.5, 4: 16.7, 8: 15.3, 10: 19.4},
                             {4: 25.6, 6: 21.3, 8: 27.8}, {11: 41.2, 12: 46.7, 13: 49.5, 14: 50.1, 15: 47.4}, {2: 25.6, 3: 21.3, 4: 27.8},
                             {5: 31.2, 10: 28.9, 14: 34.6}, {11: 21.3, 13: 19.4, 15: 18.9}, {2: 17.8, 6: 12.3},
                             {7: 25.6, 8: 17.8, 10: 26.7}, {2: 35.6, 14: 30.2, 15: 41.1}, {3: 14.5, 5: 17.8, 7: 23.6, 9: 25.6, 10: 19.3}]
communication_time_matrix10 = [[INF, 0, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                               ]
OR10 = [(2, 3, 4, 5, 6, 7, 8, 9, 10)]

""" job11-n """
computation_time_matrix11 = [{8: 35.6, 10: 38.9, 12: 30.1}, {2: 26.7, 6: 31.2, 8: 28.9, 9: 19.8, 10: 21.4}, {13: 21.3, 14: 26.7, 15: 31.2},
                             {2: 15.6, 13: 19.8}, {1: 24.5, 6: 21.8, 15: 31.2}, {3: 17.8, 12: 23.4, 13: 25.3},
                             {5: 25.6, 9: 27.8, 10: 29.9, 12: 20.1}, {4: 17.9, 14: 14.5, 15: 18.4}, {5: 34.4, 9: 42.1},
                             {11: 18.9, 15: 26.7}, {2: 24.5, 6: 31.2, 7: 27.6, 8: 28.9}, {9: 18.9, 11: 23.4, 12: 17.8, 13: 28.9, 15: 30.2}]
communication_time_matrix11 = [[INF, 0, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]]
OR11 = [(9, 10, 11, 12)]

""" job12-n """
computation_time_matrix12 = [{3: 21.3, 6: 35.6, 8: 17.8, 13: 18.3}, {1: 6.7, 8: 12.3}, {4: 36.7, 6: 41.2, 14: 32.1, 15: 41.2},
                             {13: 21.8, 14: 14.6, 15: 11.9}, {7: 14.5, 8: 16.7, 9: 25.6, 10: 12.7}, {3: 51.4, 6: 47.8},
                             {12: 6.8, 15: 13.6}, {1: 19.9, 7: 25.6, 9: 21.2}, {4: 26.7, 8: 45.5, 10: 21.5},
                             {6: 19.9, 8: 34.7}, {1: 26.3, 7: 18.1, 14: 31.4}, {2: 9.1, 5: 14.5, 15: 19.6},
                             {1: 16.8, 6: 24.5}, {1: 21.5, 8: 34.5, 13: 20.4}, {5: 28.9, 8: 18.4, 11: 19.7, 13: 23.5}]
communication_time_matrix12 = [
                               [INF, 0, INF, INF, INF, 0, INF, INF, 0, INF, INF, INF, 0, 0, INF],
                               [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                             ]
OR12 = [(2, 6, 7, 8, 9, 13, 14, 15)]


""" job1-1 """
computation_time_matrix13 = [{9: 13, 14: 10}, {11: 24, 15: 18}, {15: 43},
                            {12: 43},  {13: 30}, {4: 32, 12: 25},
                            {1: 40, 5: 49, 11: 39}, {8: 47}]
communication_time_matrix13 = [
                               [INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, 0, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, 0, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR13 = []

""" job2-1 """
computation_time_matrix14 = [{5: 10, 8: 16, 14: 13}, {8: 6, 9: 8, 15: 7}, {4: 40},
                            {6: 14, 9: 10, 7: 20, 12: 13},  {1: 33, 7: 40, 11: 43}, {1: 42, 5: 38},
                            {6: 25, 11: 33, 15: 30}, {10: 41, 15: 44}, {2: 10, 13: 12},
                            {11: 34, 14: 24, 15: 30}, {6: 38, 11: 42}, {4: 25, 8: 26, 12: 30},
                            {7: 39}, {10: 37, 12: 40}]
communication_time_matrix14 = [
                               [INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, 0, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR14 = [(9, 10, 11, 12, 13)]

"job3-1"
computation_time_matrix15 = [{4: 29, 7: 36, 11: 34}, {2: 35, 8: 29, 11: 27, 12: 30, 15: 33}, {1: 11, 6: 9, 7: 8, 10: 19, 14: 12},
                            {2: 18, 3: 20, 6: 27, 7: 13},  {2: 19, 3: 24, 4: 22, 5: 31, 7: 37}, {1: 13, 7: 8, 10: 12, 12: 9, 13: 5},
                            {1: 50, 5: 39, 6: 44, 13: 48}, {1: 6, 12: 9}, {3: 44, 4: 36, 5: 30, 13: 39, 14: 33},
                            {3: 39, 4: 45, 7: 41, 12: 50, 13: 40}, {2: 29, 4: 36, 9: 33}, {1: 19, 4: 20, 9: 17, 12: 16, 14: 21},
                            {9: 40, 14: 33, 15: 35}, {2: 11, 4: 12, 6: 14, 7: 15}, {1: 10, 8: 19, 12: 20, 13: 17, 14: 16}, {10: 49, 15: 44},
                            {10: 20, 12: 33, 13: 39}, {6: 30, 7: 29, 9: 40, 10: 39, 13: 33}, {3: 20, 8: 29, 10: 40, 14: 34, 15: 31}]
communication_time_matrix15 =  [
                                [INF, 0, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                                [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                            ]
OR15 = []

""" job4-1 """
computation_time_matrix16= [{2: 18}, {8: 38, 12: 30}, {9: 20},
                            {5: 8, 11: 9},  {3: 29}, {2: 36, 4: 33, 5: 39},
                            {1: 23, 10: 20}, {6: 45}, {3: 5, 12: 9},
                            {5: 39, 9: 33}, {7: 36, 11: 41}, {14: 31, 15: 29},
                            {1: 28, 2: 22, 6: 21}, {10: 18, 14: 28}, {12: 24}, {7: 23, 9: 25}]
communication_time_matrix16 = [
                               [INF, 0, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
OR16 = [(2, 3, 4, 5, 6), (14, 15)]

"job5-1"
computation_time_matrix17 = [
        {3: 35, 4: 29, 5: 36, 11: 31}, {1: 40, 3: 34, 5: 44, 10: 41, 15: 39}, {11: 15, 15: 13}, {2: 31, 6: 33, 7: 29, 10: 27, 14: 25},
        {6: 13, 12: 9, 13: 8, 14: 14}, {11: 28, 12: 29}, {2: 31, 4: 24, 10: 28, 12: 26, 14: 32}, {6: 34, 10: 33, 11: 30, 13: 29},
        {3: 41, 4: 37, 13: 40}, {1: 38, 4: 29, 5: 35, 8: 30, 9: 31}, {6: 48, 10: 50, 11: 44, 14: 41, 15: 47},
        {6: 26, 7: 32, 9: 38, 12: 29, 13: 30}, {6: 23, 10: 20, 13: 25, 14: 18, 15: 22}, {2: 14, 8: 11, 10: 17, 12:13},
        {3: 27, 5: 24, 13: 26}, {4: 20, 8: 19, 13: 14}, {2: 27, 3: 21, 4: 28, 7: 30, 14: 29}, {3: 39, 7: 34, 10: 40, 14: 35}
    ]
communication_time_matrix17 = [
        [INF,   0, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF,   0, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR17 = [(2, 3, 9, 10, 11, 12, 13), (4, 5, 6, 7, 8)]

"job6-1"
computation_time_matrix18 = [
        {3: 38, 4: 33, 11: 36}, {2: 22, 3: 21, 6: 19}, {5: 14}, {5: 17, 8: 20}, {3: 36, 6: 33, 11: 39},
        {2: 24, 3: 20, 10: 18}, {3: 21, 9: 17, 15: 24}, {8: 38}, {4: 19, 11: 15}, {8: 14, 10: 19, 15: 17},
        {1: 25, 4: 21, 9: 19, 13: 28}, {7: 42, 12: 43}, {1: 48, 2: 42, 6: 46}, {7: 10, 10: 14},
        {2: 14, 13: 16, 14: 13}, {1: 36, 4: 33, 5: 31, 8: 34}, {1: 47, 12: 44}, {9: 30, 10: 26, 13: 29},
        {1: 18, 5: 19, 12: 15}, {9:24, 11:25}
    ]
communication_time_matrix18 = [
        [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR18 = [(6, 7, 9, 11, 12, 13), (8, 10)]

"job7-1"
computation_time_matrix19 = [
        {7: 12, 8: 17}, {2: 7, 5: 6, 8: 8, 12: 11}, {11: 30, 15: 27}, {7: 27}, {2: 10, 3: 11, 9: 16},
        {4: 46, 11: 50, 13: 49}, {3: 22}, {10: 10, 5: 9}, {1: 27, 2: 28, 6: 24}, {6: 8, 12: 5, 13: 11},
        {2: 47, 9: 48}, {1: 27, 8: 30}, {9: 18, 13: 19, 14: 20}, {7: 22, 11: 20},
        {7: 13, 8: 11, 13: 14}, {6: 15, 14: 10}, {4: 21, 5: 26, 7: 20}, {4: 29, 5: 30, 13: 26},
        {1: 35, 2: 31}, {5: 22, 6: 18, 11: 23}, {1: 32, 7: 33, 10: 28}
    ]
communication_time_matrix19 = [
        [INF, 0, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR19 = [(2, 6, 7, 8, 9), (3, 4, 5), (12, 13, 14, 17), (15, 16)]

"""job8-1"""
computation_time_matrix20 = [
        {4: 50}, {8: 23, 15: 21}, {12: 35}, {4: 11, 8: 16, 7: 13}, {2: 18, 11: 20},
        {4: 36, 13: 33}, {1: 38, 3: 35}, {6: 16, 15: 17}, {9: 24}, {5: 23, 14: 26},
        {1: 15, 5: 16, 8: 17}, {3: 43, 10: 49}, {10: 44}, {13: 32, 14: 31},
        {10: 36, 13: 38}, {14: 28}, {2: 39, 10: 34}, {5: 18, 7: 15}, {11: 16}, {3: 45, 12: 48}
    ]
communication_time_matrix20 = [
        [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR20=[(2, 3, 7, 8, 11, 12, 16), (18, 19), (4, 5, 6), (9, 10)]

"""job9-1"""
computation_time_matrix21 = [
        {5: 31, 9:27, 12:21, 13:28, 14:23}, {7: 21}, {7: 21, 9:22, 10:25, 13:20}, {3: 13, 15: 15},
        {3: 6, 6:5, 9:7, 12:10, 13:9}, {1: 37, 2:33, 5:39, 6:29, 10:32}, {4: 7, 10:8, 11:9, 13:5, 15:6},
        {1: 42, 4:41, 8:39, 9:45, 12:44}, {4: 10, 7:9, 14:14}, {4: 19, 5:14, 7:15, 8:12, 14:10},
        {3: 28, 9:24, 10:27, 11:22, 15:20}, {4: 45, 6: 41}, {2: 44}, {4: 47, 5:43, 14:44, 15:42},
        {2: 17, 5:14, 6:20, 9:21, 14:18}, {2: 45, 4:42, 13:46}, {1: 27, 3:25, 5:23, 6:28, 15:20},
        {2: 10, 7:12, 9:17, 10:16, 11:11}, {2: 9,13:10}, {4: 18, 6:23, 8:21, 12:25}
    ]
communication_time_matrix21 = [
        [INF, 0, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR21 =[(3, 4, 5), (8, 9, 10), (17, 18, 19)]

"""job10-1"""
computation_time_matrix22 = [
        {1: 34, 2: 39, 3: 40, 4:33}, {6: 27, 15: 20}, {1: 22, 13:24}, {10: 22, 13: 20}, {4: 37, 7: 35},
        {5: 10, 9: 12}, {8: 39, 12: 32, 14: 36}, {12: 44}, {2: 23, 3: 24, 6:21, 9:19}, {3: 48, 12: 45},
        {14: 17}
    ]
communication_time_matrix22 = [
        [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR22 =[(4, 5, 6, 7, 8)]

"""job11-1"""
computation_time_matrix23 = [
        {1: 38, 6: 30}, {5: 39, 8: 40, 14:36, 15:44}, {3:11,5:13,11:9,12:12,13:8}, {5:21,6:23,8:29,13:27,14:25},
        {3:33,4:31,6: 29}, {2: 28, 10: 27}, {1: 40, 14: 42, 15: 46}, {2:6,7:8,9:10,11:11,14:7}, {5: 40, 9:39, 13:36}
    ]
communication_time_matrix23 = [
        [INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR23 = []

"""job12-1"""
computation_time_matrix24 = [
    {1: 31, 11: 29}, {8: 46, 15: 44}, {5: 5, 11: 11}, {12: 41}, {15: 24}, {2: 42, 13: 45},
    {8: 19, 11: 15}, {3: 18, 12: 20}, {6: 5, 14: 7}, {4: 18}, {7: 39}, {6: 13, 10: 7},
    {2: 26, 3: 22}, {1: 5, 8: 8, 13: 9}, {9: 39}, {7: 10, 10: 13}, {4: 41, 12: 38}, {5: 21, 9: 22, 13: 19}
]
communication_time_matrix24 = [
    [INF, 0, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
]
OR24 = [(14, 15, 16, 17)]

"""job13-1"""
computation_time_matrix25 = [
        {3: 46, 4: 47, 10: 44, 11: 41, 13: 50}, {5: 8, 7: 5, 10: 10, 12: 11, 15: 9}, {2: 16, 7: 12},
        {1: 7, 3: 5, 4: 13, 6: 12, 15: 8}, {6: 26, 8: 24, 10: 28}, {1: 5, 9:4, 12: 7, 15: 9},
        {2: 27, 8: 30, 10: 33, 12: 29}, {2: 40}, {3: 23, 6: 24, 7: 29, 9: 21}, {1: 12, 2: 14, 5: 19, 9: 18, 10: 17},
        {10: 47, 11: 49, 12: 50}, {4: 44, 6: 38, 13: 41}, {1: 22, 9: 21, 10: 16, 12: 18},
        {1: 15, 4: 18, 6: 13, 13: 14, 14: 19}, {3: 6, 4: 4, 6: 5, 13: 9}, {5: 15, 11: 18, 14: 13},
        {8: 15, 9: 16, 11: 19}, {2: 44, 15: 50}
    ]
communication_time_matrix25 = [
        [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR25 = [(2, 6, 7, 11, 12, 13, 14, 15, 16), (3, 4, 5), (8, 9, 10)]

"""job14-1"""
computation_time_matrix26 = [
        {3: 46, 9: 43}, {1: 10, 2: 17, 7: 11, 12: 13}, {4: 8, 7: 9, 8: 10}, {3: 18, 6: 25}, {4: 9},
        {3: 29, 4: 27, 13: 33}, {5: 30, 9: 29}, {2: 9, 3: 8}, {5: 18, 12: 10, 15: 19}, {9: 28, 15: 25},
        {4: 42, 14: 43, 15: 47}, {9: 35, 10: 31, 14: 29}, {6: 9, 10: 7}
    ]
communication_time_matrix26 = [
        [INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR26 = [(2, 3, 4), (6, 7)]

"""job15-1"""
computation_time_matrix27 = [
        {1: 20, 11: 18}, {12: 41, 13: 43}, {6: 17}, {7: 8}, {2: 12, 15: 15}, {4: 48, 5: 43},
        {9: 47}, {8: 28, 12: 30}, {2: 18, 8: 22}, {14: 50}, {8: 6, 13: 7}, {5: 48, 7: 45},
        {1: 9, 5: 10, 6: 11}, {3: 22, 6: 24, 9: 21}, {1: 42, 12: 47}
    ]
communication_time_matrix27 = [
        [INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR27 = [(2, 3, 4, 5), (8, 9, 10)]

"""job16-1"""
computation_time_matrix28 = [
        {1: 43, 2: 45, 11: 41}, {7: 32}, {3: 33, 6: 39, 13: 35}, {4: 40,5:43,7:41,9:44,15:49},
        {1: 25, 2: 30, 6: 31}, {6: 5, 12: 10}, {3:7, 5:5, 6:9, 11:8, 14:10}, {5: 16, 7: 19, 9: 18},
        {1: 12, 4:18, 9:14, 10:9, 13:15}, {6: 19, 11:11, 12:16, 13:20, 14:21},
        {4: 31, 7:39, 8:30, 10:33, 15:40}, {5: 28, 8: 27, 14: 24}, {1: 50, 4:44, 7:47, 8:49, 15:48},
        {1: 17, 2:19, 8:20, 9:21}, {1: 8, 2:7, 4:6, 5:9, 7:10}, {9: 5, 12: 6},
        {1: 21, 3:20, 8:24, 13:19, 15:23}, {4: 26, 5: 27, 10: 24, 11: 18}, {3: 19, 11: 20},
        {7: 19, 8: 20, 14: 15, 15: 23}, {2: 27, 12: 29, 14: 14}
    ]
communication_time_matrix28 = [
        [INF, 0, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR28 = [(2, 3, 4, 5, 6, 15, 16, 17), (7, 8, 9, 10, 11, 12, 13, 14), (19, 20)]

"""job17-1"""
computation_time_matrix29 = [
        {10: 46, 11: 44}, {5: 16, 10: 13}, {4: 11}, {12: 13, 13: 14}, {7: 11, 12: 17},
        {13: 46}, {2: 23, 11: 19}, {1: 20, 5: 18, 9: 17}, {2: 29, 12: 30}, {13: 16, 15: 13},
        {1: 24}, {4: 21, 8: 17}, {6: 33}, {1: 17, 3: 12, 6: 14}, {5: 8, 8: 7}, {1: 5, 8: 8},
        {2: 42}, {2: 15, 10: 18}, {1: 6, 6: 7}, {9: 5, 10: 10, 11: 9}, {3: 15, 12: 18},
        {6: 19, 11: 17, 14: 20}
    ]
communication_time_matrix29 = [
        [INF, 0, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR29 = [(2, 7, 8, 11), (3, 4, 5, 6), (9, 10), (14, 15, 16), (19, 20, 21)]

"""job18-1"""
computation_time_matrix30 = [
        {3: 8, 8: 13}, {5: 16, 6: 12, 8: 13}, {2: 21}, {1: 13, 5: 16, 10: 18}, {9: 17},
        {5: 46, 8: 47}, {3: 44, 7: 48, 13: 49}, {5: 17, 6: 14, 13:10}, {8: 16, 15: 13},
        {3: 28, 11: 27, 15: 30}, {10: 48, 13: 50}, {5: 31, 13: 32, 15: 36},
        {3: 30, 6: 28, 9: 26}, {2: 11}, {1: 16, 14: 18}, {4: 18, 15: 19}, {3: 36, 10: 32, 14: 35}
    ]
communication_time_matrix30 = [
        [INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ]
OR30 = [(2, 3, 4, 5), (8, 9), (13, 14, 15)]

output_filename = "integrate_data.py"
with open(output_filename, 'w') as f:
    f.write("inf = float('inf')\n")
print("start")

# 消融实验用的数据
# problem = [[2, 6, 8, 15, 18, 17, 19], [1, 6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30], [1, 3, 5, 7, 9, 10, 16, 17, 14, 13, 18, 20, 22, 24, 25, 27, 29, 30 ], [3, 21, 10, 7, 6, 13, 15, 2, 18, 20, 27, 8, 1, 29, 30], [5, 6, 3, 9, 28, 25, 8, 30, 17, 4, 13, 11, 19, 12, 2, 1, 14, 15, 7, 24, 22, 10, 26, 23], [19, 25, 18, 17, 1, 13, 26, 30, 5, 30, 21, 14, 18, 17, 6, 7, 2, 9, 5, 19, 12, 11, 29, 25, 27, 20, 23, 1, 10, 16, 28, 4, 13, 3, 2, 8]]
# 小规模算法实验用的数据

problem = [ [2, 6, 8, 10, 12], [1, 2, 4, 7, 9, 12], [2, 3, 6, 7, 9, 10], [2, 6, 8, 9, 10, 11],
           [3, 4, 6, 7, 8, 10], [3, 4, 7, 8, 10, 12], [1, 3, 6, 7, 9, 11], [2, 4, 6, 8, 10, 12],
           [2, 3, 4, 7, 8, 9], [4, 6, 7, 8, 9, 10]]
# 迭代对比实验用的数据
# problrm=[[9, 12, 20, 3, 16, 24, 28, 6, 15, 1, 29, 7, 30, 17, 4, 25, 11, 22],[13, 5, 26, 9, 2, 20, 18, 23, 15, 1, 27, 7, 14, 29, 11, 3, 21, 30],[7, 19, 28, 2, 30, 12, 6, 22, 13, 5, 16, 24, 9, 27, 20, 15, 10, 1], [8, 15, 1, 27, 4, 30, 11, 23, 7, 19, 29, 6, 16, 20, 12, 25, 5, 13],
#           [11, 4, 23, 8, 14, 25, 3, 18, 21, 29, 12, 7, 30, 1, 27, 9], [2, 10, 24, 20, 5, 7, 25, 12, 29, 6, 14, 3], [27, 4, 11, 23, 7, 19, 6, 16, 20, 12, 25, 5, 13],[17, 3, 24, 30, 9, 14, 7, 22, 11, 5, 19, 12, 6, 23, 20, 1], [2, 25, 10, 15, 8, 30, 3, 21, 19, 6, 5, 14, 7, 17],
#           [18, 4, 29, 20, 1, 27, 7, 12, 21, 6, 15, 5, 19, 13, 25]
#           ]
# problem = [[9, 12, 20, 3, 16, 24, 28, 6, 15, 1, 29, 7, 30, 17, 4, 25, 11, 22], [13, 5, 26, 9, 2, 20, 18, 23, 15, 1, 27, 7, 14, 29, 11, 3, 21, 30],
#            [7, 19, 28, 2, 30, 12, 6, 22, 13, 5, 16, 24, 9, 27, 20, 15, 10, 1], [11, 4, 23, 8, 14, 25, 3, 18, 21, 29, 12, 7, 30, 1, 27, 9, 19, 6], [16, 2, 10, 24, 20, 5, 7, 25, 28, 12, 29, 6, 14, 3, 19, 22, 30, 11],
#            [8, 15, 1, 27, 4, 30, 11, 23, 7, 19, 29, 6, 16, 20, 12, 25, 5, 13], [17, 3, 24, 30, 9, 14, 7, 28, 22, 11, 5, 19, 12, 27, 6, 23, 20, 1],
#            [2, 25, 10, 15, 29, 12, 8, 30, 3, 21, 19, 6, 27, 5, 14, 22, 7, 17], [18, 4, 29, 20, 1, 27, 7, 12, 21, 6, 15, 5, 30, 23, 19, 10, 13, 25]]




for pro in range(0, len(problem)):
    print(f'pro{pro + 1}', problem[pro])
    targetms = 0  # 不设定目标值的情况
    targetet = INF
    a = []
    b = []
    c = []
    for job in problem[pro]:
        computation_time_matrix = eval(f'computation_time_matrix{job}')
        if isinstance(computation_time_matrix, list):
            a.extend(computation_time_matrix)
        else:
            time_op = computation_time_matrix[0]
            a.extend(time_op)
        communication_time_matrix = eval(f'communication_time_matrix{job}')
        if isinstance(communication_time_matrix, list):
            communication_time_matrix = [communication_time_matrix]
            b.extend(communication_time_matrix)
        else:
            com = communication_time_matrix[0]
            com = [com]
            b.extend(com)
        OR = eval(f'OR{job}')
        if isinstance(OR, list):
            OR = [OR]
            c.extend(OR)
        else:
            OR = OR[0]
            OR = [OR]
            c.extend(OR)
# print(a)
# print(b)
# print(c)
    computation_time_matrix, communication_time_matrix, OR = final_matrix(a, b, c)
    length = len(computation_time_matrix)

    with open(output_filename, 'a') as f:
        f.write(f'num_operations{pro + 1} = {length},\n')
        f.write(f"computation_time_matrix{pro + 1} = [")
        for idx, item in enumerate(computation_time_matrix, 1):
            if idx % 3 == 1:
                f.write("    ")
            f.write(str(item))
            if idx % 3 == 0 and idx != len(computation_time_matrix):
                f.write(",\n")
            elif idx != len(computation_time_matrix):
                f.write(", ")
            else:
                f.write("]\n")

        f.write(f"communication_time_matrix{pro + 1} = [\n")
        for idx, row in enumerate(communication_time_matrix):
            f.write(" " * 31)  # 添加空格对齐
            f.write("[")
            for i, val in enumerate(row):
                f.write(f"{val}")
                if i < len(row) - 1:
                    f.write(", ")
            f.write("]")
            if idx < len(communication_time_matrix) - 1:
                f.write(",\n")
            else:
                f.write("\n]\n")
        f.write(f"OR{pro + 1} = {OR}\n")
        f.write("\n")




