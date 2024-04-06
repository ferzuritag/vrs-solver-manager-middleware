import os

config = {
    'available_services': {
        'vrp': {
            'name': 'Problema de Ruteo de Vehiculos',
            'path':  os.getenv('VRP_API_PATH')
        },
        'cvrp': {
            'name': 'Problema de Ruteo de Vehiculos con Capacidad Limitada',
            'path':  os.getenv('CVRP_API_PATH')
        },
        'mdvrp': {
            'name': 'Problema de Ruteo de Vehiculos con Capacidad Limitada',
            'path':  os.getenv('MDVRP_API_PATH')
        }
    }
}