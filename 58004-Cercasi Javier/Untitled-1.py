@parameterized.expand([
        # Test entradas validas
        (4, [2, 3, 2], [1, 2, 2]),
        (9, [1, 2, 3], [0, 1, 3]),
        # Test entradas NO validas
        (9, ["a", 2, 3, 1], [1, 2, 1]),
        (9, [1, 11, 1, 1, 2, 3], [0, 1, 3])
    ])
    def test_getValues(self, size, numbers, expected):
        self.ui.sizev = size
        mock = MagicMock()
        mock.side_effect = numbers
        with patch("builtins.input", new=mock):
            result = self.ui.getValues()
        self.assertEqual(result, expected)



        def getValues(self):
        # Toma valores para las coordenadas y para el valor de la casilla
        number = 0
        row = 0
        column = 0
        while not self.numberInput(number) or not self.position(row, column):
            try:
                row = int(input("\nFila: "))
                column = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
                if not (self.numberInput(number) and
                        self.position(row, column)):
                    raise ValueError
            except ValueError:
                print("Ingresaste un valor no permitido, intentalo de nuevo")
        uinput = [row - 1, column - 1, number]
        return uinput