import matplotlib.pyplot as plt

class SparseSet:
    def __init__(self, n):
        self.n = n
        self.sparse = [-1] * n
        self.dense = [0] * n
        self.size = 0

    def insert(self, x):
        if self.contains(x):
            return
        self.sparse[x] = self.size
        self.dense[self.size] = x
        self.size += 1

    def remove(self, x):
        if not self.contains(x):
            return
        idx = self.sparse[x]
        last = self.dense[self.size - 1]
        self.dense[idx] = last
        self.sparse[last] = idx
        self.sparse[x] = -1
        self.size -= 1

    def contains(self, x):
        return 0 <= x < self.n and self.sparse[x] < self.size and self.dense[self.sparse[x]] == x

    def visualize(self, operation=None):
        fig, ax = plt.subplots(2, 1, figsize=(10, 6))

        ax[0].set_title("Dense Array")
        ax[0].bar(range(self.size), self.dense[:self.size], color="skyblue")
        for i, val in enumerate(self.dense[:self.size]):
            ax[0].text(i, val + 0.1, str(val), ha='center', va='bottom')
        ax[0].set_xlim(-1, self.n)
        ax[0].set_ylim(0, self.n)
        ax[0].set_xticks(range(self.n))
        ax[0].grid(axis='x', linestyle='--', alpha=0.6)

        ax[1].set_title("Sparse Array")
        sparse_vals = self.sparse
        ax[1].bar(range(self.n), sparse_vals, color="lightcoral")
        for i, val in enumerate(sparse_vals):
            ax[1].text(i, val + 0.1, str(val), ha='center', va='bottom')
        ax[1].set_xlim(-1, self.n)
        ax[1].set_ylim(-1, self.n)
        ax[1].set_xticks(range(self.n))
        ax[1].grid(axis='x', linestyle='--', alpha=0.6)

        if operation:
            fig.suptitle(f"Estado del Sparse-Set despues de {operation}", fontsize=16)
        else:
            fig.suptitle("Estado del Sparse-Set", fontsize=16)
        plt.tight_layout()
        plt.show()

def interactive_sparse_set():
    n = int(input("Introduce el tamanio del sparse-set (por ejemplo, 10): "))
    sparse_set = SparseSet(n)

    print("\nComandos:")
    print("  insert <x>: Agregar un elemento x al sparse set.")
    print("  remove <x>: Eliminar un elemento x del sparse set.")
    print("  contains <x>: Verificar si x esta en el sparse set.")
    print("  exit: Salir de la sesion.\n")

    while True:
        command = input("Introduce un comando: ").strip().lower()
        if command.startswith("insert"):
            try:
                x = int(command.split()[1])
                if x < 0 or x >= n:
                    print(f"Error: {x} esta fuera de los limites (0 a {n-1}).")
                else:
                    sparse_set.insert(x)
                    print(f"Insertado {x}.")
                    sparse_set.visualize(f"insert({x})")
            except (IndexError, ValueError):
                print("Formato de comando invalido. Uso: insert <x>")
        elif command.startswith("remove"):
            try:
                x = int(command.split()[1])
                if x < 0 or x >= n:
                    print(f"Error: {x} esta fuera de los limites (0 a {n-1}).")
                else:
                    sparse_set.remove(x)
                    print(f"Eliminado {x}.")
                    sparse_set.visualize(f"remove({x})")
            except (IndexError, ValueError):
                print("Formato de comando invalido. Uso: remove <x>")
        elif command.startswith("contains"):
            try:
                x = int(command.split()[1])
                if x < 0 or x >= n:
                    print(f"Error: {x} esta fuera de los limites (0 a {n-1}).")
                else:
                    result = sparse_set.contains(x)
                    print(f"{x} esta {'en' if result else 'no esta en'} el sparse set.")
            except (IndexError, ValueError):
                print("Formato de comando invalido. Uso: contains <x>")
        elif command == "exit":
            print("Saliendo. Adios!")
            break
        else:
            print("Comando invalido. Intenta de nuevo.")

interactive_sparse_set()
