from environment import Environment
from uniform_cost_search import uniform_cost_search

def main():
    env = Environment("Prueba1.txt")
    path, cost, nodes_expanded, max_depth, computation_time = uniform_cost_search(env)
    
    print("Ruta encontrada:", path)
    print("Costo de la ruta:", cost)
    print("Cantidad de nodos expandidos:", nodes_expanded)
    print("Profundidad máxima del árbol de búsqueda:", max_depth)
    print("Tiempo de cómputo:", computation_time, "segundos")

if __name__ == "__main__":
    main()

