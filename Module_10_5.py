import multiprocessing
import datetime




def read_info(name):
    all_data = list()
    with open(name,encoding='utf-8') as file:
        for i in file:
            all_data.append(file.readline())
        return
# время выполнения линейным способом:0:00:06.423317
# время выполнения многопроцессным способом:0:00:03.343112

start = datetime.datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info,filenames)

#for i in filenames: read_info(i) - использовалось для линейного выполнения

    end = datetime.datetime.now()
    print(end-start)