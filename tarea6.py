import random
import csv
import sys

def generar_bases(n):
    return [random.choice(['R', 'D']) for _ in range(n)]

def generar_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generar_mensaje(n):
    bits = generar_bits(n)
    bases = generar_bases(n)
    return bits, bases

def almacenar_bases_estados(bits, bases, archivo):
    n = len(bits)
    with open(archivo, "w") as f:
      f.write("Bit Base\n")
      for row in range(n):
         f.write(f"{bits[row]}\t{bases[row]}\n")

def almacenar_bases(bases,archivo):
   with open(archivo, "w") as f:
      f.write("Base\n")
      for base in bases:
            f.write(str(base) + "\n")

def medicion(bits_emisor, bases_emisor, bases_receptor):
    bob_bits = []
    for a_bit, a_base, b_base in zip(bits_emisor, bases_emisor, bases_receptor):
        if a_base == b_base:
            bob_bits.append(a_bit)
        else:
            bob_bits.append(random.randint(0, 1))
    return bob_bits

def extraer_clave(alice_bits, bob_bits, alice_bases, bob_bases):
    indices = []
    alice_key = []
    bob_key = []
    
    for i, (a_base, b_base) in enumerate(zip(alice_bases, bob_bases)):
        if a_base == b_base:
            indices.append(i)
            alice_key.append(alice_bits[i])
            bob_key.append(bob_bits[i])
    
    return indices, alice_key, bob_key

def verificar_errores(alice_key, bob_key, muestra=50):
    largo = len(alice_key)
    if largo < muestra:
        muestra = largo
    
    indices = random.sample(range(largo), muestra)
    
    errores = 0
    for idx in indices:
        if alice_key[idx] != bob_key[idx]:
            errores += 1
    
    tasa_error = errores / muestra if muestra > 0 else 0
    
    return indices, errores, tasa_error

def simulacion_caso_normal(n : int, muestra : int):
   alice_bits, alice_bases = generar_mensaje(n)
   bob_bases = generar_bases(n)
   
   # exportar a text por separado
   almacenar_bases_estados(alice_bits, alice_bases, "alice_bb84.txt")
   #almacenar_bases(bob_bases, "bob_bb84_bases.txt")

   # realizar mediciones
   bob_bits = medicion(alice_bits, alice_bases, bob_bases)
   almacenar_bases_estados(bob_bits, bob_bases, "bob_bb84.txt")

   # comparar bases y medir errores
   indices, alice_key, bob_key = extraer_clave(alice_bits, bob_bits, alice_bases, bob_bases)
   indices_muestra, errores, tasa_error = verificar_errores(alice_key, bob_key, muestra)

   print("Alice Bits:", alice_bits)
   print("Alice Bases:", alice_bases)
   print("Bob Bases:", bob_bases)
   print("Bob Bits:", bob_bits)

   print("Alice Key:", alice_key)
   print("Bob Key:", bob_key)
   print("Cantidad de Errores:", errores)
   print("Tasa de Error:", tasa_error)

def simulacion_bajo_ataque(n : int, muestra : int):
   alice_bits, alice_bases = generar_mensaje(n)
   bob_bases = generar_bases(n)
   eve_bases = generar_bases(n)
   
   # exportar a text por separado
   almacenar_bases_estados(alice_bits, alice_bases, "alice_bb84_attack.txt")

   # realizar intercepcion
   eve_bits = medicion(alice_bits, alice_bases, eve_bases)
   almacenar_bases_estados(eve_bits, eve_bases, "eve_bb84_attack.txt")

   # realizar mediciones
   bob_bits = medicion(eve_bits, eve_bases, bob_bases)
   almacenar_bases_estados(bob_bits, bob_bases, "bob_bb84_attack.txt")

   # comparar bases y medir errores
   indices, alice_key, bob_key = extraer_clave(alice_bits, bob_bits, alice_bases, bob_bases)
   indices_muestra, errores, tasa_error = verificar_errores(alice_key, bob_key, muestra)

   print("Alice Bits:", alice_bits)
   print("Alice Bases:", alice_bases)
   print("Bob Bases:", bob_bases)
   print("Bob Bits:", bob_bits)

   print("Alice Key:", alice_key)
   print("Bob Key:", bob_key)
   print("Cantidad de Errores:", errores)
   print("Tasa de Error:", tasa_error)

if __name__ == "__main__":
   print("\n SIMULACIÓN PROTOCOLO BB84")
   print("Universidad de los Andes\n")
   
   N = 1000
   MUESTRA = 50
   
   parte1 = simulacion_caso_normal(n=N, muestra=MUESTRA)
   parte2 = simulacion_bajo_ataque(n=N, muestra=MUESTRA)
