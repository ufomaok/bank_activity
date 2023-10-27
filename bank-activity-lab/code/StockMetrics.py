import statistics as stats
from code.StockData import StockData




class StockMetrics(StockData):
    def __init__(self, path):
        #Call  parent method's constructor
        super(StockMetrics, self).__init__(path)

        #Running self.load to interact with self.data
        self.load()
    
    def average01(self):
        averages = []

        #Iterating over each row of data
        #For loop iterating through each row
        for row in self.data:
            data_row = row[1:]

            #Creating new variable y, to store list of float values for all rows (excluding header)
            y = []

            #For loop iterating through each row in new saved values (data_row)
            #Using append to store floats for all rows in the y variable

            for x in data_row:
                try:
                    y.append(float(x))

                #Except Value Error will skip over invalid values
                except ValueError:
                    continue

            #Created new variable to store mean of y variable list values
            newaverage = stats.mean(y)
            
            #Appending mean values (rounded to three decimals) to averages variables
            rounded_average = round(newaverage, 3)
            averages.append(rounded_average)

        return averages


    def median02(self):
        medians = []

        #Iterating over each row of data
        #For loop iterating through each row           
        for row in self.data:
            data_row2 = row[1:]

            #Creating new variable y2, to store list of float values for all rows (excluding header)
            y2 = []

            #For loop iterating through each row in new saved values (data_row2)
            #Using append to store floats for all rows in the y variable
            for x in data_row2:
                try:
                    y2.append(float(x))

                #Except Value Error will skip over invalid values
                except ValueError:
                    continue

            #Created new variable to store mean of y2 variable list values
            newmedian = stats.median(y2)

            #Appending median values into medians variable
            medians.append(newmedian)

        return medians
    

    def stddev03(self):
        sdeviation = []

        #Iterating over each row of data
        #For loop iterating through each row 
        for row in self.data:
            data_row3 = row[1:]

            #Creating new variable y3, to store list of float values for all rows (excluding header)
            y3 = []
            for x in data_row3:
                try: 
                    y3.append(float(x))

                #Except Value Error will skip over invalid values
                except ValueError:
                    continue

            #Created new variable to store standard deviation of y3 variable list values
            new_sd = stats.stdev(y3)

            #Created new variable to rounded values (by three decimals)
            new_sd2 = round(new_sd, 3)

            #Appending rounded values into sdeviation variable
            sdeviation.append(new_sd2)

        return sdeviation



