import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open(name,'r') as file:
        all_data.append(file.readlines())
    print(f'Read file {name} complete')
    print(len(all_data))



if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_files = []
        for i in range(1,5):
            all_files.append(f'./file {i}.txt')
        start = datetime.datetime.now()
        pool.map(read_info, all_files)
    end = datetime.datetime.now()
    print(end - start)



# start = datetime.datetime.now()
# for i in range(1,5):
#     read_info(f'./file {i}.txt')
#
# end = datetime.datetime.now()
# print(end - start)

#1 0:00:02.351793
#2 0:00:00.849328