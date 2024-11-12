import math

class Lanzamiento:
    def __init__(self, angulo):
        self.g = 9.8  # Aceleración gravitacional en m/s^2
        self.R = int(input("Introduce el valor del alcance máximo: "))  # Alcance máximo
        self.angulo = math.radians(angulo)  # Ángulo de lanzamiento en radianes
        self.K = float(input("Introduce el valor de la constante del resorte: "))  # Constante del resorte 
        self.m = int(input("Introduce el valor de m: "))  # Masa
     
    def calcular_velocidad_inicial(self):
        # Calcular el valor de sin(2*ángulo) en radianes
        seno_doble = math.sin(2 * self.angulo)
        
        # Calcular la velocidad inicial usando la fórmula
        velocidad_inicial = math.sqrt((self.g * self.R) / seno_doble)
        print(f"Velocidad inicial calculada: {velocidad_inicial:.2f} m/s")
        return velocidad_inicial
    
    def calcular_compresion_resorte(self):
        # Calcular la compresión del resorte (ΔX)
        Delta_X = math.sqrt((self.m * self.calcular_velocidad_inicial()**2) / self.K)
        print(f"Compresión del resorte calculada: {Delta_X:.2f} cm")
        return Delta_X

# Ejemplo de uso
lanzamiento = Lanzamiento(30)  # Ángulo en grados
lanzamiento.calcular_velocidad_inicial()
lanzamiento.calcular_compresion_resorte()



