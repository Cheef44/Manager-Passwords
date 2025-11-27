#Класс поиска записей по ключевым словам
class Search:
    def __init__(self, key_name:str, array:list):
        self.key_name = key_name
        self.array = array
    
    #Метод поиска в многомерном списке
    def multidimensional_array(self):
        sorted_array = []
        for array in range(len(self.array)):
            for value in range(len(self.array[array])):
                if self.key_name in str(self.array[array][value]):
                    sorted_array.append(array)
                    break
        
        if len(sorted_array) > 0:
            return sorted_array
        return None
            