import random

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





    


if __name__ == "__main__":
    dataset = read_in_file('iris.data')
    (traing_set, testing_set) = separate_dataset(dataset)
