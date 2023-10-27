
import statistics as stats
from code.StockData import StockData




class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        averages = []

        #iterate over each row of data
        #for loop will go through each row
        #take the row and save it as a row

        for row in self.data:
            data_row = row[1:]

            y = []
            for x in data_row:
                try:
                    y.append(float(x))
                except ValueError:
                    continue

            #use stats package to find mean of y
            newaverage = stats.mean(y)
            
            #now append list of average AND round to three decimals
            rounded_average = round(newaverage, 3)
            averages.append(rounded_average)

        return averages


    def median02(self):
        medians = []
        
       
        for row in self.data:
            data_row2 = row[1:]

            y2 = []
            for x in data_row2:
                try:
                    y2.append(float(x))
                except ValueError:
                    continue

            newmedian = stats.median(y2)

            medians.append(newmedian)

        return medians
    

    def stddev03(self):
        sdeviation = []

        for row in self.data:
            data_row3 = row[1:]

            y3 = []
            for x in data_row3:
                try: 
                    y3.append(float(x))
                except ValueError:
                    continue

            new_sd = stats.stdev(y3)

            new_sd2 = round(new_sd, 3)
            sdeviation.append(new_sd2)

        return sdeviation



