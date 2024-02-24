class Matrix: 
    def __init__(self, rows = 0, cols = 0, elements = []):
        self.rows = rows
        self.cols = cols
        self.elements = elements

    def input_matrix(self): 
        self.elements = []
        while True:
            try:
                print('введите  числа:')
                self.rows, self.cols = int(input('количество строк - ')), int(input('количество столбцов - '))
            except ValueError:
                continue 
            else:
                break
        for i in range(self.rows):
            self.elements.append(list(map(float, input(f'введите элементы строки №{i+1}: ').split())))                  
            if len(self.elements[i]) != self.cols:
                raise ValueError('проверьте корректность введенных данных')
        
    def __str__(self):
        output = ''
        for j in range(self.rows):
            output += ' '.join(str(i) for i in self.elements[j]) + '\n'
        return output