#!/usr/bin/env python3
dataList = [
    {"name": "AdviceController", "time": "1,352,000"},
    {"name": "AdviceService", "time": "1,339,000"},
    {"name": "AlertController", "time": "214,700"},
    {"name": "AlertService", "time": "1,166,000"},
    {"name": "AlexaService", "time": "81,950"},
    {"name": "AlexaController", "time": "26,970"},
    {"name": "BasicErrorController", "time": "26,434 923"},
    {"name": "ConfigController", "time": "39,970"},
    {"name": "ContentController", "time": "20,890,000"},
    {"name": "ContentFulService", "time": "16,713 287,600"},
    {"name": "ContentService", "time": "78,450,000"},
    {"name": "CsToolsConverter", "time": "34,338 5,496,000"},
    {"name": "DailyContentController", "time": "111,500"},
    {"name": "DiaperController", "time": "56,534 670,900"},
    {"name": "DiaperService", "time": "14,220,000"},
    {"name": "FeedingController", "time": "2,569,000"}
]


# calculate the percentage of cumulative time for each Controller, print them out in order from highest to lowest.
# The cumulative time is the last column in each row. Only do the Controllers

def time_to_int(time):
    return int(float(time.replace(',', '').replace(' ', '')))


totalTime = 0
for item in dataList:
    totalTime = totalTime + time_to_int(item['time'])
print('total time:', totalTime)

for item in dataList:
    if 'Controller' in item['name']:
        time = time_to_int(item['time'])
        percent = time / totalTime * 100
        print(item["name"] + '  ' + str('%f' % percent) + '%')
