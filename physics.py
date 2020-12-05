# Physics constants
G = 6.67*10**-11
g = 9.81
PI = 3.14

def newton_law(mass, acceleration) :
    f =  mass * acceleration
    return f

def newton_gravitation(mass1, mass2, distance) :
    f = (G * mass1 * mass2)/(distance**2)
    return f

def friction_force(friction_coefficient, mass) :
    f = friction_coefficient * mass * g
    return f

def hook_law(elastic_costant, distance) :
    f = elastic_costant * distance
    return f

def uniform_motion_straight_line(velocity, time, initial_position = 0) :
    p = initial_position + (velocity * time)
    return p

def motion_under_constant_acceleration(acceleration, time, initial_position = 0, initial_velocity = 0) :
    s = initial_position + (initial_velocity * time) + (1/2 * (acceleration * time**2))
    return s

def motion_under_gravity(time, initial_height = 0, initial_velocity = 0) :
    y = initial_height + (initial_velocity * time) + (1/2(g * time**2))
    return y

def acceleration_uniform_circular_motion(linear_velocity, radius) :
    a = (linear_velocity**2/radius)
    return a

def linear_velocity_uniform_circular_motion(period, radius) :
    v = (2 * PI * radius) / period
    return v

def kinetic_energy(mass, velocity) :
    t = 1/2 * mass * velocity**2
    return t

def linear_momentum(mass, velocity) :
    p = mass * velocity 
    return p
