import time

class MeasureTime():
    @staticmethod
    def measureTime(Sorter):
        start_time = time.time()
        Sorter.Sort()
        return (time.time()-start_time)*1000