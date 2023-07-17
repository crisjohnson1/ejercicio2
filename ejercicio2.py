import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
        valores = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jota", "Reina", "Rey"]
        self.cartas = []

        for palo in palos:
            for valor in valores:
                carta = Carta(palo, valor)
                self.cartas.append(carta)

    def barajar(self):
        random.shuffle(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) == 0:
            return None
        return self.cartas.pop()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
        print(f"Mano de {self.nombre}:")
        for carta in self.mano:
            print(carta)

    def calcular_puntaje(self):
        puntaje = 0
        num_as = 0

        for carta in self.mano:
            if carta.valor.isdigit():
                puntaje += int(carta.valor)
            elif carta.valor != "As":
                puntaje += 10
            else:
                num_as += 1

        for _ in range(num_as):
            if puntaje + 11 <= 21:
                puntaje += 11
            else:
                puntaje += 1

        return puntaje

class JuegoBlackjack:
    def __init__(self):
        self.mazo = Mazo()
        self.mazo.barajar()

    def repartir_cartas_iniciales(self, jugador, crupier):
        jugador.recibir_carta(self.mazo.sacar_carta())
        crupier.recibir_carta(self.mazo.sacar_carta())
        jugador.recibir_carta(self.mazo.sacar_carta())
        crupier.recibir_carta(self.mazo.sacar_carta())

    def jugar(self):
        jugador = Jugador("Jugador")
        crupier = Jugador("Crupier")

        self.repartir_cartas_iniciales(jugador, crupier)

        print("=== Comienza el juego ===\n")
        jugador.mostrar_mano()
        print("\n")

        while True:
            opcion = input("¿Deseas tomar otra carta? (s/n): ")

            if opcion.lower() == "s":
                jugador.recibir_carta(self.mazo.sacar_carta())
                jugador.mostrar_mano()

                if jugador.calcular_puntaje() > 21:
                    print("\n¡Te pasaste de 21! ¡Has perdido!")
                    break
                elif jugador.calcular_puntaje() == 21:
                    print("\n¡Has obtenido 21! ¡Ganaste!")
                    break
            else:
                crupier.mostrar_mano()

                while crupier.calcular_puntaje() < 17:
                    crupier.recibir_carta(self.mazo.sacar_carta())
                    crupier.mostrar_mano()

                if crupier.calcular_puntaje() > 21:
                    print("\n¡El crupier se pasó de 21! ¡Ganaste!")
                elif crupier.calcular_puntaje() > jugador.calcular_puntaje():
                    print("\n¡El crupier tiene un puntaje mayor! ¡Has perdido!")
                elif crupier.calcular_puntaje() < jugador.calcular_puntaje():
                    print("\n¡Tienes un puntaje mayor al crupier! ¡Ganaste!")
                else:
                    print("\n¡Es un empate!")

                break

# Ejemplo de uso
juego = JuegoBlackjack()
juego.jugar()
