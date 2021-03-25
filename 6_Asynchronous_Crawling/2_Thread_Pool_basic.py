# import time
#
# def get_page(str):
#      print('Downloading...: ', str)
#      time.sleep(2)
#      print('Successful: ', str)
#
# name_list = ['xiaozi','aa','bb','cc']
#
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%ds'% (end_time-start_time))


#Using Thread Pool----------------
import time

#import Thread Pool package
from multiprocessing.dummy import Pool
start_time = time.time()
def get_page(str):
     print('Downloading...: ', str)
     time.sleep(2)
     print('Successful: ', str)
name_list = ['xiaozi','aa','bb','cc']

#Pool instance
pool = Pool(4)
#Send each element in the list to get_page method
pool.map(get_page,name_list)

end_time = time.time()
print('%ds'% (end_time-start_time))

