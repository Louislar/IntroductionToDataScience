

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
    return input_file

def separate_dataset(dataset):
    '''
    切分training、testing
    '''
    dataset_length = len(dataset)


if __name__ == "__main__":
    dataset = read_in_file('iris.data')
    print(dataset)