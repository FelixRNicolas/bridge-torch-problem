#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

struct Paso {
    vector<int> cruzan;
    int tiempo;
    bool ida; // true = van hacia la derecha, false = regresa alguien
};

vector<int> personas = {1, 2, 5, 10};
int mejorTiempo = INT_MAX;
vector<Paso> mejorCamino;

// Función auxiliar para mostrar un vector
string vecToStr(const vector<int>& v) {
    string s = "(";
    for (size_t i = 0; i < v.size(); i++) {
        s += to_string(v[i]);
        if (i < v.size() - 1) s += ",";
    }
    s += ")";
    return s;
}

// Backtracking
void resolver(vector<int> izquierda, vector<int> derecha, bool antorchaIzq,
              int tiempo, vector<Paso> camino) {

    // Si todos están a la derecha → solución
    if (izquierda.empty()) {
        if (tiempo < mejorTiempo) {
            mejorTiempo = tiempo;
            mejorCamino = camino;
        }
        return;
    }

    // Poda: si ya pasa del mejor tiempo encontrado
    if (tiempo >= mejorTiempo) return;

    if (antorchaIzq) {
        // Elegir 2 personas que crucen de izquierda a derecha
        for (size_t i = 0; i < izquierda.size(); i++) {
            for (size_t j = i + 1; j < izquierda.size(); j++) {
                int a = izquierda[i], b = izquierda[j];
                int t = max(a, b);

                vector<int> newIzq = izquierda;
                vector<int> newDer = derecha;

                // quitar de izquierda
                newIzq.erase(remove(newIzq.begin(), newIzq.end(), a), newIzq.end());
                newIzq.erase(remove(newIzq.begin(), newIzq.end(), b), newIzq.end());

                // añadir a derecha
                newDer.push_back(a);
                newDer.push_back(b);

                vector<Paso> newCamino = camino;
                newCamino.push_back({{a, b}, t, true});

                resolver(newIzq, newDer, false, tiempo + t, newCamino);
            }
        }
    } else {
        // Elegir 1 persona que regrese de derecha a izquierda
        for (size_t i = 0; i < derecha.size(); i++) {
            int a = derecha[i];

            vector<int> newIzq = izquierda;
            vector<int> newDer = derecha;

            // mover de derecha a izquierda
            newDer.erase(remove(newDer.begin(), newDer.end(), a), newDer.end());
            newIzq.push_back(a);

            vector<Paso> newCamino = camino;
            newCamino.push_back({{a}, a, false});

            resolver(newIzq, newDer, true, tiempo + a, newCamino);
        }
    }
}

int main() {
    vector<int> izquierda = personas;
    vector<int> derecha;
    vector<Paso> camino;

    resolver(izquierda, derecha, true, 0, camino);

    // Mostrar solución
    cout << "Tiempo minimo: " << mejorTiempo << " minutos\n";
    cout << "Secuencia de pasos:\n";
    for (auto &p : mejorCamino) {
        if (p.ida)
            cout << vecToStr(p.cruzan) << " -> (+" << p.tiempo << ")\n";
        else
            cout << vecToStr(p.cruzan) << " <- (+" << p.tiempo << ")\n";
    }

    return 0;
}
