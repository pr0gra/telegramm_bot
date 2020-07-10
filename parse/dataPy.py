class Data():
    def __init__(self, values): #Принимаем сюда все компонетены парсинга
        self.names = values[::3] #Название банков сюды

        del values[::3]
        
        self.buys = values[::2] #цены покупки
        self.sells = values[1::2] #цены продажи

        self.best_buy_value = max(self.buys)
        self.best_sell_value = min(self.sells)  

    def get_all_list(self):
        message = ''
        i = 0
        while i < len(self.names):
            message += f'{self.names[i]}: \nПродажа: {self.buys[i]} \nПокупка:{self.sells[i]} \n\n'
            i += 1 
        
        message = message.rstrip()

        return message 
    

    def __get_best_values(self, values, best_value):
        message = ''

        i = 0 
        while i < len(values):
            if values[i] == best_value:
                message += f'{self.names[i]} - {best_value}\n' #Привязываем лучшую цену к названию банка
            i += 1 

        message = message.rstrip()
        return message

    def get_best_buy_value(self):
        return self.__get_best_values(self.buys, self.best_buy_value)
    
    def get_best_sell_value(self):
        return self.__get_best_values(self.sells, self.best_sell_value)