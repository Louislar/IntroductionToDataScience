import random
from collections import Counter

def read_in_file(file_name):
    '''
    讀入檔案
    '''
    input_file = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(',')
            input_file.append(line)
    input_file = input_file[:-1]
    return input_file

def separate_dataset(dataset):
    '''
    切分training、testing
    '''
    dataset_length = len(dataset)

    dataset_label1 = [data for data in dataset if data[4] == 'Iris-setosa']
    dataset_label2 = [data for data in dataset if data[4] == 'Iris-versicolor']
    dataset_label3 = [data for data in dataset if data[4] == 'Iris-virginica']

    # 切分testing n = 25, training n = 25
    random.shuffle(dataset_label1)
    random.shuffle(dataset_label2)
    random.shuffle(dataset_label3)

    dataset_label1_testing = dataset_label1[0:25]
    dataset_label2_testing = dataset_label2[0:25]
    dataset_label3_testing = dataset_label3[0:25]

    dataset_label1_training = dataset_label1[25:]
    dataset_label2_training = dataset_label2[25:]
    dataset_label3_training = dataset_label3[25:]

    dataset_training = dataset_label1_training + dataset_label2_training + dataset_label3_training
    dataset_testing = dataset_label1_testing + dataset_label2_testing + dataset_label3_testing
    return dataset_training, dataset_testing

def distance_measurement(data_point1, data_point2):
    '''
    衡量兩個資料點的距離函數
    預設資料點最後一個欄位是label所以會忽略
    使用歐拉距離
    '''
    dis = 0
    for index in range(0, len(data_point1)-1): 
        substract_num = float(data_point1[index]) - float(data_point2[index])
        power_num = substract_num ** 2
        dis += power_num
    return dis

def nearest_neighbor(dataset_training, datapoint_testing, k=5):
    '''
    找(排序)最近的資料點
    '''
    
    dataset_distance = [distance_measurement(entry, datapoint_testing) for entry in dataset_training]
    # print(dataset_distance)
    # dictionary of [距離] : [該距離對應的資料點]
    dataset_distance_dict = {}
    for index in range(0, len(dataset_distance)):
        dataset_distance_dict[dataset_distance[index]] = dataset_training[index]
    dataset_distance_dict = { k:dataset_distance_dict[k] for k in sorted(dataset_distance_dict)}

    # 根據k是多少，就從排序資料點拉多少資料出來投票
    vote_datapoint_list = [ dataset_distance_dict[entry] for entry in dataset_distance[0:k]]
    # print(vote_distance_list)
    vote_label_list = [entry[4] for entry in vote_datapoint_list]
    # print(vote_label_list)
    vote_result_dict = Counter(vote_label_list)
    print(dict(vote_result_dict))
    # 投票結果再sort一次
    
    


    return dataset_distance_dict




if __name__ == "__main__":
    dataset = read_in_file('iris.data')
    (traing_set, testing_set) = separate_dataset(dataset)
    # print(distance_measurement([1, 2, 3, 4, 'abc'], [5, 6, 7, 8, 'bcd']))
    traing_set_distance = nearest_neighbor(traing_set, testing_set[0])
    

