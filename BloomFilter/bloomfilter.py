'''Bloom filter data structure for pokemons Pikachu and Charmander.
A toy example script.
'''
import pyhash

bit_vector = [0]*20

# Non criptographic hash functions (Murmur nad FNV)

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output of FNV and Murmur hash functions for Pikachu and Charmander. 

fnv_pika = fnv('Pikachu') % 20
fnv_char = fnv('Charmander') % 20

murmur_pika = murmur('Pikachu') % 20
murmur_char = murmur('Charmander') % 20

print(fnv_pika)
print(fnv_char)
print(murmur_pika)
print(murmur_char)

# Flip the bits of bit_vector in the corresponding locations from above hashes.

bit_vector[fnv_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_pika] = 1
bit_vector[murmur_char] = 1

# A wild Bulbasaur appears!
# Calculate output of FNV and Murmur hash for Bulbasaur.
fnv_bulb = fnv('Bulbasaur') % 20
murmur_bulb = murmur('Bulbasaur') % 20

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb])

# Flip the bits in the Bloom filter to indicate that we now have captured Bulbasaur.
bit_vector[fnv_bulb] = 1
bit_vector[murmur_bulb] = 1
print(bit_vector)


