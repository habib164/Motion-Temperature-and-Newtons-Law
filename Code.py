t_mass = int(input("What's the mass of the object? "))
print("The mass is", t_mass)

t_acceleration = int(input("What's the acceleration of the object? "))
print("The acceleration is", t_acceleration)

t_distance = int(input("What's the distance of the object? "))
print("The acceleration is", t_distance)

bomb_mass = int(input("What's the mass of the a bomb? "))
print("The mass of the bomb is", bomb_mass)

print("Calculating...............")


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius  = f_to_c(int(input("Input the temperature in Fahrenheit: ")))
print(f100_in_celsius, "Celcius")

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(int(input("Input the temperature in Celcius: ")))
print(c0_in_fahrenheit, "Fahrenheit")

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

t_force = get_force(t_mass, t_acceleration)
#print(train_force)

print("The GE train supplies " + str(t_force) + " Newtons of force.")

def get_energy(mass, c=3 * (10**8)):
  energy = mass * c**2
  return energy

bomb_energy = get_energy(bomb_mass)
#print(bomb_energy)

print("A 1kg bomb supplies", bomb_energy, "Joules.")

def get_work(mass, acceleration, distance):
  work = t_force * distance
  return work

train_work = get_work(t_mass, t_acceleration, t_distance)
print("The GE train does", train_work ,"Joules of work over Y meters.")