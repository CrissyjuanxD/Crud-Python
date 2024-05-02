class Company {
  static next = 0;  // Variable de clase (estática) para almacenar el próximo ID disponible
  #id // definicion del atributo privado
  // Método constructor que se ejecuta cuando se instancia la clase
  constructor(name = "Melissa", ruc = "0943213456001") {
    // Incrementa el contador de ID para cada nueva instancia
    Company.next++;
    // Variables de instancia
    this.#id = Company.next;  // Asigna el ID único a la instancia actual (privado)
    this.business_name = name;  // Asigna el nombre de la empresa a la instancia actual
    this.ruc = ruc;  // Asigna el RUC de la empresa a la instancia actual
  }

  // Método de usuario que muestra la información de la empresa (ID, nombre y RUC)
  show() {
    console.log(`Id:${this.#id} Empresa: ${this.business_name} ruc:${this.ruc}`);
  }
}

console.log("***********************************************************");
// Crea dos instancias (objetos) de la clase Company con nombres diferentes
const comp1 = new Company("Supermaxi");
const comp2 = new Company(undefined,ruc="9999999999001");
// Muestra la información de la primera empresa
comp1.show();
console.log("-----------------------------------------------------------");
// Muestra la información de la segunda empresa
comp2.show();
console.log("-----------------------------------------------------------");
// comp2.#id=3
console.log(Company.next);
